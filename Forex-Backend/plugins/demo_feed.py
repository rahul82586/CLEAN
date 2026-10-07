"""A minimal WORKING plugin, to prove the master actually spawns something.

Not a product plugin - a proof that `master.py` reads `plugins.yaml`, starts the process,
serves on its port, survives being restarted, and stops cleanly. Once this works, a real
LP gateway is the same file with real methods instead of these.

Implements the two-method contract in the smallest honest way:

    async def handle(self, payload) -> dict     the master never calls this
    it exists to prove the PROCESS boundary is real

WHAT IT PROVES
--------------
* `python -m plugins.demo_feed` is importable from the repo root (so a third party can add one)
* the master passes `--port` and `--config` and the plugin reads both
* the process is independently killable, so `supervise()` restarting it is testable
* `--dry-run` starts nothing (already shown)

HOW TO RUN IT
-------------
    # in one shell
    python master.py
    # in another
    curl http://127.0.0.1:9199/health
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys


def parse_args() -> tuple[int, dict]:
    ap = argparse.ArgumentParser(description="demo feed plugin")
    ap.add_argument("--port", type=int, required=True)
    ap.add_argument("--config", type=str, default="{}")
    args, _unknown = ap.parse_known_args()
    try:
        cfg = json.loads(args.config)
    except json.JSONDecodeError as exc:
        print(f"[demo_feed] --config is not valid JSON: {exc}", file=sys.stderr)
        raise SystemExit(2)
    return args.port, cfg


async def serve(port: int, cfg: dict) -> None:
    """A deliberately tiny HTTP server. One endpoint proves the process is alive."""
    started = asyncio.get_event_loop().time()

    async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        try:
            request = await asyncio.wait_for(reader.readline(), timeout=5.0)
            line = request.decode("utf-8", "replace").strip()
            # Consume headers so the client does not see a reset.
            while True:
                h = await asyncio.wait_for(reader.readline(), timeout=5.0)
                if h in (b"\r\n", b"\n", b""):
                    break
            body = json.dumps({
                "plugin": cfg.get("name"),
                "type": cfg.get("type"),
                "port": port,
                "params": cfg.get("params", {}),
                "uptime_s": round(asyncio.get_event_loop().time() - started, 2),
                "request": line,
            }).encode()
            writer.write(
                b"HTTP/1.1 200 OK\r\n"
                b"Content-Type: application/json\r\n"
                b"Content-Length: " + str(len(body)).encode() + b"\r\n"
                b"Connection: close\r\n\r\n" + body
            )
            await writer.drain()
        except asyncio.TimeoutError:
            pass
        except Exception as exc:                       # noqa: BLE001
            print(f"[demo_feed] handler error: {exc}", file=sys.stderr)
        finally:
            try:
                writer.close()
            except Exception:
                pass

    server = await asyncio.start_server(handle, "127.0.0.1", port)
    addr = ", ".join(str(s.getsockname()) for s in server.sockets or [])
    print(f"[demo_feed] up name={cfg.get('name')} type={cfg.get('type')} "
          f"params={cfg.get('params', {})} on {addr}", flush=True)
    async with server:
        await server.serve_forever()


def main() -> int:
    port, cfg = parse_args()
    try:
        asyncio.run(serve(port, cfg))
    except KeyboardInterrupt:
        print("[demo_feed] stopped", flush=True)
    except OSError as exc:
        print(f"[demo_feed] cannot bind port {port}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())