import json

import tornado.web

from hotspot.tokenManager import TokenManagerInstance

from hotspot.RequestBaseManager import RequestBaseManager


class UserManager(RequestBaseManager):
    
    def post(self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))

        result = {}
        
        if self.checkValid(data):
    
            self.write({'success': '1'})
        
        else:
    
            self.write({'success': '0'})
    
    def checkValid(self, data):
    
        user = data['user']
        
        token = data['token']
        
        return TokenManagerInstance().checkToken(token, user)
    
    