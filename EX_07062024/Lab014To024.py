
print("ex_07062024/Lab014.py")
print("Hello World")
# Commment
# Varaible
# Data Types in Python
# int, str, float, complex, bool
# int
a = 10
print(a)
# str
b = "Hello"
print(b)
# float
c = 10.5
print(c)
# complex
d = 10 + 5j
print(d)
# bool
e = True
print(e)
print(type(a))

print("ex_07062024/Lab015.py")
# Advance Data Type in Python
# List, Tuple, Set, Dict - DS - API and Web Automation.
# Take a user input
user_input = input("Enter your name: ")
value = (print(user_input))
print(type(value))
print(type(user_input))

print("ex_07062024/Lab016.py")
# Take the 2 int number from the user and we want to add them.
# We need to use the input() function.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# type conversion - str -> int -> ? int()
result = int(num1)+int(num2)
print(result)

#  + ->  int  sum operation
#  + -> str - concat
# int to str -> str()
# str to int -> int()

print(type(int(num1)))
print(type(int(num2)))
print(type(int(result)))

print("ex_07062024/Lab017.py")
pi = 3.14
print(pi)
print(type(pi))

i = 10
i2 = 12
result = i2/i
print(result) # Python is very smart, it knows that 12/10 is a float
print(type(result))

print("ex_07062024/Lab018.py")
# Strings
# Bunch of Char
# '', "" , """
name = 'Harry'
print(name)
name = "Harry"
print(name)
name = """Harry, Is is Good person
He love to walk alone, He has a dog
....
....

....
"""
print(name)

# Raw String
dir = r'C:\nomedir\some dir'
print(dir)

# Format of the String
first_name = "Harry"
last_name = "Potter"
print(first_name + " " + last_name)
print(first_name, last_name)
# f -> formatting - it will replace the values of the variables
#{} -> placeholders
print(f'Your Full name is {first_name} {last_name}')

print("ex_07062024/Lab019.py")
# Format String
print(2 * 1)
num = 90
print(f"The number is {num * 2}")
print(f"The number is {num * 3}")

num = 5
print(f"{num}x1={num}")
print(f"{num}x2={num * 2}")
print(f"{num}x3={num * 3}")
print(f"{num}x10={num * 10}")

b = 1
print(f"{b}x1={b}")
print("2x{}={},{}".format(b, b * 2, 3))
# Thi''''''s is just use to showcase the output



print("ex_07062024/Lab020.py")

# In built Functions -
# Function -> Repeat a task - You can use a function.
# print(),input, type(), format(), max, min, id(), sum(), avg()

# Strings
name = "Amit" # 0 to 3
# 0,1,2,3
# A,m,i,t
print(name)
print(type(name))
print(id(name)) # id -> memory address where it is stored 4309895152
print(len(name))
# length of string ( 1 )
name = name.upper()
name = name.lower()
a = name.count('A')
# 0
print(a)
# t
print(name[3])
# print(name[4]) # string index out of range

# Python - Immutable - that can't be changed
# name[0] = "P" # 'str' object does not support item assignment

print("ex_07062024/Lab021.py")
name = "This is a Big line"
print(len(name))
print(type(name))
print(name[14])
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
print(name[11])
print(name[12])
print(name[13])
print(name[14])
print(name[15])
print(name[16])
print(name[17])
# IndexError: string index out of range
# print(name[18])
print(name[-1])
print(name[-2])
print(name[-10])

print("ex_07062024/Lab022.py")
val = None
#val = val+1 # unsupported operand type(s) for +: 'NoneType' and 'int'
# Data Type  - NoneType
print(val)
# Nothing
# None is not a default value
# None is not 0.
# None is not an empty string.
# None is not the same as False.

name = "" # empty String - memory allocated
print(id(name))
name = None
print(type(name)) # NoneType
print(id(name))
print(name)
name = "Amit"
print(name)
print(id(name))

print("ex_07062024/Lab023.py")
# List - Shopping List
# milk, bread, butter, poha
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit


shopping_list = ["milk", "bread", "butter", "poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("curd") # Add item in the end
print(shopping_list)
shopping_list.insert(3, "jam") # Add item in the middle
print(shopping_list)

shopping_list.extend(["chips", "salt"]) # Add multiple items in the end
print(shopping_list)

shopping_list.remove("bread") # Remove item
print(shopping_list.pop())
print(shopping_list.index("butter"))
shopping_list.reverse()
shopping_list.sort()
print(shopping_list)
shopping_list[0] ="John"
print(shopping_list)

#
my_list = [1, 2, 3, 4, True, 3.14, "john"]
print(type(my_list))  # <class 'list'>

print("ex_07062024/Lab024.py")
# Escape Seq
print("Hello \"World\"")
print("Hello \nWorld")
print("Hello \tWorld")
print("Hello \bWorld")