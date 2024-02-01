import asyncio
import websockets
import redis.asyncio as redis

class WebSocketServer:
    def __init__(self, redis_host, redis_port):
        self.clients = set()
        self.redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    async def handle_client(self, websocket, path):
        self.clients.add(websocket)
        print(f"Nouveau client connecté. Nombre total de clients : {len(self.clients)}")

        try:
            await self.redis_client.set(f'client:{id(websocket)}', 'connected')

            async for message in websocket:
                print(f"Message reçu : {message}")

                if message == 'exit':
                    await self.redis_client.delete(f'client:{id(websocket)}')
                    break

                for client in self.clients:
                    try:
                        await client.send(message)
                    except websockets.exceptions.ConnectionClosedError:
                        pass
        except websockets.exceptions.ConnectionClosedError:
            pass
        finally:
            self.clients.remove(websocket)
            print(f"Client déconnecté. Nombre total de clients : {len(self.clients)}")

    async def start_server(self, host, port):
        start_server = websockets.serve(self.handle_client, host, port)
        await start_server

if __name__ == "__main__":
    redis_host = "10.33.76.7"
    redis_port = 6379
    server = WebSocketServer(redis_host, redis_port)

    asyncio.get_event_loop().run_until_complete(server.start_server("localhost", 8765))
    asyncio.get_event_loop().run_forever()
