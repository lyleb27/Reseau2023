import asyncio
import json
import websockets

async def server_handler(websocket, path):
    while True:
        try:
            message = await websocket.recv()
            print(f"Received message from client: {message}")

            response = {"message": f"Hello client! Received \"{message}\""}
            await websocket.send(json.dumps(response))
            print(f"Sent response to client: {response}")
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")
            break

start_server = websockets.serve(server_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
