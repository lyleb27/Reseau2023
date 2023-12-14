import asyncio
import websockets

CLIENTS = set()

async def handle_client(websocket, path):
    CLIENTS.add(websocket)
    print(f"Nouveau client connecté. Nombre total de clients : {len(CLIENTS)}")

    try:
        async for message in websocket:
            print(f"Message reçu : {message}")
            for client in CLIENTS:
                try:
                    await client.send(message)
                except websockets.exceptions.ConnectionClosedError:
                    pass
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        CLIENTS.remove(websocket)
        print(f"Client déconnecté. Nombre total de clients : {len(CLIENTS)}")

start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
