# 生成器
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(next(g))

for n in g:
    print(n)

# Fibonacci

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b
        a,b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))

for n in fib(6):
    print(n,'n')

g2 = fib(6)
while True:
    try:
        x = next(g2)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
