# 定制类

class Student(object):
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

print(Student('xz'))
Student('xz')


# __iter__

class Fib(object):

    def __init__(self):
      self.a, self.b = 0,1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    
# for n in Fib():
#     print(n)


# print(Fib()[5])


# __getitem__

class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

print(Fib1()[5])

f = Fib1()

print(f[0:5])


