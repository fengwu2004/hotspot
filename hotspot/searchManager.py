import json
import sys
from pymongo import MongoClient
from hotspot.RequestBaseManager import RequestBaseManager

class SearchManager(RequestBaseManager):

    def post(self):
    
        keywords = json.loads(self.request.body.decode('utf-8'))
        
        client = MongoClient('localhost', 27017)
        
        db = client["hotspot"]
        
        table = db['spot']
        
        searchkeywords = dict()

        searchkeywords['top'] = keywords['top']

        searchkeywords['secondary'] = keywords['secondary']

        searchkeywords['affiliate'] = {'company':keywords['affiliate'], 'stocktype':keywords['stocktype']}

        searchkeywords['creator'] = keywords['creator']

        if keywords['finish'] != 'other':
            
            searchkeywords['finish'] = keywords['finish']

        results = table.find(searchkeywords, {'_id':0})
        
        starttime = 0

        endtime = sys.maxsize
        
        temps = []
        
        if keywords['timeInterval']['start'] != '':
            
            starttime = int(keywords['timeInterval']['start'])

        if keywords['timeInterval']['end'] != '':
            
            endtime = int(keywords['timeInterval']['end'])
        
        for r in results:
            
            if starttime <= int(r['createTime']) <= endtime:
        
                temps.append(r)
                
        self.write({'success':1, 'data':temps})