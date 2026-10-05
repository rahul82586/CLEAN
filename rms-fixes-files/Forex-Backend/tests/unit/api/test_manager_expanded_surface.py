"""
Unit tests for expanded MT5 Manager API endpoints:
- RouteEvaluate
- NOPLimitCheck
- LPBridgeConnect
- ABookAllocation
- MarginCheck
- ForceLiquidation
- AccountStatement
- DailySummary
"""
import os
import socket
from urllib.parse import urlparse

import pytest
from fastapi.testclient import TestClient
from api.main import create_app
from api.auth.jwt_handler import create_access_token


def _database_is_reachable() -> bool:
    """N7: this test drives the REAL lifespan, which opens a PostgreSQL connection.

    It was moved onto `with TestClient(app)` for a good reason - without the context
    manager starlette starts a fresh event loop per request and the second request's
    asyncpg connection is bound to a loop the first one already closed. That was invisible
    while the manager dependency fabricated an in-memory account (R7); now that it reads
    the database, the test genuinely needs one.

    A unit-test directory must not fail on a machine without PostgreSQL, so the requirement
    is declared instead of crashing: skip with the reason when the configured host:port does
    not accept a connection. Set BROKER_TEST_DATABASE=1 to force it to run (and fail loudly)
    in an environment that is supposed to have one - that is what CI should do.
    """
    if os.environ.get("BROKER_TEST_DATABASE", "").strip().lower() in ("1", "true", "yes"):
        return True
    url = os.environ.get("DATABASE_URL", "") or "postgresql://localhost:5432"
    try:
        parsed = urlparse(url if "://" in url else f"postgresql://{url}")
        host = parsed.hostname or "localhost"
        port = parsed.port or 5432
    except ValueError:
        return False
    try:
        with socket.create_connection((host, port), timeout=0.5):
            return True
    except OSError:
        return False


pytestmark = pytest.mark.skipif(
    not _database_is_reachable(),
    reason=(
        "needs a reachable PostgreSQL for the app lifespan (manager login 1000 must exist); "
        "set BROKER_TEST_DATABASE=1 to require it"
    ),
)


def test_manager_expanded_endpoints():
    app = create_app()
    # Used as a CONTEXT MANAGER: the documented way to drive an app whose lifespan owns
    # async resources. Without `with`, starlette's `_portal_factory` starts a NEW event
    # loop for EVERY request, so the first request's asyncpg connection is bound to a loop
    # already closed by the second. That was invisible while the manager dependency never
    # touched the database - it resolved a fabricated in-memory account (R7).
    with TestClient(app) as client:

        # The subject used to be 100001, which does NOT exist as a manager - verified against
        # the live database. The request only succeeded because get_current_manager resolved
        # manager tokens through the client-plane resolver, which fabricated a funded account
        # (R7). This now uses the login the project actually provisions: manager 1000.
        token = create_access_token({"sub": "1000", "is_manager": True})
        headers = {"Authorization": f"Bearer {token}"}
    
        # 1. NOP Limit Check
        resp = client.get("/api/v1/manager/NOPLimitCheck?symbol=EURUSD&volume=10.0", headers=headers)
        assert resp.status_code == 200
        data = resp.json()
        assert data["symbol"] == "EURUSD"
        assert "recommended_action" in data
    
        # 2. LP Bridge Connect
        resp = client.post("/api/v1/manager/LPBridgeConnect", json={
            "lp_name": "LMAX",
            "protocol": "FIX4.4",
            "target_comp_id": "LMAX_GW_01"
        }, headers=headers)
        assert resp.status_code == 200
        assert resp.json()["status"] == "CONNECTED"
    
        # 3. Daily Summary Report
        resp = client.get("/api/v1/manager/DailySummary?days=3", headers=headers)
        assert resp.status_code == 200
        assert len(resp.json()) == 3
    
        # 4. Force Liquidation
        resp = client.post("/api/v1/manager/ForceLiquidation", json={
            "login": 744209,
            "comment": "Dealer stopout test"
        }, headers=headers)
        assert resp.status_code == 200
        assert resp.json()["login"] == 744209

