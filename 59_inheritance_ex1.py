class Person():

    # Constructor
    def __init__(self, name):
        self.name = name

        # To get name

    def getName(self):
        return self.name

        # To check if this person is employee

    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True
emp = Person("Geek1")
print(emp.getName(),emp.isEmployee())
emp =Employee("Geek2")
print(emp.getName(),emp.isEmployee())