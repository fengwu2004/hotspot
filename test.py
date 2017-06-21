import asyncio
import time
import aiohttp
from concurrent.futures.thread import ThreadPoolExecutor

executor = ThreadPoolExecutor()

now = lambda : time.time()

async def hello():
    
    await fun()
    
    await asyncio.sleep(5)
    
    for n in range(100):
        
        print('kdkdkd')
        
async def fun():

    await asyncio.sleep(10)
    
    for n in range(12):
        
        print('funfu')
        
start = now()

asyncio.get_event_loop().run_until_complete(hello())

print('TIME: ', now() - start)