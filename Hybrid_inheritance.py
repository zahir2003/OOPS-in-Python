# Base Class
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

# Intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk")

# Intermediate Class 2 (Multilevel)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")

# Derieved Class (Multilevel Inheritance)
class Bat(Mammal,Bird):
    def __init__(self, name):
        Mammal.__init__(self,name) # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal")

# Create an instance of Bat
obj = Bat("Bruce")
obj.sound()
obj.feed()
obj.fly()
obj.nocturnal()
