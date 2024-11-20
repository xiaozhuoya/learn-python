# slots 定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'xiaozhuo'
s.age = 25
# s.score = 66

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
print(g.score)