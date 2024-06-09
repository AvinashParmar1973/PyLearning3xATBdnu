print("hello world")
print(2+2)
print(2-2)
print(2/2)
print(2*2)

#proper intentation
print("hello","world", 123,"test")
# sep
print("hello","world", 123,"test",sep="     ")
# one arguments
print("Hi, my name is avinash")

# one arguments
print("Hi, my name is avinash","parmar")

# print()
# self - Concept in OOps which points to itself - ignore.
# *args - Unlimited number of arguments * - string, int, float, boolean...
# sep=' ' - How you want to separate the arguments
# end='\n' - in the end what you want to do
# file=None - File IO


print("Hello", "World", 123, True, 3.14)


# use of \t , to print multiple sentences in one sentence (ex_05062024/Lab004.py)
print("Hi", "Neeta", "Parmar",sep="-",end="\t")
print("Hi", "Avi", "Param")

# use of _ for concatenate two sentences (ex_05062024/Lab005.py)
# print(sep="-", "Hi", "Manesh")
print("I am Good Person", end="_")
print("I am Bad Person")
# Python is case sensitive

# Program to find the max in two numbers (ex_05062024/Lab006.py)
print(max(10, 23))
print(max(10, 23, 45))
print(max(10, 23, 45, -1, -2, 100, 1, 87.34))

# TypeError: '>' not supported between instances of 'str' and 'int'
# print(max(10, 23, 45, -1, -2, 100, 1, "John"))

# IndentationError: unexpected indent (ex_05062024/Lab007.py)
#    print("Hello World")

# ✅ Dynamically typed  (ex_05062024/Lab008.py)
# Dynamic Type - Type of Data that Python supports.
age = 65
# variableName = variableValue
# identifier = literal

# Types which are supported in the Python

# Integers - Positive and negative whole numbers.
# 1, -1,123, 999, 100000, 96543210

# Floating Points Numbers
# 3.14, 5.3333333 , 18.00, 0.000786  . -0.4, -1.6
pi = 3.14

# String
# "pramod", "A", "hello world", "Hi, I am good person, You are a liar", "12345"
name = "John"

# Boolean
# True, False
# true, false ? boolean?
isMale = True

# How do I check the type of the variable?
print(type(age))
print(type(name))
print(type(isMale))
print(type(pi))

# Python - Complex NUMBER - i iota -
complex_number = 2 + 3j
# Real - 2
# Imaginary - 3
print(complex_number.real)
print(complex_number.imag)

# Complex Data types in Python
# List
# Tuple
# Dictionary
# Set

# ex_05062024/Lab009.py
age = 65
# Dynamically typed
print(type(age))
age = "sixty five"
print(type(age))

# ex_05062024/Lab010.py
# variable name should be start grom A-Z, a-z _
name = "John"
print(type(name))

# variable name should not start with number
# 123 =345 - variable names


# variable name should not be any keyword
# keyword ? // Reserved word
# 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield' [2]
# and = 123

# variable name should not be any special character
# @ = 123
# $ = 344
_ = 123
print(_)
_name = "john"
print(_name)
# $john = "john"
# john$ = "Hello"

# variable name should not be any space
# first name = "john"
first_name = "john"
print(first_name)
# Python love the snake case
varaible_name = "john"
print(varaible_name)

long_var_name_is_created_here = "Hello"
print(long_var_name_is_created_here)


# ex_05062024/Lab011.py
print("ex_05062024/Lab011.py")
# Numbers
# Integer (whole)
age = 78
age = -90
roll_number = 123
phone_number = 9876543210

print(type(age))

pi = 3.14
gst = 0.18
pi = -3.14

print(type(pi))

isMarried = True
isSantoshMarried = False

name = "JOHN"
name2 = 'JOHN'
name3 = """JOHN
dasdasd
das
dasd
asd
as
das
da
sd
asd
a
"""

print(type(name), name)
print(type(name2),name2)
print(type(name3),name3)

print("ex_05062024/Lab013.py")
# Take an input from the username, and print it.
first_name = input("Enter your First name:")
last_name = input("Enter your Last name:")
print("Your first name is ", first_name, "and your last name is ", last_name)
