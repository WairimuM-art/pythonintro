#OOP stands for Object Oriented Programming
# A class is a blueprint of an object
# An object is an instance of a class

# CLASS
class Student:
# Constructor method
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def display(self):
# Member function
        print(f"Student name is : {self.name} age is : {self.age} score is : {self.score}")
 #instance of the class
my_obj=Student("Abigael",18, "A")
my_obj.display()
my_obj2 = Student("Ryan",17, "A")
my_obj2.display()
my_obj3 = Student("Joy",19, "B+")
my_obj3.display()
my_obj4 = Student("Sara",20, "B")
my_obj4.display()
my_obj5 = Student("Mike",16, "A-")
my_obj5.display()

