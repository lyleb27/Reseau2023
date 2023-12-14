import asyncio

host = '127.0.0.1'
port = 8889
global CLIENTS
CLIENTS = {}


async def handle_client_msg(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"New client: {addr[0]}:{addr[1]}")

    data = await reader.read(1)  # Read the first byte to determine the message type
    msg_type = int(data[0])
    print(f"Received message type: {msg_type}")

    if msg_type == 1:  # Short message
        size_data = await reader.read(2)  # Read the next 2 bytes for the message size
        message_size = int.from_bytes(size_data, byteorder='big')
        print(f"Short message size: {message_size}")

        message = await reader.read(message_size)  # Read the message
        print(f"Received message: {message}")
    elif msg_type == 2:  # Long message
        header_size_data = await reader.read(1)  # Read 1 byte for the header size
        header_size = int.from_bytes(header_size_data, byteorder='big')
        print(f"Long message header size: {header_size}")

        size_data = await reader.read(header_size)  # Read the header
        message_size = int.from_bytes(size_data, byteorder='big')
        print(f"Long message size: {message_size}")

        message = await reader.read(message_size)  # Read the message
        print(f"Received message: {message}")
        
async def announce(announcement):
    for client_addr, client_info in CLIENTS.items():
        announcement_bytes = announcement.encode()
        msg_type = 1  
        pseudo_len_data = len("Announcement").to_bytes(1, byteorder='big') 
        announcement_len_data = len(announcement).to_bytes(2, byteorder='big')  
        client_info["w"].write(msg_type.to_bytes(1, byteorder='big') + pseudo_len_data + "Announcement".encode() + announcement_len_data + announcement_bytes)
        await client_info["w"].drain()


async def main():
    server = await asyncio.start_server(handle_client_msg, host, port)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
