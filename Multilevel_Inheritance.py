# Common Base Class
class A:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello from A, {self.name}")

# Intermediate Class 1
class B(A):
     def greet(self):
        print(f"Hello from B, {self.name}")
        super().greet()

# Internediate Class 2
class C(A):
     def greet(self):
        print(f"Hello from C, {self.name}")
        super().greet()

# Derieved Class
class D(B,C):
     def greet(self):
        print(f"Hello from D, {self.name}")
        super().greet()

# Create an instance of D
obj = D("Frank")
obj.greet()