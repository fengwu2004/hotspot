def getLines():

    lines = [line.rstrip('\n') for line in open('top.txt')]

    return lines

def saveToDB(lines):
    
    f = open('topadd.txt', 'w')
    
    r = set()

    for line in lines:
        
        r.add(line)
        
    for v in r:
        
        f.write("'" + v + "',")
        
saveToDB(getLines())
    
    

