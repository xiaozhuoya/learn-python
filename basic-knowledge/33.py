# 匿名函数

L = list(map(lambda x: x * x,[1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)

f = lambda x: x * x
print(f(6),6)

def f(x):
    return x * x

result = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(result)

# 
L1 = list(filter(lambda n:n % 2 == 1, range(1, 20)))
print(L1)

