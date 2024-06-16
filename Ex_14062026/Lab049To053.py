# ex01_June/ex_14062024/Lab049.py
# For loop
# for counter in range(0, 101, 2):  # Even
    # Define the counter
counter = int(input("Enter the counter: "))
for counter in range(1, 101):  # Odd
    print(counter)
    if counter == 5:
        break

print("Outside of the program")

# ex01_June/ex_14062024/Lab050.py
# range - Can  be negative
# for counter in range(10,0,-1):
#     print(counter)


for counter in reversed(range(0,10)):
    print(counter)

# ex01_June/ex_14062024/Lab051.py

# Break ->  based on condition if will kick you
# out of the loop.


# Pass -> ? pass do nothing  - Skip the code
for i in range(10):  # 0-9
    print(i)
    if i == 5:
        pass
    else:
        print(i)


# ex01_June/ex_14062024/Lab052.py
# and and or ?
for i in range(0, 10):
    if i % 3 == 0:
        print(i)
    else:
        print(i*2)

# ex01_June/ex_14062024/Lab053.py
# Multiple Conditions
# Switch in JAVA - I
# Match Case
numbers = int(input("Enter a Number\n"))
browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed!")
    case "firefox":
        print("FF code executed!")
    case _:
        print("No browser Found!")