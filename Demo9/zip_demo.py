a=[1,2,3]
b=[4,5,6]
c=[4,5,6,7,8]
zipped1=zip(a,b)
print(list(zipped1))
zipped2=zip(a,c)
print(list(zipped2))
d1,d2=zip(*zip(a,b))
# d1,d2=zip(*zipped1) #error
print(list(d1))
print(list(d2))
listA=[a for a in range(1,5)]
print(listA)