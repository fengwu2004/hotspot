import tornado.web

class loginManager(tornado.web.RequestHandler):
    
    def post(self):
    
        self.set_header('Content-Type', 'application/json')
        
        self.write('no')