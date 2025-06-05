# Single/Basic Inheritance

# Base Class
class Parent:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Derieved Class
class Child(Parent):
    def play(self):
        print(f"{self.name} is Playing")


# Create an instance of Child
obj = Child("Alex")
obj.greet()
obj.play()