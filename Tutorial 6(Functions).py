# Functions
# Functions are a convenient way to divide your code into useful blocks,
# allowing us to order our code, make it more readable, reuse it and save some time.
# Also functions are a key way to define interfaces so programmers can share their code.

# Functions in python are defined using the block keyword "def",
# followed with the function's name as the block's name. For example:
# def my_function():
#     print("Hello From My Function!")
# Functions may also receive arguments (variables passed from the caller to the function). For example:
# def my_function_with_args(username, greeting):
#     print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
# Functions may return a value to the caller, using the keyword- 'return' . For example:
# def sum_two_numbers(a, b):
#     return a + b


# Q.1 How do you call functions in Python?
# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)


# Q2. Add a function named list_benefits() that returns the following list of strings:
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# a function named build_sentence(info) which receives a single argument containing a string and returns a sentence
# starting with the given string and ending with the string " is a benefit of functions!"


# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()


# Two types of function
#(1) Built in Function :- Functions that are built in Python.
# (2) User Defined Function :- Functions defined by users themselves.

# Built-in functions

# Method	Description

# Python abs()	returns absolute value of a number
# Python all()	returns true when all elements in iterable is true
# Python any()	Checks if any Element of an Iterable is True
# Python ascii()	Returns String Containing Printable Representation
# Python bin()	converts integer to binary string
# Python bool()	Coverts a Value to Boolean
# Python bytearray()	returns array of given byte size
# Python bytes()	returns immutable bytes object
# Python callable()	Checks if the Object is Callable
# Python chr()	Returns a Character (a string) from an Integer
# Python classmethod()	returns class method for given function
# Python compile()	Returns a Python code object
# Python complex()	Creates a Complex Number
# Python delattr()	Deletes Attribute From the Object
# Python dict()	Creates a Dictionary
# Python dir()	Tries to Return Attributes of Object
# Python divmod()	Returns a Tuple of Quotient and Remainder
# Python enumerate()	Returns an Enumerate Object
# Python eval()	Runs Python Code Within Program
# Python exec()	Executes Dynamically Created Program
# Python filter()	constructs iterator from elements which are true
# Python float()	returns floating point number from number, string
# Python format()	returns formatted representation of a value
# Python frozenset()	returns immutable frozenset object
# Python getattr()	returns value of named attribute of an object
# Python globals()	returns dictionary of current global symbol table
# Python hasattr()	returns whether object has named attribute
# Python hash()	returns hash value of an object
# Python help()	Invokes the built-in Help System
# Python hex()	Converts to Integer to Hexadecimal
# Python id()	Returns Identify of an Object
# Python input()	reads and returns a line of string
# Python int()	returns integer from a number or string
# Python isinstance()	Checks if a Object is an Instance of Class
# Python issubclass()	Checks if a Object is Subclass of a Class
# Python iter()	returns iterator for an object
# Python len()	Returns Length of an Object
# Python list() Function	creates list in Python
# Python locals()	returns dictionary of current local symbol table
# Python map()	Applies Function and Returns a List
# Python max()	returns largest element
# Python memoryview()	returns memory view of an argument
# Python min()	returns smallest element
# Python next()	Retrieves Next Element from Iterator
# Python object()	Creates a Featureless Object
# Python oct()	converts integer to octal
# Python open()	Returns a File object
# Python ord()	returns Unicode code point for Unicode character
# Python pow()	returns x to the power of y
# Python print()	Prints the Given Object
# Python property()	returns a property attribute
# Python range()	return sequence of integers between start and stop
# Python repr()	returns printable representation of an object
# Python reversed()	returns reversed iterator of a sequence
# Python round()	rounds a floating point number to ndigits places.
# Python set()	returns a Python set
# Python setattr()	sets value of an attribute of object
# Python slice()	creates a slice object specified by range()
# Python sorted()	returns sorted list from a given iterable
# Python staticmethod()	creates static method from a function
# Python str()	returns informal representation of an object
# Python sum()	Add items of an Iterable
# Python super()	Allow you to Refer Parent Class by super
# Python tuple() Function	Creates a Tuple
# Python type()	Returns Type of an Object
# Python vars()	Returns __dict__ attribute of a class
# Python zip()	Returns an Iterator of Tuples
# Python __import__()	Advanced Function Called by import

# (2) User defined function
# Example:-

# Program to illustrate
# the use of user-defined functions

def add_numbers(x,y):
   sum = x + y
   return sum

num1 = 5
num2 = 6

print("The sum is", add_numbers(num1, num2))

# some examples of functions
# The least common multiple (L.C.M.) of two numbers is the smallest positive integer
# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

# change the values of num1 and num2 for a different result
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# uncomment the following lines to take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))

