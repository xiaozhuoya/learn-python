# 迭代

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,'&',value)

for c in 'ABC':
    print(c)

# 是否可以迭代
from collections.abc import Iterable

print(isinstance(123, Iterable))

# 下标
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 两个循环
for x,y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)