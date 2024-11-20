# 偏函数

def int2(x, base=2):
    return int(x, base)

print(int2('101'))

import functools
int2 =  functools.partial(int,base=2)

print(int2('100'))