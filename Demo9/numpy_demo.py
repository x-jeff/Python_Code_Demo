import numpy as np
a=[1,2,3]
b=[2,3,4]
#print(a*b) #error
for k,v in zip(a,b):
    print(k*v)
for k,v in zip(a,b):
    print(k,v)
c=[k*v for k,v in zip(a,b)]
print(c)

import numpy as np
a=np.array([1,2,3])
b=np.array([2,3,4])
print(a+b)
print(a*b)