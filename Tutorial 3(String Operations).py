# Basic String Operations
#the first thing you learned was printing a simple sentence.

astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

print(astring.index("o"))
print(astring.count("0"))

print(astring[3:7]) # This prints a slice of the string, starting at index 3,
                    # and ending at index 6. But why 6 and not 7?
                    # Again, most programming languages do this -
                    #it makes doing math inside those brackets easier.

print(astring[3:7:2])#This prints the characters of string from 3 to 7 skipping one character.
                     # This is extended slice syntax. The general form is [start:stop:step].

print(astring[::-1]) # reverse the string

astring = "Hello world!"
print(astring.upper()) # upper case letter
print(astring.lower()) # lower case letter

astring = "Hello world!"
print(astring.startswith("Hello")) # true condition satisfy because it is starting from "Hello"
print(astring.endswith("asdfasdfasdf")) # False condition because it is ending from "world"

astring = "Hello world!"
afewwords = astring.split(" ") # splits at a space


# EXCERCISE

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing) odd number
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

