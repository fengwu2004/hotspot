import tornado.web

class RequestBaseManager(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        
        print('set_default_headers')
        
        self.set_header("Access-Control-Allow-Origin", "*")
        
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')