import asyncio

async def sampleCoroutine():
    print("Here is Coroutine!")

def trivial_example():
    
    # First define an instance of an ### event loop ###
    event_loop = asyncio.get_event_loop()
    
    # Tell this event loop to run until all the tasks assigned
    # to it are complete. In this example just the execution of
    # sampleCoroutine() coroutine
    event_loop.run_until_complete(sampleCoroutine())
    
    # Tidying up our loop by calling close()
    event_loop.close()

#TODO!! how to define Coroutines - two ways
# 1 ### with async key word (from python 3.5)
async def async_way_func():
    pass
# 2 with decorator (from python 3.4)
@asyncio.coroutine
def decoarot_way_func():
    pass



if __name__ == '__main__':
    trivial_example()