#LIST DATA STRUCTURE
#It is ordered
#It is mutable
#It has an index
fruit=["Mangoes","Banana","Oranges","Avocado","Pineapples","Apples","Grapes"]
print(fruit)
fruit[1]="Watermelon"
print(f"I love eating {fruit[0]}")
numbers=[1,3,5,8,1,4,0,-2,5]
numbers.sort()
numbers.append("Pineapples")
numbers.pop(0)
numbers.reverse()
print(numbers[4])
print(numbers)

#TUPLE DATA STRUCTURE
#It is ordered
#It has an index
#It is immutable
cars=("Mercedes","Nissan","Toyota","Subaru","Range Rover","Mazda","Honda","Vw")
numbers1=(3,9,8,1,0,4,5,4,33,-78,-2)
# cars[6]="Suzuki"
print(cars)
# cars.count()
print(f"Japan produces {cars[2]}")
print(numbers1)
print(sorted(numbers1))

#SET DATA STRUCTURE
#Not ordered
#Not indexed
country={"Kenya","Uganda","Tanzania","Burundi","Rwanda","USA","Dubai","Mexico"}
print(country)
country.pop()
# country[0]="Nigeria" NOT SUPPORTED
print(country)

#DICTIONARY DATA STRUCTURE
#Key value pair
#It is mutable
student={"name":"Abigael","Age":18,"Gender":"Female","Phone number":+254769025481}
student['name']="John"
print(f"My name is {student['name']}, im {student['Age']} years old, my gender is {student["Gender"]} and my number is {student['Phone number']}")

