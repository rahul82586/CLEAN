import asyncio
import websockets
import msgpack
import json

async def main():
    async with websockets.connect('ws://127.0.0.1:8000/ws/marketdata') as ws:
        await ws.send(json.dumps({"action": "sub", "symbol": "ETHUSD"}))
        count = 0
        while count < 5:
            raw = await asyncio.wait_for(ws.recv(), timeout=5.0)
            if isinstance(raw, bytes):
                data = msgpack.unpackb(raw, raw=False)
            else:
                data = json.loads(raw)
            if data.get("s") == "ETHUSD":
                print("TICK:", data)
                count += 1

if __name__ == "__main__":
    asyncio.run(main())
