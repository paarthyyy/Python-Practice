# Step 1: Input two numbers
num1 = float(input("Enter first number (num1): "))
num2 = float(input("Enter second number (num2): "))

# Step 2: Swap values using arithmetic operations (addition and subtraction)
num1 = num1 + num2  # Store total sum in num1
num2 = num1 - num2  # Subtract new num2 from total to get original num1 value
num1 = num1 - num2  # Subtract new num2 from total to get original num2 value

# Step 3: Display swapped values
print("Swapped num1:", num1)
print("Swapped num2:", num2)