
# Function to calculate factorial
def factorial(n):
    # Initialize result
    result = 1

    # Use a for loop to multiply result by each number from 1 to n
    for i in range(1, n + 1):
        result *= i

    return result


# Input number
number = int(input("Enter a number to find its factorial: "))

# Calculate and print the factorial
print(f"The factorial of {number} is {factorial(number)}")