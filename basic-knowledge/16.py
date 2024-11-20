#  
import math

def quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return '没有实数解'
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(b**2 -4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 -4*a*c))/(2*a)
        return x1, x2
    
print(quadratic(2, 3, 1))
