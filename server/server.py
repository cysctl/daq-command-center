import asyncio
import websockets

async def handler(websocket):
    print("New connection established.")
    await websocket.send("Hello world!")
    
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send("Hello world!")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed!")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future() # forever

if __name__ == "__main__":
    asyncio.run(main())
