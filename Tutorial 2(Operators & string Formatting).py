remainder = 11 % 3
print(remainder)

squared = 7 ** 2
print(squared)
cubed = 2 ** 3
print(cubed)


# Using Operators with Strings
lotsofhellos = "hello" * 10
print(lotsofhellos)

#Using Operators with Lists

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#The target of this exercise is to create two lists called x_list and y_list,
# which contain 10 instances of the variables x and y, respectively.
# You are also required to create a list called big_list,
# which contains the variables x and y, 10 times each,
# by concatenating the two lists you have created

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
else:
    print("Great!")

# String Formatting
# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

#To use two or more argument specifiers, use a tuple (parentheses)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#Any object which is not a string can be formatted using the %s operator as well.
# The string which returns from the "repr" method of that object is formatted as the string

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# You will need to write a format string which prints out the data using the following syntax:
# Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)