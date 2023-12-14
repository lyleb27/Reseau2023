import asyncio

async def count_and_sleep1():
    for i in range(11):
        print(i)
        await asyncio.sleep(0.5)

async def count_and_sleep2():
    for i in range(11):
        print(i)
        await asyncio.sleep(0.5)

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(count_and_sleep1()),
    loop.create_task(count_and_sleep2()),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()

