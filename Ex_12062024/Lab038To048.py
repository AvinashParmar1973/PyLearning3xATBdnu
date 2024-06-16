# ex01_June/ex_12062024/Lab038.py

# ✅ Conditions
# age > 18 -> You are allowed to go the club
# age < 18 -> You are not allowed

# pramod -> goa -> father permission
# pramod -> no goa -> no permission

# If, ELSE
# Syntax
# if condition:
#     code to be executed
# else:
#     code to be executed when condition is false

# Write a program to take a user age and let him know if he can go the club.

# Take a user pinput

age = int(input("Enter your Age"))

if age > 18:
    print("Go to the club")
else:
    print("Not allowed")

# ex01_June/ex_12062024/Lab039.py
age1 = int(input("Enter your Age"))
if age1 == 5: # = Assignment, == condition
    print("Hello")
else:
    print("Bye")

#ex01_June/ex_12062024/Lab040.py
# Avinash - Multiple condition

a = 10
b = 45
x = 10
y = 67

result1 = (a > b) # False
result2 = (x < y) # True
result3 = result1 and result2 # False and True
print(result3) # False


#And Gate
# False |False | False
# False |True  |  False
# True  |False | False
# True  |True  | True

# ex01_June/ex_12062024/Lab041.py
# Problem to find the max between two

a1 = int(input("Enter num1\n"))
b1= int(input("Enter num2\n"))

# Max
# result = max(a,b)
# print(result)

if a1 > b1:
    print(a1)
else:
    print(b1)
# ex01_June/ex_12062024/Lab042.py

# Avinash - Multiple Condition


# Problem  Find the Max between 3 numbers

# num1, num2 , num3

# num1 > num2 and num1 > num3 ->  num1
#
# num2 > num1 and num2 > num3 -> num2
#
# num3

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

# max()

# outTrue if conditin else outfalse

# ex01_June/ex_12062024/Lab043.py
#  LOOPs
# Repeat a block of code multiple times.


# Print Hello World 10 times

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# for loop


# for pramod in range(5):  # 0 to 4
#     print(pramod)
#
# for amit in range(1,5):  # 1 to 4
#     print(amit)

# for i in range(3, 5):
#     print(i)

#Range(start, stop, step)

for i in range(1, 10, 9):
    print(i)

# ex01_June/ex_12062024/Lab044.py
for i in range(1, 11):
    print("Hello -> ", i)


# range = 190
# print(range)

x = list(range(1,20,2))
print(x)
#Answer [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x1 = list(range(0,20,2))
print(x1)
# Answer [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for i1 in range(2, 22):
    print("Hello -> ", i1+1)

# ex01_June/ex_12062024/Lab045.py
# while
i = 0
while i < 5:
    print(i)
    i = i+1


# i = 0 , 0 < 5 -> 0
# i = 1 , 1 < 5 -> 1
# i = 2 , 2 < 5 -> 2
# i = 3 , 3 < 5 -> 3
# i = 4 , 4 < 5 -> 4
# i = 5 , 5 < 5 -> Out of the loop

# ex01_June/ex_12062024/Lab046.py
# Write a program that calculates and displays the letter grade for a
# given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Multiple condition - if, elif, else

# Step 1# Logic Building
# Input ?
# score ->  int
score = int(input("Enter the score\n"))
# output - String -> A,B,C,D,F - st


# Step 2
# Write the rough logic and convert to real one

# score >=90 and score <=100 -> A
# score >=80 and score <=89 -> B
# score >=70 and score <=79 -> C
# score >=60 and score <=69 -> D
# score >=0 and score <=59 -> F



if score >= 90 and score <= 100:
    print("Grade is A")
elif score >= 80 and score <= 89:
    print("grade is B")
elif score >= 70 and score <= 79:
    print("grade is C")
elif score >= 60 and score <= 69:
    print("grade is D")
elif score >= 0 and score <= 59:
    print("grade is F")
else:
    print("Invalid Score")



# For
# While
# If else
# If elif else

# ex01_June/ex_12062024/Lab047.py

age = 30
name = "Pramod"

if name == "Pramod":
    if age == 30:
        print("Allowed")
    else:
        print("Not Allowed!, wrong age")
else:
    print("Wrong Name")

# Define the number for which you want to create a multiplication table (EXTRA PRACTICE)
number = int(input("Enter the number: " ))

# Use a for loop to iterate through the range 1 to 10 (inclusive)
for i in range(1, 11):
    # Calculate the product
    product = number * i
    # Print the result
    print(f"{number} x {i} = {product}")

# ex01_June/ex_12062024/Lab048.py

    # Define the age
age = int(input("Enter the age: "))

# Use an if statement to check if age is greater than 100
if age > 100:
    print("You are old")
else:
    # This block will execute if the condition age > 100 is not met
    print("You are not that old")




