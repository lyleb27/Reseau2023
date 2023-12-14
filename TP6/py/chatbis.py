import asyncio
import aioconsole

async def send_message(writer, message):
    writer.write(message.encode())
    await writer.drain()

async def user_input(writer):
    while True:
        message = await aioconsole.ainput("")
        writer.write(message.encode())
        await writer.drain()

async def receive_messages(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        print(data.decode())

async def main():
    try:
        reader, writer = await asyncio.open_connection(host="127.0.0.1", port=8889)

        pseudo = input("Choisissez votre pseudo : ")
        await send_message(writer, f"Hello|{pseudo}")

        input_task = asyncio.create_task(user_input(writer))
        receive_task = asyncio.create_task(receive_messages(reader))

        await asyncio.gather(input_task, receive_task, return_exceptions=True)
    except asyncio.CancelledError:
        pass

if __name__ == '__main__':
    asyncio.run(main())
