import asyncio

CLIENTS = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')

    if addr not in CLIENTS:
        data = await reader.read(1024)
        message = data.decode()
        if message.startswith("Hello|"):
            pseudo = message.split("|")[1]
            print(f"\033[92mAnnonce\033[0m : {pseudo} a rejoint la chatroom")
            CLIENTS[addr] = {}
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["w"] = writer
            CLIENTS[addr]["pseudo"] = pseudo

            announcement = (f"\033[92mAnnonce\033[0m : {pseudo} a rejoint la chatroom")
            for client_addr, client_data in CLIENTS.items():
                if client_addr != addr:
                    client_data["w"].write(announcement.encode())
                    await client_data["w"].drain()

    while True:
        data = await reader.read(1024)
        if not data:
            break

        message = data.decode()
        print(f"\033[94mMessage\033[0m reçu de {pseudo} : {message}")
        for client_addr, client_data in CLIENTS.items():
            if client_addr != addr:
                pseudo = client_data["pseudo"]
                response_message = f"{pseudo} a dit : {message}"
                client_data["w"].write(response_message.encode())
                await client_data["w"].drain()

    print(f"\033[91mClient déconnecté :\033[0m {addr}")
    del CLIENTS[addr]

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8889)

    addr = server.sockets[0].getsockname()
    print(f'Serveur en attente de connexions sur {addr}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
