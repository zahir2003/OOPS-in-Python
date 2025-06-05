# lst = [1,2,3]
# my_str = "MLOps"
# my_int = 155

# print(type(my_int))
# print(type(my_str))
# print(type(lst))
# lst.clear()
# print(lst)
# my_str = my_str.capitalize()
# print(my_str)
# print("\n")

# # Functions
# a1 = len(lst)
# print(a1)

# Methods
from OOPS_Project import Chatbook
obj = Chatbook()
# obj.post()

# Static Method
print(obj.id)
# obj2 = Chatbook()
# print(obj2.id)
# obj3 = Chatbook()
# print(obj3.id)


obj1 = Chatbook()
print(obj1.id)
# Using static method directly from class rather than using obj
Chatbook.set_id(10)
obj2 = Chatbook()
print(obj2.id)
obj3 = Chatbook()
print(obj3.id)

# To show the hidden data
# print(obj._Chatbook__name)

# # Getter and Setter
# print(obj.get_name())
# obj.set_name("Zahir")
# print(obj.get_name())