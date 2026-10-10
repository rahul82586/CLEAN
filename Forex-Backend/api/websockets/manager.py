"""
WebSocket Connection Manager

Manages active WebSocket connections for public market data streaming and
private authenticated user trade event updates.
"""
import json
import logging
from typing import Dict, List, Optional, Set
from fastapi import WebSocket

logger = logging.getLogger(__name__)


import asyncio
import os

class ConnectionManager:
    """
    Tracks and distributes messages to public broadcast streams and user-specific streams.
    Supports Phase 3 micro-batched tick frame delivery (every 20-50 ms).
    """
    def __init__(self, batch_interval_seconds: Optional[float] = None):
        self.active_connections: List[WebSocket] = []
        self.user_connections: Dict[str, Set[WebSocket]] = {}
        if batch_interval_seconds is None:
            batch_interval_seconds = float(os.environ.get("WS_TICK_BATCH_INTERVAL_SECONDS", "0.030"))
        self.batch_interval_seconds = max(0.0, float(batch_interval_seconds))
        self._tick_batch_queue: List[dict] = []
        self._flush_task: Optional[asyncio.Task] = None
        self._running = True

    async def connect_public(self, websocket: WebSocket) -> None:
        """Register an unauthenticated public stream connection."""
        await websocket.accept()
        self.active_connections.append(websocket)
        self._ensure_flush_task()
        logger.debug(f"Public WebSocket connected. Total active: {len(self.active_connections)}")

    async def connect_user(self, websocket: WebSocket, user_id: str) -> None:
        """Register an authenticated private user stream connection."""
        if user_id not in self.user_connections:
            self.user_connections[user_id] = set()
        self.user_connections[user_id].add(websocket)
        logger.debug(f"User WebSocket connected for login '{user_id}'")

    def disconnect(self, websocket: WebSocket, user_id: Optional[str] = None) -> None:
        """Unregister a disconnected WebSocket connection."""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

        if user_id and user_id in self.user_connections:
            self.user_connections[user_id].discard(websocket)
            if not self.user_connections[user_id]:
                del self.user_connections[user_id]

    def _ensure_flush_task(self) -> None:
        if self.batch_interval_seconds > 0 and (self._flush_task is None or self._flush_task.done()):
            try:
                loop = asyncio.get_running_loop()
                self._flush_task = loop.create_task(
                    self._flush_tick_batches_loop(), name="ws_tick_batch_flush"
                )
            except RuntimeError:
                pass

    async def broadcast_tick(
        self,
        symbol: str,
        bid: str,
        ask: str,
        spread: Optional[str] = None,
        timestamp: Optional[str] = None,
        ts: Optional[int] = None,
    ) -> None:
        """Broadcast a price tick to ALL public WebSocket connections (batched frame delivery)."""
        if ts is None and timestamp:
            try:
                from datetime import datetime
                ts = int(datetime.fromisoformat(timestamp).timestamp() * 1000)
            except Exception:
                pass
        if ts is None:
            import time
            ts = int(time.time() * 1000)

        if timestamp is None and ts is not None:
            try:
                from datetime import datetime, timezone
                timestamp = datetime.fromtimestamp(ts / 1000.0, tz=timezone.utc).isoformat()
            except Exception:
                pass

        tick_payload = {
            "type": "tick",
            "symbol": symbol,
            "bid": bid,
            "ask": ask,
            "spread": spread,
            "timestamp": timestamp,
            "ts": ts,
        }

        if self.batch_interval_seconds <= 0 or not self.active_connections:
            # Direct non-batched delivery if batching disabled or no connections
            await self._send_public_frame(json.dumps(tick_payload))
            return

        self._tick_batch_queue.append(tick_payload)
        self._ensure_flush_task()

    async def _flush_tick_batches_loop(self) -> None:
        while self._running:
            try:
                await asyncio.sleep(self.batch_interval_seconds)
                await self._flush_tick_batch()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.exception("Error in WS tick batch flush loop: %s", e)

    async def _flush_tick_batch(self) -> None:
        if not self._tick_batch_queue or not self.active_connections:
            self._tick_batch_queue.clear()
            return

        batch = list(self._tick_batch_queue)
        self._tick_batch_queue.clear()

        if len(batch) == 1:
            frame_str = json.dumps(batch[0])
        else:
            frame_str = json.dumps({"type": "ticks", "ticks": batch})

        await self._send_public_frame(frame_str)

    async def _send_public_frame(self, message: str) -> None:
        to_remove = []
        for connection in list(self.active_connections):
            try:
                await connection.send_text(message)
            except Exception:
                to_remove.append(connection)

        for closed_conn in to_remove:
            self.disconnect(closed_conn)

    async def send_user_update(self, user_id: str, event_type: str, payload: dict) -> None:
        """Send a private trade/risk update event to a specific user's WebSockets."""
        if user_id not in self.user_connections:
            return

        message = json.dumps({
            "type": event_type,
            "data": payload
        })
        to_remove = []
        for connection in list(self.user_connections[user_id]):
            try:
                await connection.send_text(message)
            except Exception:
                to_remove.append(connection)

        for closed_conn in to_remove:
            self.disconnect(closed_conn, user_id=user_id)

