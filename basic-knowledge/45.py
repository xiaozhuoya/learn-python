# 

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))

hasattr(obj, 'y') # false

setattr(obj, 'y', 19)
hasattr(obj, 'y') # true
getattr(obj, 'y')

getattr(obj, 'z', 404)

hasattr(obj, 'power')

fn = obj.power

print(fn())