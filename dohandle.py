import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.gen
import os
from hotspot.RequestBaseManager import RequestBaseManager

class SleepHandler(RequestBaseManager):
    
    @tornado.gen.coroutine
    def ping (self, url):
        
        os.system("ping -c 2 {}".format(url))
        
        return 'after'
    
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        
        response = yield tornado.gen.Task(self.ping, ' www.google.com')
        
        print('response', response)
        
        self.write("Sleep")
        
class JustNowHandler(RequestBaseManager):
    
    def get(self, *args, **kwargs):
        
        self.write("JustNow")

def make_app():
    return tornado.web.Application([
        (r"/sleep", SleepHandler),
        (r"/just", JustNowHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

# async def hello_world():
#
#     time.sleep(10)
#
#     print("Hello World!")
#
# async def callCoroutine():
#
#     await hello_world()
#
# loop = asyncio.get_event_loop()
#
# re = callCoroutine()
#
# print(time.time())
#
# # loop.run_until_complete(callCoroutine())
#
# def dis():
#
#     print('ok')
#
# print(time.time())
    

