"""
Client Authentication Dependencies for FastAPI.

Injects current authenticated client user account into protected endpoints via OAuth2 Bearer token,
enforcing token revocation blacklist checks and rate limits.
"""
import logging
from decimal import Decimal
from typing import Optional

logger = logging.getLogger(__name__)
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer

from api.auth.jwt_handler import verify_token
from api.di_providers import get_account_repo, get_token_blacklist, get_rate_limiter
from core.domains.accounts.account import Account
from core.domains.accounts.enums import AccountType
from core.domains.common.value_objects import Money
from core.ports.interfaces import IAccountRepository, ITokenBlacklist, IRateLimiter

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    account_repo: Optional[IAccountRepository] = Depends(get_account_repo),
    token_blacklist: Optional[ITokenBlacklist] = Depends(get_token_blacklist)
) -> Account:
    """FastAPI dependency resolving the authenticated client Account, with fallback for dev/test."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if token_blacklist:
        try:
            revoked = await token_blacklist.is_blacklisted(token)
        except Exception as exc:  # noqa: BLE001
            # Fail CLOSED. This was `except Exception: pass`, so a revoked token was
            # accepted precisely when the blacklist was unreachable - the only moment the
            # check matters. A revocation list that cannot be read is not permission to
            # ignore revocation.
            logger.error("token blacklist unreachable, refusing the request: %s", exc)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Token revocation status unavailable; request refused",
            )
        if revoked:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has been revoked",
                headers={"WWW-Authenticate": "Bearer"},
            )

    try:
        payload = verify_token(token)
    except Exception:
        raise credentials_exception

    # NO DEFAULT. This was `payload.get("sub", "100001")`, so a token carrying no subject
    # silently became account 100001 - a login that does not exist in this database at all.
    # An absent subject is a malformed token, which is a 401.
    raw_subject = payload.get("sub")
    if raw_subject is None or str(raw_subject).strip() == "":
        raise credentials_exception
    login_id = str(raw_subject).strip()

    if account_repo is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Account lookup unavailable; request refused",
        )

    try:
        account = await account_repo.find_by_login(
            int(login_id) if login_id.isdigit() else login_id
        )
    except Exception as exc:  # noqa: BLE001
        # An OUTAGE is not "no such account". Both refuse, but they are different failures
        # and an operator must be able to tell which is happening. This was swallowed into
        # `account = None`, which then produced a FUNDED trading account - so a database
        # outage granted trading rights.
        logger.error("account lookup failed for %s: %s", login_id, exc)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Account lookup unavailable; request refused",
        )

    if account is None:
        # An unknown login is refused. This used to return an Account holding 10,000 USD
        # with margin level 999999 and NO GROUP - and with no group,
        # `Account.evaluate_margin_state()` returns an empty list, so that account could
        # never be margin-called or stopped out. An identity that cannot be loaded is not a
        # licence to trade.
        raise credentials_exception

    if not getattr(account, "is_enabled", True):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled",
        )

    return account


async def require_rate_limit(
    request: Request,
    login_id: Optional[str] = None,
    rate_limiter: Optional[IRateLimiter] = Depends(get_rate_limiter)
) -> None:
    """FastAPI dependency enforcing rate limiting."""
    if not rate_limiter:
        return

    client_ip = request.client.host if request.client else "127.0.0.1"

    if not await rate_limiter.is_allowed(f"rate_limit:ip:{client_ip}", limit=20, window_seconds=60):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded for IP address"
        )

    if login_id:
        if not await rate_limiter.is_allowed(f"rate_limit:login:{login_id}", limit=5, window_seconds=60):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded for login ID"
            )
