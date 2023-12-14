import asyncio
import aioconsole

async def send_message(writer, message_type, content):
    formatted_msg = f"{message_type}|{len(content)}|{content}"
    size_data = len(formatted_msg).to_bytes(1, byteorder='big')
    writer.write(message_type.to_bytes(1, byteorder='big') + size_data + formatted_msg.encode())
    await writer.drain()



async def user_input(writer):
    while True:
        message = await aioconsole.ainput("")
        await send_message(writer, 1, message) 

async def receive_messages(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        print(f"Received raw data: {data}")
        msg_type = int(data[0])
        print(f"Received message type: {msg_type}")

        if msg_type == 1:  # Short message
            size_data = int.from_bytes(data[1:3], byteorder='big')
            message = data[3:].decode()
        elif msg_type == 2:  # Long message
            header_size = int.from_bytes(data[1:2], byteorder='big')
            size_data = int.from_bytes(data[2:2+header_size], byteorder='big')
            message = data[2+header_size:].decode()

        print(f"Received message size: {size_data}")
        print(f"Received message content: {message}")


async def main():
    try:
        reader, writer = await asyncio.open_connection(host="127.0.0.1", port=8889)

        pseudo = input("Choisissez votre pseudo : ")
        await send_message(writer, 1, f"Hello|{pseudo}") 

        input_task = asyncio.create_task(user_input(writer))
        receive_task = asyncio.create_task(receive_messages(reader))

        await asyncio.gather(input_task, receive_task, return_exceptions=True)
    except asyncio.CancelledError:
        pass

if __name__ == '__main__':
    asyncio.run(main())
