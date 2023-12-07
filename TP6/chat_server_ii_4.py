import asyncio

global CLIENTS
CLIENTS = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Received connection from {addr}")

    if addr not in CLIENTS:
        CLIENTS[addr] = {"r": reader, "w": writer}
        print(f"Client {addr} connected")

        writer.write(f"Hello {addr[0]}:{addr[1]}".encode())
        await writer.drain()
    else:
        print(f"Client {addr} is already connected. Ignoring.")

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break

            message = data.decode()
            print(f"Message received from {addr[0]}:{addr[1]} : {message}")

            for client_addr, client_info in CLIENTS.items():
                if client_addr != addr:
                    client_info["w"].write(f"{addr[0]}:{addr[1]} said: {message}".encode())
                    await client_info["w"].drain()

    except asyncio.CancelledError:
        pass
    finally:
        print(f"Closing connection from {addr}")
        del CLIENTS[addr]
        writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8889)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
