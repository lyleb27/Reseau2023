import asyncio
import websockets

async def client_handler():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter a string to send to the server (or 'exit' to quit): ")

            await websocket.send(message)
            if message.lower() == 'exit':
                break

            response = await websocket.recv()
            print(f"Received response from server: {response}")

asyncio.get_event_loop().run_until_complete(client_handler())
