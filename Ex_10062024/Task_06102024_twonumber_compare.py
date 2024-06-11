# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
# Function to compare two numbers
def compare_numbers(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 < num2:
        return f"{num1} is less than {num2}"
    else:
        return f"{num1} is equal to {num2}"

# Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers and get the result
result = compare_numbers(num1, num2)

# Print the result
print(result)