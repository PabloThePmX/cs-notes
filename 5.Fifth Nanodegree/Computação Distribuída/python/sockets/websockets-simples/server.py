import asyncio
import websockets

async def get_messages_client(websocket):
    print("Cliente conectado!")

    async for msg in websocket:
        await websocket.send(msg.upper())


async def main():
    async with websockets.serve(get_messages_client, "localhost", 8765):
        print("Rodando")
        await asyncio.Future()

asyncio.run(main())