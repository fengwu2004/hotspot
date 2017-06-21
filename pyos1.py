class Task(object):

    taskid = 0
    
    def __init__(self, target):
    
        Task.taskid += 1
        
        self.tid = Task.taskid
        
        self.target = target
        
        self.sendval = None
        
    def run(self):
    
        return self.target.send(self.sendval)
    
    
def foo():

    print('Part 1')
    
    yield
    
    print('Part 2')
    
    yield
    
t1 = Task(foo())

t1.run()

t1.run()