# 
class Student():
    pass

s = Student()
s.name = 'xiaozhuo'
print(s.name)

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)

print(s.age)

s2 = Student()
# s2.set_age(25)

def set_score(self,score):
    self.score = score

Student.set_score = set_score

s.set_score(100)

print(s.score)

s2.set_score(99)

print(s2.score)