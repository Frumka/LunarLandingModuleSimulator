import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send('get')

        f = await websocket.recv()
        print("< {}".format(f))

asyncio.get_event_loop().run_until_complete(hello())