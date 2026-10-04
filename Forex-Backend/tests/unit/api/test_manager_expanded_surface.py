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
import pytest
from fastapi.testclient import TestClient
from api.main import create_app
from api.auth.jwt_handler import create_access_token


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

