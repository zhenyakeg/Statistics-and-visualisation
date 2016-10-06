__author__ = 'student'
import random
import math
def f (x):
    if x<=15 and x>=10:
        return math.sin(x**2+4)
    else:
        return 0

def integrate(min,max,n):
    s1 = 0
    s2 = 0
    random.seed()
    i=0
    while min+i/n<=max :
        s1+=f(min+i/n)/n
        s2+=f(min+(i+1)/n)/n
        i+=1
    return (s1+s2)/2
print(integrate(-3,20,10000))