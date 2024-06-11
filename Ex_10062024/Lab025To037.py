print("ex_10062024/Lab025.py")
# Literals
# var_name = variable_value
name = "SaiSantosh"
# var_name -> Identifier
# var_val -> Literals
# Literals are the actual values assigned
# Literals can be Numeric and Non-Numeric.
age = 12
pi = 3.14
is_married = True
have_lambo = None
my_list = []
my_set = {}
print("ex_10062024/Lab026.py")
my_set = {1, 2, 3, 4, 5, 5} # Collection of Unique items
print(my_set)

newline_char = '\n'
newline_char2 = '\t'
newline_char3 = '\b' # backspace
print("ex_10062024/Lab027.py")
is_married = True
is_pramod_married = False

# Decimal Number System
age = 65

# Binary 0, 1
number_ten = 0b1010 # -> decimal = 10

# 10 -> 1010

# Oct
c = 0o130

# Hex
d = 0x12c


# String
name = "Pramod"

name2 = 'Pramod'

mul_string_line = """ This is Multi
line strng we can have
lines which you can type
anything
like story
"""

# Boolean Liters
x = True
y = False
print("ex_10062024/Lab028.py")
# Operators

# Assignment Operator
# = - assign the value from right to left
name = "Pramod"

# == -> Compare operator ( bool)

v1 = (1 == True)
v2 = (0 == False)
print(v1)
print(v2)

age = +65 # Unary Operator + ( Pycharm +_ -> Remove, Self exp.
num = -1
print(age)
print(num)
r = age+num # BODMAS - Math
print(r)

# Not Operator (Boolean)
is_married = True
print(not is_married)

# Is Operator - Identity Operator - Return bool
# List
a = 6
b = 6
c = False

print(a is b)

my_list = [1, 2, 3]
my_list2 = [1, 2, 3]
print(my_list is my_list2)

# is - How? - Conditions

print("ex_10062024/Lab029.py")
# Arithmetic Operators
# +,-,*,/, %
a = 180
b = 90
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # Float - Why Python is smart - div

print(a % b)
print(10 ** 2)
r = pow(10, 2)
print(r)

# Modulus - Operator -> Reminder
# 90 | 180 | 2
#    | 180 |
#    |   0 |
#
print(87 % 10)
print(87 // 10) # Q

print("ex_10062024/Lab030.py")
print(10 / 10)

# Logical Operator - bool
x = 10
y = 20
print(x > y)
print(x < y)

a = 10
b = 10
print(a >= b)  # 10 > 10 or 10 = 10
print(a == b)  # 10 > 10 or 10 = 10
print(not a)
# Or Gate

f = False
t = True
print(f and t)
print(f or t) # Truth Table of or

print("ex_10062024/Lab031.py")
x = 10
y = 20

result = (x != y) # 10 not equal 20 -> True
print(result)
print("ex_10062024/Lab032.py")
# Ternary Operator
pramod_marks = 90
amit_marks = 97

#   x > y -> do something - print("pramod")
# y > x -> do something else -> print("amit)
print("pramod is winner" if pramod_marks > amit_marks else "amit is winner")


if pramod_marks > amit_marks:
    print("pramod is the winner")
else:
    print("Amit is the winner")
print("ex_10062024/Lab033.py")
# Program - Calculate the area of circle.
# input -> radius
# output -> area
import math

# data types
# input -> int or float -> float
# output -> float

# Core Logic -> pi*r*r = 3.14

radius = float(input("Enter the radius\n"))
print(math.pi)
area = math.pi*(radius**2)
area2 = math.pi*(math.pow(radius,2))
print(area)
print(area2)
print("ex_10062024/Lab034.py")

print(3.141592653589793*(float(input("Enter the radius\n"))**2))

print("ex_10062024/Lab035.py")
# Math
import math
a = math.pow(2,2)
pi = math.pi
print(a)
print(pi)

result = math.sin(90)
print(result)
print("end")