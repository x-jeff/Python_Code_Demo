li=[1,2,3,4,5,6,7,8]
print(len(li))
print(li[0])
print(li[-1])
print(li[0:3])

li.sort(reverse=False)
print(li)
li.sort(reverse=True)
print(li)

#li.append(9)
#li.extend([9,10])
#li.insert(0,"hello")

#li.pop()
#li.remove(1)
#del li[0]

#li[0]="hello"
#print(li)

tu=(1,2,3)

a=1
b=2
print(a,b)
a,b=b,a
print(a,b)

dic={'a':1,'b':0.2,'c':'hello'}
print(dic['b'])
#print(dic['d'])

print(dic.get('b'))
print(dic.get('d'))

print(dic.get('b','default'))
print(dic.get('d','default'))
print(dic.get('b',0.3))
print(dic.get('d',0.3))

dic['d']=100
print(dic)

print(dic.keys())
print(dic.values())

for key in dic.keys():
#for key in dic:
    print(key)

for n in dic:
    print(n,dic.get(n))
    #print(n,dic[n])

print('hello')
print("hello")
print('''hello''')

print('hell\'o')
print("hell'o")

print("hell\"o")
print('hell"o')

print('''hell'o , worl"d''')