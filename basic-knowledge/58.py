# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

def fn(self,name = 'world'):
    print('Hello,%s.'% name)
# create Hello class
Hello = type('Hello',(object,),dict(hello=fn)) 
h = Hello()
h.hello()
print(type(Hello))
print(type(h))