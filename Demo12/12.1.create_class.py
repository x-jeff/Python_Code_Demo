class Employee:
    'class information'
    empCnt=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCnt+=1
        #self.empCnt=1

    def displayCnt(self):
        print("Total Employee %d" % Employee.empCnt)

    def displayEmp(self):
        print("Name : ",self.name," , Salary : ",self.salary)

print(Employee.__doc__)

#创建Employee类的第一个对象
emp1=Employee("Zara",2000)
#创建Employee类的第二个对象
emp2=Employee("Manni",5000)

print(emp1.empCnt)
print(emp2.empCnt)

emp1.displayEmp()
emp2.displayEmp()
#emp2.displayCnt()
print("Total Employee %d " % Employee.empCnt)

emp1.age=7
emp1.age=8
print(emp1.age)
#print(emp2.age)
del emp1.age

setattr(emp2,'age',10)
getattr(emp2,'age')
print(getattr(emp2,'age'))
hasattr(emp2,'age')
print(hasattr(emp2,'age'))
delattr(emp2,'age')

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
