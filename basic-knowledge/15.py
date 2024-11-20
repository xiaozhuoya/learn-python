# isinstance
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
  

print(not isinstance(1,(int)))


print(my_abs('1'))