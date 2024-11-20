# reduce
from functools import reduce
def add(x,y):
    return x + y

# print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
    return x * 10 + y

print(reduce(fn,[1, 3, 5, 7, 9]))