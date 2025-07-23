---

# 🐍 Object-Oriented Programming (OOPS) in Python

Welcome to my **OOPS in Python repository** – a comprehensive yet concise guide to mastering **Object-Oriented Programming concepts** with real-world examples and clear explanations. This repository is designed to **impress recruiters, interviewers, and visitors** by demonstrating clean coding practices, conceptual clarity, and practical implementations.

---

## ✨ **Why OOPS Matters?**

Object-Oriented Programming (OOPS) is a programming paradigm that enhances **modularity, reusability, scalability, and maintainability** of code, making it essential for software development, data science, and production-grade ML pipelines.

---

## 📚 **Key Concepts Covered**

### 🔹 **1. Class & Object**

* **Class**: Blueprint of an object.
* **Object**: Instance of a class.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

mycar = Car("Toyota", "Corolla")
print(mycar.brand, mycar.model)
```

---

### 🔹 **2. Inheritance**

Enables a class to derive properties from another class, promoting **code reusability**.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, cc):
        super().__init__(brand)
        self.cc = cc

b = Bike("Yamaha", 150)
print(b.brand, b.cc)
```

---

### 🔹 **3. Encapsulation**

Restricts direct access to variables and methods for **data protection**.

```python
class Student:
    def __init__(self):
        self.__marks = 0   # private variable

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(85)
print(s.get_marks())
```

---

### 🔹 **4. Polymorphism**

Enables the same method name to perform **different tasks**.

```python
class Bird:
    def intro(self):
        print("I am a bird")

    def flight(self):
        print("Some birds can fly, some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

obj = Sparrow()
obj.intro()
obj.flight()
```

---

### 🔹 **5. Abstraction**

Hides internal complexities and exposes only **essential features**.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

sq = Square(4)
print(sq.area())
```

---

## ⚙️ **Tools & Techniques Used**

| Category           | Tools/Features                                                       |
| ------------------ | -------------------------------------------------------------------- |
| **Language**       | Python 3.x                                                           |
| **Paradigm**       | Object-Oriented Programming                                          |
| **Concepts**       | Class, Object, Inheritance, Encapsulation, Polymorphism, Abstraction |
| **IDE/Notebook**   | VS Code / Jupyter Notebook                                           |
| **Best Practices** | Clean code, PEP8 compliance                                          |

---

## 💡 **Highlights**

✅ Real-world examples for each concept
✅ Clean, beginner-friendly explanations
✅ Professional code structuring
✅ Modular, scalable design patterns for production

---

## 🙌 **Get In Touch**

If you find this repository inspiring or wish to discuss **Python OOPS, Data Science, or MLOps opportunities**, feel free to connect via [LinkedIn](https://www.linkedin.com/in/sk-mahiduzzaman) or drop a message at [skmahiduzzaman@gmail.com](mailto:skmahiduzzaman@gmail.com).

---

> **⭐ Please consider starring this repository to support and share this knowledge.**

---

### *“Code is poetry when structured with OOPS.”*

---