import asyncio
import websockets

async def main():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as ws:
        print("Conectado")

        msgs = ["oi", "mario", "alo"]

        for msg in msgs:
            await ws.send(msg)
            print(f"Recebendo: {await ws.recv()}")
             

asyncio.run(main())