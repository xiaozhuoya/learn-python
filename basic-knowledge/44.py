# 
class MyDog(object):
    def __len__(self):
        return 100
    
dog = MyDog()
len(dog) # 100


print(len(dog('200')))
