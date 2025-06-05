# Base Class

class parent:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Derieved class 1
class Child1(parent):
    def play(self):
        print(f"{self.name} is playing")

# Derieved class 2
class Child2(parent):
    def study(self):
        print(f"{self.name} is studying")

# Create instances of Child1 and Child2 class
obj1 = Child1("Dave")
obj2 = Child2("Eve")

obj1.greet()
obj1.play()

obj2.greet()
obj2.study()