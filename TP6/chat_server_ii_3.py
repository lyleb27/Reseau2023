import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Received connection from {addr}")

    writer.write(f"Hello {addr[0]}:{addr[1]}".encode())
    await writer.drain()

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            message = data.decode()
            print(f"Message received from {addr[0]}:{addr[1]}: {message}")
    except asyncio.CancelledError:
        pass
    finally:
        print(f"Closing connection from {addr}")
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
