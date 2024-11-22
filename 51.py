# 使用@property

class Student(object):
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.score = 60
print(s.score)
s.score = 200

# 只定义getter方法，不定义setter方法就是一个只读属性

class Teacher(object):
    def __init__(self, birth=None):
        self._birth = birth
        
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth