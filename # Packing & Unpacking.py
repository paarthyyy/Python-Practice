# Packing & Unpacking
point = (3, 5)  # Packing
x, y = point  # Unpacking

print(x)  # Output: 3
print(y)  # Output: 5

# One-Line Swap (No temporary variable needed!)
a, b = 10, 20
a, b = b, a

print(a, b)  # Output: 20 10