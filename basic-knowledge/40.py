# class
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def get_name(self):
        return self.__name
    
    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


print(Student('xz',90).get_name())

a = Student('xz',90)
a.set_score(66)

print(a.get_score())

