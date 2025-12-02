import asyncio
import time


async def fetch_data_async():
    print("Fetching data ...")
    await asyncio.sleep(4)


loop = asyncio.new_event_loop()

tasks = [
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async()),
    loop.create_task(fetch_data_async())
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()