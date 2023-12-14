import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Received connection from {addr}")

    # Send a greeting to the client
    writer.write(f"Hello {addr[0]}:{addr[1]}".encode())
    await writer.drain()

    # Wait for data from the client
    data = await reader.read(100)
    message = data.decode()
    print(f"Received message from {addr}: {message}")

    # Respond to the client
    response = f"Received your message: {message}"
    writer.write(response.encode())
    await writer.drain()

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
