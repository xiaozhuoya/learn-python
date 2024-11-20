# class 继承
class Animal():
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()
cat = Cat()
cat.run()


a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
isinstance(a, list) # True
isinstance(c, Dog)  # True
isinstance(c, Animal) # True

b = Animal()
isinstance(b, Dog) # False

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

run_twice(Dog())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())