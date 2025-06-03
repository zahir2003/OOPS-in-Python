# Initialize a Class
class Employee:
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/data have been initialized")

    # Method
    def company(self,name):
        print("This company method was called manually")
        print(f"The company name is : {name}")


# Create an object/instance of the class
sam = Employee()
# print(sam.id)
# print(sam.salary)
# print(sam.designation)
sam.company("Google")
print(type(sam))