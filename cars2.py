# create a new file, create a class called cars with make,model, color,
# year as the attributes in a constructor method. Then a member function
# that prints(whatever you want to say). Create five objects of the above

class Cars:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
    def describe(self):
        print(f"The {self.color} {self.model} was manufactured by {self.make} in the year {self.year}")
my_car1 = Cars("Ford", "Mustang", "Red", "1999")
my_car1.describe()
my_car2 = Cars("Audi Hungaria", "Audi A3 Sedan convertible", "Blue", 2017)
my_car2.describe()
my_car3 = Cars("BMW group", "BMW X6", "Yellow",2019, )
my_car3.describe()
my_car4 = Cars("Automobili Lamborghini", "Lamborghini Urus", "Grey",2020, )
my_car4.describe()
my_car5 = Cars("Porsche Automobil Holding SE", "Porsche 718 Boxer", "Black",2016, )
my_car5.describe()
