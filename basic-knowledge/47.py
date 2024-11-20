# 面向对象高级编程  9*9

class Student(object):
    pass

def nine_nine():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j} x {i} = {i * j}", end="\t")
        print()

nine_nine()