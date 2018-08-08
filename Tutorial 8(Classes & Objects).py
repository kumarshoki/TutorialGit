# Classes and Objects
# A user-defined prototype for an object that defines a set of attributes that characterize any object of the class.
# The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
# A class is a code template for creating objects.
# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()
print(myobjectx.variable)

# You can create multiple different objects that are of the same class(have the same variables and functions defined).
# However, each object contains independent copies of the variables defined in the class.

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# We have a class defined for vehicles.
# Create two new vehicles called car1 and car2.
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer,
# and car2 to be a blue van named Jump worth $10,000.00

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())


# The __init__ method
# The __init__ method is similar to constructors in C++ and Java.
# It is run as soon as an object of a class is instantiated.
# The method is useful to do any initialization you want to do with your object.

# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Shokendra Kumar')
p.say_hi()

# Python program to show that the variables with a value
# assigned in class declaration, are class variables and
# variables inside methods and constructors are instance variables.
# Class for Computer Science Student
class CSStudent:
    # Class Variable
    stream = 'cse'

    # The init method or constructor
    def __init__(self, roll):
        # Instance Variable
        self.roll = roll

    # Objects of CSStudent class


a = CSStudent(101)
b = CSStudent(102)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.roll)  # prints 101

# Class variables can be accessed using class
# name also
print(CSStudent.stream)  # prints "cse"


# Python program to show that we can create
# instance variables inside methods

# Class for Computer Science Student
class CSStudent:
    # Class Variable
    stream = 'cse'

    # The init method or constructor
    def __init__(self, roll):
        # Instance Variable
        self.roll = roll

        # Adds an instance variable

    def setAddress(self, address):
        self.address = address

    # Retrieves instance variable
    def getAddress(self):
        return self.address

    # Driver Code


a = CSStudent(101)
a.setAddress("Noida, UP")
print(a.getAddress())

# write a program for two employee which shows their name and their salary.

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)


# Vector addition
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


