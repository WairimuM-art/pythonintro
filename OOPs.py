class Employee:
    count=0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.count += 1 # non-parameterized constructor
    def display(self):
        print("Name:%s Age:%d" %(self.name,self.age))
emp1 = Employee("John", 25)
emp2 = Employee("Jane", 28)
emp3 = Employee("Aliya", 21)
print("LIST OF EMPLOYEES AND THEIR AGES")
print(emp1.name,emp1.age)
print(emp2.name,emp2.age)
print(emp3.name,emp3.age)
print("TOTAL NUMBER OF EMPLOYEES:") # non-parametrized constructor
print(Employee.count)
print("The first employee's name is" +emp1.name)
print("The second employee's name is" +emp2.name)
print("The third employee's name is" +emp3.name)
print(getattr(emp1,'name'))
print(getattr(emp1,'age'))
setattr(emp1,"age",26)
print(getattr(emp1,'age'))
delattr(emp1,'age')
#print(getattr(emp1,'age'))
print(Employee.__doc__)
print(Employee.__dict__)
print(Employee.__module__)



