# Simple Inheritance

# # Base/Parent Class
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# # Child/Derieved Class
# class Dog(Animal):
#     def nam(self):
#         print(f"{self.name} is a Dog")

# # Create an instance of Animal
# obj = Animal("Generic Animal")
# obj.speak()

# # Create an instance of Dog
# obj2 = Dog("Tommy")
# obj2.speak()
# obj2.nam()


# Constructor Overloading :

# # Base/Parent Class
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# # Child/Derieved Class
# class Dog(Animal):
#     def __init__(self):
#         self.behaviour = "friendly"

#     def speak(self):
#         print(f"{self.behaviour} is a sweet behaviour")

#     def nam(self):
#         print(f"Tommy is a Dog and he is very {self.behaviour}")

# # # Create an instance of Animal
# obj = Animal("Generic Animal")
# obj.speak()

# # Create an instance of Dog
# obj2 = Dog()
# obj2.speak()
# obj2.nam()


# Method Overloading : 

# Base/Parent Class
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child/Derieved Class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} is a Dog")

    def nam(self):
        print(f"{self.name} is a Dog and he is very friendly")

# # Create an instance of Animal
obj = Animal("Generic Animal")
obj.speak()

# Create an instance of Dog
obj2 = Dog("Tommy")
obj2.speak()
obj2.nam()