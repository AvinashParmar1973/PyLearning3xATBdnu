num1 = input("Enter the first number: ")
# Square
square = int(num1)*int(num1)
print("by simple steps :",square)

square1 = int(num1)**2
print("by ** power option :",square)

num2 = input("Enter the Second number: ")
# Cube
cube = int(num2)*int(num2)*int(num2)
print(cube)
print("by simple steps :",cube)
cube1 = int(num1)**3
print("by *** power option :",cube1)

# Function to calculate square and cube of a number
def calculate_square_and_cube(int_num):
    square = int_num ** 2
    cube = int_num ** 3
    return square, cube

# Input number
int_num = int(input("Enter number:"))

# Calculate square and cube
square, cube = calculate_square_and_cube(int_num)

# Print the results
print(f"The square of {int_num} is {square}")
print(f"The cube of {int_num} is {cube}")