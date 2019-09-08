import asyncio
import random

async def perform_coroutines(id):
    
    #define random time consumer to emulate performing long task
    time_consumer = random.randint(1,7)
    
    #await will wait until this task is finished
    await asyncio.sleep(time_consumer)
    print(f'Coroutine did some hard task! id: {id} and took {time_consumer} seconds')

async def main_func():
    my_tasks = []
    # lets simulate some multiple tasks
    for id in range(15):
        my_tasks.append(asyncio.ensure_future(perform_coroutines(id)))

    await asyncio.gather(*my_tasks)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main_func())
finally:
    loop.close()
