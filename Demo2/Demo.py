a=[1,2,3,4,5,6,7,8]
for i in a :
    print(i)
for i in a :
    if i % 2 == 0 :
        print(i)
for i in a:
    print(i)
print("end")
for i in a:
    print(i)
    print("end")
b=15
if b==12:
    print("b=12")
elif b<12:
    print("b<12")
elif b>12 and b<20:
    print("12<b<20")
else :
    print("b>=20")

def addNum(a,b):
    return a+b
print(addNum(2,3))

def square(x):
    return x*x
print(square(3))

addNum1=lambda a,b:a+b
print(addNum1(3,4))

square1=lambda x:x**3
print(square1(3))

a=3.2
import math
b=math.ceil(a)
print(b)

import numpy
numpy.random.normal(25,5,10)