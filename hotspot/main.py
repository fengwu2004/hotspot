import tornado.escape
import tornado.ioloop
import tornado.web
from hotspot.create import SpotCreateManager
from hotspot.loginManager import loginManager
from hotspot.usercheck import UserManager
from hotspot.admin import SpotAdminInfo
from hotspot.searchManager import SearchManager
        

def make_app():
    
    return tornado.web.Application([
        
        (r"/login", loginManager),
        (r"/create", SpotCreateManager),
        (r"/user", UserManager),
        (r"/spotinfo", SpotAdminInfo),
        (r"/search", SearchManager),
    ])

if __name__ == "__main__":
    
    app = make_app()
    
    app.listen(8888)
    
    tornado.ioloop.IOLoop.current().start()