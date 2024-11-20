# 获取对象信息

type(123) # <class 'int'>

type('123') # <class 'str'>

import types

def fn():
    pass

type(fn) == types.FunctionType

type(abs) == types.BuiltinFunctionType

type(lambda x: x) == types.LambdaType

type((x for x in range(10))) == types.GeneratorType

#  a = Animal()
#  d = Dog()
#  h = Husky()

isinstance('a', str)

isinstance(b'a', bytes)

print(dir('ABC'))

len('ABC') 
# 等价于下面代码
'ABC'.__len__()
