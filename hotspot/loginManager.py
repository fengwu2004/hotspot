from hotspot.tokenManager import TokenManagerInstance
from hotspot.usercheck import UserManager
from hotspot.RequestBaseManager import RequestBaseManager
import json
from pymongo import MongoClient

class loginManager(RequestBaseManager):
    
    def options(self, *args, **kwargs):
        
        self.set_status(204)
        
        self.finish()
    
    def checkCorrect(self, name, pwd):
        
        client = MongoClient('localhost', 27017)
        
        db = client["hotspot"]
        
        coll = db['users']
        
        user = coll.find({'name': name})
        
        for u in user:
            
            if u['pwd'] == pwd:
                
                return True
        
        return False
    
    def post(self):
        
        print(self.count)
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        username = data['name']
        
        password = data['pwd']
        
        if self.checkCorrect(username, password):
            
            data = {}
            
            data['success'] = 1
            
            data['data'] = {}
            
            data['data']['url'] = 'http://192.168.1.58/spot/main.html'
            
            data['token'] = TokenManagerInstance().createToken(username)
            
            self.write(data)
            
            return
        
        self.write({'success': '0'})