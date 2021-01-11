import math
import random as rd


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

x = fib(17)
print(math.sqrt(144), '', x)
a=rd.random()
b=rd.randint(1,100)
c=rd.uniform(1,100)
numbers= [1,2,3,4,5,6,7,8,9]
d=rd.choice(numbers)
e=rd.sample(numbers,6)
print(a)
print(b)
print(c)
print(d)
print(e)
name=input('Please enter your name ')
print('Hello', name)

