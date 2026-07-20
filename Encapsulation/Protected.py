class Employee:
    def __init__(self, name, age):
        self.name = name  # public
        self._age = age  # protected


class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)  # Accessible in subclass


emp = SubEmployee("Ross", 30)
print(emp.name)  # Public accessible
emp.show_age()

