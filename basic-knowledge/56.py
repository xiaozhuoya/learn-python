# 把Student的gender属性改造为枚举类型，可以避免使用字符串：

from enum import Enum,unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):

    def __init__(self, name, gender):
      self.name = name
      self.gender = gender

      if not isinstance(gender, Gender):
            raise ValueError("Invalid gender. Expected a Gender enum value.")

# test
bart = Student('Bart',Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过！')
else:
    print('测试失败！')

