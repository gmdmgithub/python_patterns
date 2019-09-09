import asyncio

async def coroutine_future(future):
    await asyncio.sleep(3)

    future.set_result('My results from future')

async def my_func():
    #first define future object
    future = asyncio.Future()

    # wait for the completion of 
    # coroutine that turned into a future object 
    # using the ensure_future() function
    await asyncio.ensure_future(coroutine_future(future))

    # see the result
    print(future.result())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(my_func())
    finally:
        loop.close()