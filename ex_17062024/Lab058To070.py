# ex01_June/ex_17062024/Lab058.py
# Functions
# Block of Code - Which can executed or reused.
# Define
# Call

# Built Functions - bultins.py - file (Python 3 setup)
# Which are created by the Python Contributers
result = max(2, 3)


# User Defined
# They can return something
# The can't return -> non return
# They have parameters
# They don't parameters / arguments

# def say_hello():  # No Return Type and No Parameter / Argument
#     print("Hello")
#
#
# say_hello()
#
#
# def say_hello_arg(name):  # No Return Type and with Argument
#     print("Hello", name)
#
#
# say_hello_arg("pramod")
# say_hello_arg("amit")


def say_hello_arg_default(name="Pramod"):  # No Return Type and with Default Argument
    # Write the Code
    print("Hello", name)

say_hello_arg_default()
say_hello_arg_default("Deeksha")
say_hello_arg_default(name="Sachin")



def sum_number_argument_ret(a, b): # Argument + return Type
    return a + b

# result = sum_number_argument_ret(3,4)
# result = sum_number_argument_ret(31,43)
# result = sum_number_argument_ret(a=90,b=89)
result = sum_number_argument_ret(b=101,a=99)
print(result)

# ex01_June/ex_17062024/Lab059.py
def say_hello_arg_default(name="Pramod"):
    print("Hello", name)


say_hello_arg_default()
say_hello_arg_default(name="Rajani")
say_hello_arg_default("Indu")

# Ctrl + Alt  + L - Windowns

# ex01_June/ex_17062024/Lab060.py
def f1(a, b, c):
    print(a, b, c)
    return a + b + c


print("End")

# result = f1(3, 4, 5)
# result = f1(a=4, b=6, c=9)
# result = f1(b=6, a=4, c=9)
result = f1(1,2,3)
print(result)

# ex01_June/ex_17062024/Lab061.py
def f1(a, b, c):
    return a+b+c


result = f1(10, 20, 30)
# result = f1(10, 20, 30,45)
print(result)

# ex01_June/ex_17062024/Lab062.py
# *args - any number of arguments
# print("Pramod", "Amit", "SB")


def sum_three(a=1, b=1, c=1):
    return a + b + c


# result = sum_three()
result1 = sum_three()
result2 = sum_three(1,2)
result3 = sum_three(1,2,3)
result4 = sum_three(a=10,b=67,c=45)
result5 = sum_three(b=67,a=10,c=45)
print(result1,result2,result3,result4,result5)

# ex01_June/ex_17062024/Lab063.py
# def print_argument(*args):  # ["pramod","amit","lucky"]
#     for i in args:
#         print(i, end="\n")


# *args -> List
a = ["pramod", "amit", "lucky"]
for i1 in a:
    print(i1)


for i2 in range(1, 10):
    print(i2)
#
# print_argument("pramod", "amit", "lucky")

# ex01_June/ex_17062024/Lab064.py
def make_pizza(*topings):
    for topin in topings:
        print(topin)


pramod = make_pizza("tomato")
bharkave = make_pizza("Olives","mushroom", "paneer" )
vinay = make_pizza("mushroom","pineapple","paneer","sweetcorn")

# ex01_June/ex_17062024/Lab065.py
# r = max("Amit", 2, 3, 4, 6)
r = int(max(1, 2, 3, 4, 6))
print(r)

# ex01_June/ex_17062024/Lab066.py

d = {"name":"Pramod"}
print(d)

# ex01_June/ex_17062024/Lab067.py
def make_pizza(*topings,base):
    print(topings,base)

amit = make_pizza("mushroom","tomato",base="thin crust")

# ex01_June/ex_17062024/Lab068.py
#
#
# A leap year is divisible by 4,
# but not by 100 unless it is also divisible by 400.
#
# Use an if-else statement to make this determination.

year = int(input("enter year:"))

(year % 4 == 0)
(year % 100 != 0)
(year % 400 == 0)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# ex01_June/ex_17062024/Lab069.py
# Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
#
#
#
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
#
#
#
# Use an if-else statement to classify the triangle.
#
# 3 Input
#
# side 1, side 2 and side 3
#
# output - Eq, Iso, Scalene -
#
# Eq. = side 1 == side 2 = side 3


side1 = 3
side2 = 3
side3 = 3

if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Scalene")


# ex01_June/ex_17062024/Lab070.py

# Factorial
import math
import math

n = 5
factorial = 1
# result = math.factorial(5)
# print(result)
# range(1,10) #1-9

# while n > 0:
#     factorial = factorial * n
#     n = n - 1


for i in range(1, n + 1):
    factorial *= i


print(factorial)

# fib

