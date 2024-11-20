# 
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('xz',16,a=2,b=3,c=5))
# print(person('xz',16))


def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

# 只接受city, job
def person3(name, age, *, city, job):
    print(name, age, city, job)

person3('Jack', 24, city='Beijing', job='Engineer')


# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person4('Jack', 24, job='Engineer')

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。