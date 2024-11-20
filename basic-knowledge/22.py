# 列表生成式
L = []
for x in range(1,11):
    L.append(x * x)
print(L)

[x * x for x in range(1,11)]

print([x * x for x in range(1,11)])

[x * x for x in range(1,11) if x % 2 == 0]

B = [m + n for m in 'ABC' for n in 'XYZ']
print(B)

# 导入os模块
import os
C = [d for d in os.listdir('.')]
print(C,'C')

e = {'x': 'A', 'y': 'B', 'z': 'C' }
for key,value in e.items():
    print(key,'=',value)
f = {'x': 'A', 'y': 'B', 'z': 'C' }
g = [k + '=' + v for k,v in f.items()]
print(g,'g')

[x if x % 2 == 0 else -x for x in range(1, 11)]
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# list中所有的字符串变成小写
T = ['Hello', 'World', 18, 'Apple', None]
S = [s.lower() for s in T if isinstance(s, str)]
print(S)