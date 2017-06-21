import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

executor = ThreadPoolExecutor()

async def fun1():

    print('fun1---')

    await asyncio.sleep(10)
    
    await subFun()
    
async def subFun():
    
    def fun():
    
        for i in range(10):
            
            print('abcd')
            
        return 'subFun'
        
    fun()

async def fun2():

    print('fun2')
    
    await subFun2()

async def subFun2():
    
    for i in range(10):
        
        print('-+-+')
        
    return 'UIOP'


f = fun1()
# asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

# v = fun1()

# if asyncio.iscoroutinefunction(v):
#
#     print('+')
#
# else:
#
#     print('-')

async def divide(x, y):
    
    print('go')
    
    return x / y

def bad_call():
    # This should raise a ZeroDivisionError, but it won't because
    # the coroutine is called incorrectly.
    divide(1, 0)
    
f = divide(1, 0)