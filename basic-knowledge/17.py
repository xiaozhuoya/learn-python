# def 计算x的n次方

def power(x):
    return x * x
print(power(6))


def power1(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power1(5,2))