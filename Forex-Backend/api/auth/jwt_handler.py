"""Backwards-compatible re-export. The module moved to `infrastructure/security/`.

R23: `jwt_handler` imports nothing but `os`, `datetime`, `typing` and `jwt` - it has no
FastAPI or router dependency, so it was never an HTTP-layer concern. Keeping it under
`api/auth/` forced `application/services/auth_service.py` to import `api.*` at MODULE level,
which is the one edge in the `application -> api` cycle that is not lazy, and it inverts the
dependency rule (an application service must not depend on an adapter).

The file itself now lives in `infrastructure/security/jwt_handler.py`. This shim re-exports
the public names so the eight existing `from api.auth.jwt_handler import ...` call sites
keep working unchanged; new code should import from infrastructure.
"""
from infrastructure.security.jwt_handler import *  # noqa: F401,F403
from infrastructure.security.jwt_handler import (  # noqa: F401  (explicit, for `from x import y`)
    create_access_token,
    verify_token,
)

__all__ = ["create_access_token", "verify_token"]
