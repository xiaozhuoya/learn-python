# 错误处理

def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r ==(-1):
        print('Error')
    else:
        pass
