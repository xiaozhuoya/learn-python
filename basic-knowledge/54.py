# 定制类 __getattr__

class Student(object):
    def __init__(self):
      self.name = 'xz'

    def __getattr__(self, attr):
        if attr == 'score':
           return 999
        
        if attr=='age':
            return lambda: 25
        
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
        
        

s = Student()

print(s.name)
print(s.score)

print(s.age())


class Chain(object):
    def __init__(self,path=''):
        self._path = path

    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path, path))
    
    def __str__(self):
        return self._path
    
    __repr__ = __str__


print(Chain().status.user.timeline.list)

# __call__

class Student(object):

    def __init__(self,name):
        self.name = name
    
    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('xz')
print(s())


print(callable(Student()))
print(callable('123'))
