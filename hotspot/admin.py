from pymongo import MongoClient
import tornado.web
from hotspot.RequestBaseManager import RequestBaseManager

class SpotAdminInfo(RequestBaseManager):
    
    def post(self, *args, **kwargs):
        
        client = MongoClient('localhost', 27017)
    
        db = client["hotspot"]
    
        coll = db['adminInfo']
        
        result = coll.find({})
        
        industry = None
        
        for v in result:
            
            industry = v['industry']
            
            break
            
        coll = db['users']
        
        users = coll.find({})
        
        creators = []
        
        for u in users:
            
            creators.append(u['name'])
            
        
        if industry == None:
            
            self.write({'success':0})
            
        else:
    
            self.write({'industry':industry, 'creators':creators})
        