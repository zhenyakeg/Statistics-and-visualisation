__author__ = 'student'
import random
import math
def f (x):
    if x<=2 and x>=-2:
        return math.sin(x**2+4)
    else:
        return 0

def integrate(min,max,n):
    s=0
    random.seed()
    for i in range (n) :
        s+=f(random.uniform(min,max))
    return ((max-min)/n)*s
print(integrate(-3,3,1000000))
