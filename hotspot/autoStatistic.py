import time
from pymongo import MongoClient
from hotspot.RequestBaseManager import RequestBaseManager

def getTimeOfTwoWeekago():
    
    result = time.strftime("%U %w %Y", time.gmtime())
    
    result = result.split(' ')
    
    year = int(result[2])
    
    week = int(result[0]) - 2
    
    if week < 0:
        
        year -= 1

        week += 53
    
    day = 0
    
    thattime = "%d %d %d" % (week, day, year)
    
    start = time.mktime(time.strptime(thattime, "%U %w %Y"))
    
    week = int(result[0])
    
    day = 0
    
    thattime = "%d %d %d" % (week + 1, day, year)
    
    end = time.mktime(time.strptime(thattime, "%U %w %Y"))
    
    return [start, end]

def getSecondaryIndustryList():
    
    client = MongoClient('localhost', 27017)
    
    db = client["hotspot"]
    
    coll = db['adminInfo']
    
    result = coll.find({})
    
    secondary = []
    
    for r in result:
        
        secondary = r['industry']['secondary']
        
        break
        
    return secondary

def getTwoWeekSecondaryStatus(secondaryList):
    
    client = MongoClient('localhost', 27017)
    
    db = client["hotspot"]
    
    coll = db['spot']
    
    timeinterval = getTimeOfTwoWeekago()
    
    autoResult = []
    
    for industrayName in secondaryList:
        
        finished = coll.find({'secondary': industrayName, 'finish': 'yes',
                              'createTime': {'$gte': timeinterval[0], '$lte': timeinterval[1]}}).count()
        
        unfinished = coll.find({'secondary': industrayName, 'finish': 'no',
                                'createTime': {'$gte': timeinterval[0], '$lte': timeinterval[1]}}).count()
        
        if finished == 0 and unfinished == 0:
            continue
            
        result = dict()
        
        result['name'] = industrayName
        
        result['finished'] = finished
        
        result['unfinished'] = unfinished
        
        autoResult.append(result)
        
    return autoResult

class AutoStatisticManager(RequestBaseManager):
    
    def post(self, *args, **kwargs):
        
        secondaryList = getSecondaryIndustryList()
        
        if len(secondaryList) == 0:
            
            self.write({'success': 0})
            
            return
        
        result = getTwoWeekSecondaryStatus(secondaryList)
        
        if len(result) == 0:
            
            self.write({'success': 0})
            
            return
        
        self.write({'success': 1, 'data':result})

