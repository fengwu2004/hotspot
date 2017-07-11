import json
import tornado.escape
from pymongo import MongoClient
import time
import tornado.web
from hotspot.RequestBaseManager import RequestBaseManager

class SpotCreateManager(RequestBaseManager):
    
    def post(self):
        
        print(self.cookies)
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        spotInfo = data

        client = MongoClient('localhost', 27017)

        db = client["hotspot"]

        table = db['spot']

        spotInfo['createTime'] = time.time()
        
        table.insert_one(spotInfo)
        
        self.write({'success':1})