import asyncio

import time

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(do_some_work(1)),
    asyncio.ensure_future(do_some_work(2)),
    asyncio.ensure_future(do_some_work(4))
]

asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

print('TIME: ', now() - start)