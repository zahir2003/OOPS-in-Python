# Base 1 class
class Grandparent:
    def __init__(self,name):
       self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story.")

# Base 2 class
class Parent(Grandparent):
    def work(self):
        print(f"{self.name} is working")

# Derieved class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")


# Creates an instance of Child Class
obj = Child("Charlie")
obj.tell_story()
obj.work()
obj.play()
