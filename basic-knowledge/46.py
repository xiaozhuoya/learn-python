# 实例属性和类属性
# class Student(object):
#     def __init__(self,name):
#         self.name = name
    
# s = Student('Bob')
# s.score = 90


class Student(object):
    name = 'Student'
    
s = Student()
# print(s.name)

s.name = 'xiaozhuo'

print(s.name)
print(Student.name)
del s.name
print(s.name)


class Teacher(object):
    count = 0
    
    def __init__(self, name):
      self.name = name
      Teacher.count += 1

# 测试:
if Teacher.count != 0:
    print('测试失败!')
else:
    bart = Teacher('Bart')
    if Teacher.count != 1:
        print('测试失败!')
    else:
        lisa = Teacher('Bart')
        if Teacher.count != 2:
            print('测试失败!')
        else:
            print('Students:', Teacher.count)
            print('测试通过!')
        