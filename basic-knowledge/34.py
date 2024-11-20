# 装饰器

def now():
    print('2024-11-7')

f = now

f()

print(now.__name__)

def log(func):
    def wrapper(*args,**kw):
        print('call %s():'% func._name_)
        return func(*args,**kw)
    return wrapper

@log
def now1():
    print('2024-6-1')