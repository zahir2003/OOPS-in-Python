# Super Keyword

# Base/Parent class
class Animal:
    def __init__(self):
        self.name = "Tommy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derieved/Child class
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak() # Call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")


# Create an instance of Dog class
obj = Dog("Golden Retriever")
obj.speak()
