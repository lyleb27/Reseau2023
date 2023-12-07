import asyncio
import aioconsole

async def user_input(writer):
    while True:
        message = await aioconsole.ainput("Enter your message: ")
        writer.write(message.encode())
        await writer.drain()

async def receive_messages(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            break
async def main():
    try:
        reader, writer = await asyncio.open_connection(host="127.0.0.1", port=8889)

        input_task = asyncio.create_task(user_input(writer))
        receive_task = asyncio.create_task(receive_messages(reader))

        await asyncio.gather(input_task, receive_task, return_exceptions=True)
    except asyncio.CancelledError:
        pass

if __name__ == '__main__':
    asyncio.run(main())
