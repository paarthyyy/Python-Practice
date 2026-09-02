number = int("hello")
try:                       #attempt to convert the string "hello" to an integer, which will raise a ValueError since "hello" is not a valid integer representation
    number = int("hello")
except ValueError:         #catch the ValueError exception that is raised when trying to convert "hello" to an integer and print a message indicating that the input is not a valid number
    print("That's not a number!")

try:
    x = 10 / 0             #attempt to divide 10 by 0, which will raise a ZeroDivisionError since division by zero is not allowed in mathematics
except ZeroDivisionError:
    print("Cannot divide by zero")

nums = [2, 7, 11, 15]
target = 9