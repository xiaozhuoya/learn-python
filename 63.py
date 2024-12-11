# debug 调试

# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n

# def main():
#     foo('2')

# main()

# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()