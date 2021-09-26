'''
Object
Attribute
Functions
'''
# Normal way(without use of class):-
'''
class Employee:
    pass

# Created Objects
Ayush = Employee()
Shrey = Employee()

Ayush.fname = "Ayush"
Ayush.lname = "Singh"
Ayush.salary = 44000

Shrey.fname = "Shrey"
Shrey.lname = "Dalal"
Shrey.salary = 44000

print(Shrey.fname, Shrey.lname, "has a salary of", Shrey.salary)
'''

# Good Way:-
'''
class Employee:
    increment = 1.5
    no_of_employees = 0

    # constructor - It has to run when the object is created:-
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    def increase(self):
        # self.salary = int(self.salary * Employee.increment)
        self.salary = int(self.salary * self.increment)
        # If I write only increment, this will give error
        # If I write self.increment, it first searches into constructor instance, then if there is no increment variable there it searches in the class so 1st priority is given to the constructor instance
        # If I write Employee.increment, it will search in constructor instance

    # Class method does not take self as argument and takes a class as the argument
    @classmethod
    def change_increment(cls, value):
        cls.increment = value

# Created Objects
# print("No. of employees are", Employee.no_of_employees)    # => 0
Ayush = Employee("Ayush", "Singh", 44000)
# print("No. of employees are", Employee.no_of_employees)    # => 1
Shrey = Employee("Shrey", "Dalal", 44000)
# print("No. of employees are", Employee.no_of_employees)    # => 2

print(Shrey.fname, Shrey.lname, "has a salary of", Shrey.salary)
# Shrey.increase()
# print(Shrey.fname, Shrey.lname, "has a salary of", Shrey.salary)

print(Ayush.fname, Ayush.lname, "has a salary of", Ayush.salary)
# print(Ayush.__dict__)   # This will give all the variables of instance
# Ayush.increment = 1.3      Now, we have a class method for this
# Ayush.increase()
# print(Ayush.__dict__)
# print(Ayush.fname, Ayush.lname, "has a salary of", Ayush.salary)

# print(Employee.__dict__) # This will give all the variables of all objects

print(Ayush.salary)
Employee.change_increment(1.3)
Ayush.increase()
print(Ayush.salary)
'''

# Using Class method as alternative constructor:-
'''
class Employee:
    increment = 1.5
    no_of_employees = 0
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    # Class method as alternative constructor:-
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

Maanit = Employee.from_str("Maanit-Sheth-76000")
print(Maanit.fname, Maanit.lname, "has a salary of", Maanit.salary)
'''

# When neither class variable is needed nor the self variable is needed, we use a normal python function,
# a normal python function is known as static function
'''
class Employee:
    increment = 1.5
    no_of_employees = 0
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    @staticmethod
    def isOpen(day):
        if day=="sunday":
            return False
        else:
            return True

print(Employee.isOpen('sunday'))
print(Employee.isOpen('friday'))
'''

# Inheritance:-
'''
class Employee:
    increment = 1.5
    no_of_employees = 0
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    @staticmethod
    def isOpen(day):
        if day=="sunday":
            return False
        else:
            return True

class Programmer(Employee):
    def __init__(self, fname, lname, salary, language, experience):
        super().__init__(fname, lname, salary)
        self.language = language
        self.experience = experience

    # This method overrides method in Employee
    def increase(self):
        self.salary = int(self.salary * (self.increment+0.2))

Ayush = Programmer('Ayush', 'Singh', 100000, "C++", "100 years")
print(Ayush.fname, Ayush.lname, "has a salary of", str(Ayush.salary) + ", programs in", Ayush.language, "and has an experience of", Ayush.experience)
Ayush.increase()
print(Ayush.salary)

# print(help(Programmer))      # This gives a method resolution order and other description
# help(Programmer)             # This function automatically prints and does not return anything
'''

# Magic/Dunder methods:-
'''
class Employee:
    increment = 1.5
    no_of_employees = 0
    
    def __init__(self, fname, lname, salary):       # This method is called Dunder init
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def change_increment(cls, value):
        cls.increment = value

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def isOpen(day):
        if day=="sunday":
            return False
        else:
            return True

    def __add__(self, other):       # We have owerwridden the add dunder method
        return self.salary + other.salary

    def __repr__(self):
        return 'Employee {} {} {}'.format(self.fname, self.lname, self.salary)

    def __str__(self):
        return f"the name of the employee is {Ayush.fname} {Ayush.lname} and salary is {Ayush.salary}"

Ayush = Employee("Ayush", "Singh", 50000)
Shrey = Employee("Shrey", "Dalal", 44000)

# print("1" + "1")
# print(1 + 1)

# Dunder add example
a = 6
# print(a.__add__(7))     # => 13
# 6 + 7 runs the Dunder add method\
# init is also a dunder method
# You can also search built in dunder methods on google

# Dunder Multiplication example
# print(a.__mul__(7))     # => 42

# Now, we can do this:-
# print(Ayush + Shrey)        # Now, the salary of Ayush and salary of Shrey is added
print(repr(Ayush))    # Before, overwriding the dunder method, this returns something like <__main__.Employee object at 0x0000027695CC5F40>
print(Ayush)
print(str(Ayush))
'''

# Property Decorators, setters and deleters
class Employee:
    increment = 1.5
    no_of_employees = 0
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.email = fname + lname + '@email.com'   # By writing it like this, if the lname changes, the email remains same so we will not do it like this
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def change_increment(cls, value):
        cls.increment = value

    @property               # By this, it will not be seen as a function but as an attribute. So, it can be changed afterwards
    def email(self):
        if self.fname == None:
            return 'Email not set or deleted'
        else:
            return self.fname + '.' + self.lname + '@email.com'

    @email.setter           # This is used to set the value of attribute
    def email(self, givenEmail):
        nameList = givenEmail.split('@')[0].split('.')
        self.fname = nameList[0]
        self.lname = nameList[1]

    @email.deleter
    def email(self):
        # del self.fname
        # del self.lname
        self.fname = None
        self.lname = None

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def isOpen(day):
        if day=="sunday":
            return False
        else:
            return True

if __name__ == "__main__":
    Ayush = Employee('Ayush', 'Singh', 44000)
    Shrey = Employee('Shrey', 'Dalal', 44000)
    # print(Ayush.email())
    print(Ayush.email)
    Ayush.email = "Hallo.Hello@email.com"
    print(Ayush.email)
    del Ayush.email
    print(Ayush.email)  # This gives error because email is not there, so we added if else in email method