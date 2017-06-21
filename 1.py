import tornado.ioloop
import tornado.web
import time
import tornado.concurrent
from tornado import gen
from concurrent import futures
from concurrent.futures.thread import ThreadPoolExecutor
import asyncio
import aiohttp

executor = ThreadPoolExecutor()

loop = asyncio.get_event_loop()


class MainHandle(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        yield self.asyFun()
    
    def asyFun(self):
        def send(f):
            self.set_header('Content-Type', 'application/json')
            
            self.write(f.result())
        
        def onAs():
            val = dict()
            
            val['name'] = 'yanli'
            
            val['age'] = 10
            
            for i in range(1000000):
                print('abcdefghijklmndfhrnffnfjj')
            
            print('||||||||||||||||||||')
            
            return val
        
        fu = executor.submit(onAs)
        
        fu.add_done_callback(send)
        
        return fu
    
    def get(self):
        print('get')
        
        # for i in range(1000000):
        #
        #     print('----------')
        
        self.write('hello world!!!')


def make_app():
    return tornado.web.Application([(r"/", MainHandle), ])


if __name__ == '__main__':
    app = make_app()
    
    app.listen(8888)
    
    tornado.ioloop.IOLoop.current().start()