import operator
students=[('john','A',15),('jane','B',12),('dave','B',10)]
single_stu=('john','A',15)
b=operator.itemgetter(2)
b(students)
b(single_stu)
print(b(students))
print(b(single_stu))
c=operator.itemgetter(2,1)
c(students)
c(single_stu)
print(c(students))
print(c(single_stu))
sorted(students,key=operator.itemgetter(2))
print(sorted(students,key=operator.itemgetter(2)))
print(sorted(students,key=operator.itemgetter(2),reverse=True))
sorted(students,key=lambda x:x[2])
print(sorted(students,key=lambda x:x[2]))