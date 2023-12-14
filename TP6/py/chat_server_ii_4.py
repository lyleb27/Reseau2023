import asyncio

CLIENTS = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')  

    if addr not in CLIENTS:
        print(f"Nouveau client connecté: {addr}") 
        CLIENTS[addr] = {}
        CLIENTS[addr]["r"] = reader
        CLIENTS[addr]["w"] = writer

    while True:
        data = await reader.read(1024) 
        if not data:
            break

        message = data.decode()
        print(f"Message reçu de {addr}: {message}")

        # Envoi du message à tous les clients sauf celui qui l'a envoyé
        for client_addr, client_data in CLIENTS.items():
            if client_addr != addr:
                ip, port = client_addr
                response_message = f"{ip}:{port} a dit : {message}"
                client_data["w"].write(response_message.encode())
                await client_data["w"].drain()

    print(f"Client déconnecté: {addr}")
    del CLIENTS[addr]

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8889)

    addr = server.sockets[0].getsockname()
    print(f'Serveur en attente de connexions sur {addr}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
