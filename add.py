numbers = {14, 45, 2, 89, 33, 67}
largest = next(iter(numbers))

for num in numbers:
    if num > largest:
        largest = num
print("The largest number is:", largest)
