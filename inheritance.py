class Dad:
    def __init__(self,color,dadhobby):
        self.color = color
        self.dadhobby = dadhobby
class Mum:
    def __init__(self,color,mumhobby):
        self.mumhobby = mumhobby
        self.color = color
class Boy(Dad):
    def boyinherites(self):
        print(f"Boy inherites {self.color} and {self.dadhobby}")
class Girl(Mum):
    def girlinherites(self):
        print(f"Girl inherites {self.color} and {self.mumhobby}")


# instance
my_obj=Boy("African descent", "Watching football")
my_obj.boyinherites()

my_obj1=Girl("Ugandan descent","reading books")
my_obj1.girlinherites()