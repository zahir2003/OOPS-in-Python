---

# 🐍 Python OOPS Concepts – Comprehensive Guide

Welcome to the **Python Object-Oriented Programming (OOPS) Concepts Repository**. This project provides a **crystal-clear, practical explanation** of OOPS in Python with examples, covering **all types of inheritance and essential concepts**. Designed to **impress recruiters, interviewers, and visitors**, it showcases your deep understanding of OOPS and clean code practices.

---

## ✨ **🔑 Key Features**

✅ Covers **all OOPS pillars** with real code examples
✅ Demonstrates **each type of inheritance** with clarity
✅ Structured explanations for **quick revision** before interviews
✅ Clean, modular, professional Python code

---

## 🛠️ **Table of Contents**

1. [Introduction to OOPS](#introduction-to-oops)
2. [Classes and Objects](#1-classes-and-objects)
3. [Encapsulation](#2-encapsulation)
4. [Abstraction](#3-abstraction)
5. [Inheritance](#4-inheritance)

   * [Single Inheritance](#single-inheritance)
   * [Multiple Inheritance](#multiple-inheritance)
   * [Multilevel Inheritance](#multilevel-inheritance)
   * [Hierarchical Inheritance](#hierarchical-inheritance)
   * [Hybrid Inheritance](#hybrid-inheritance)
6. [Polymorphism](#5-polymorphism)
7. [Method Overriding vs Overloading](#6-method-overriding-vs-overloading)
8. [Super() and Constructor](#7-super-and-constructor)
9. [Magic Methods and Dunder Methods](#8-magic-methods-and-dunder-methods)
10. [Real World Example](#9-real-world-example)
11. [Conclusion](#conclusion)

---

## 💡 **Introduction to OOPS**

**Object-Oriented Programming** is a programming paradigm based on the concept of **objects**, which can contain data and code to manipulate that data.

---

### ### **1. Classes and Objects**

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object
s1 = Student("Alice", 22)
s1.display()
```

✅ **Classes** are blueprints; **objects** are instances of classes.

---

### ### **2. Encapsulation**

Encapsulation is **binding data and methods** within a class and restricting direct access to variables using private/protected modifiers.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
```

---

### ### **3. Abstraction**

Abstraction hides **unnecessary implementation details** and shows only functionality.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area())
```

---

### ### **4. Inheritance**

Inheritance allows **one class to acquire properties of another**.

#### **Single Inheritance**

```python
class Parent:
    def func1(self):
        print("This is Parent class")

class Child(Parent):
    def func2(self):
        print("This is Child class")

obj = Child()
obj.func1()
obj.func2()
```

---

#### **Multiple Inheritance**

```python
class Father:
    def func1(self):
        print("Father")

class Mother:
    def func2(self):
        print("Mother")

class Child(Father, Mother):
    def func3(self):
        print("Child")

c = Child()
c.func1()
c.func2()
c.func3()
```

---

#### **Multilevel Inheritance**

```python
class Grandparent:
    def func1(self):
        print("Grandparent")

class Parent(Grandparent):
    def func2(self):
        print("Parent")

class Child(Parent):
    def func3(self):
        print("Child")

obj = Child()
obj.func1()
obj.func2()
obj.func3()
```

---

#### **Hierarchical Inheritance**

```python
class Parent:
    def func1(self):
        print("Parent")

class Child1(Parent):
    def func2(self):
        print("Child1")

class Child2(Parent):
    def func3(self):
        print("Child2")

c1 = Child1()
c2 = Child2()
c1.func1()
c2.func1()
```

---

#### **Hybrid Inheritance**

Combination of more than one type of inheritance.

```python
class A:
    def func1(self):
        print("Class A")

class B(A):
    def func2(self):
        print("Class B")

class C(A):
    def func3(self):
        print("Class C")

class D(B, C):
    def func4(self):
        print("Class D")

d = D()
d.func1()
d.func2()
d.func3()
d.func4()
```

---

### ### **5. Polymorphism**

Polymorphism means **same function name with different behavior**.

```python
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def makesound(animal):
    animal.sound()

c = Cat()
d = Dog()
makesound(c)
makesound(d)
```

---

### ### **6. Method Overriding vs Overloading**

* **Overriding**: Child class redefines parent class method.
* **Overloading**: Same function name, different parameters (Python uses \*args/\*\*kwargs for this).

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

c = Child()
c.show()
```

---

### ### **7. Super() and Constructor**

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

c = Child("Bob", 21)
print(c.name, c.age)
```

---

### ### **8. Magic Methods and Dunder Methods**

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages

b = Book(300)
print(len(b))
```

✅ ****init**, **str**, **len**, **add**** etc. are magic methods used to customize behavior.

---

### ### **9. Real World Example**

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, fuel):
        super().__init__(brand, model)
        self.fuel = fuel

    def display(self):
        super().display()
        print(f"Fuel Type: {self.fuel}")

c = Car("Toyota", "Camry", "Petrol")
c.display()
```

---

## 🎯 **Conclusion**

This repository demonstrates **all core OOPS concepts in Python**, explained with **simple, structured examples** to solidify your understanding and real-world coding assessments.

---

## 🙌 **Get In Touch**

If you find this repository inspiring or wish to discuss **Python OOPS, Data Science, or MLOps opportunities**, feel free to connect via [LinkedIn](https://www.linkedin.com/in/sk-mahiduzzaman) or drop a message at [skmahiduzzaman@gmail.com](mailto:skmahiduzzaman@gmail.com).

---

> ⭐ **Please star the repository to support and share this work.**

---

### *“Programming is not about typing; it's about thinking.”*

---