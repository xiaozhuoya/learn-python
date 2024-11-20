# 找出100以内的回数

def is_palindrome(n):
    return  str(n) == str(n)[::-1]

output = list(filter(is_palindrome, range(1, 100))) 
print('1~100:',output)

