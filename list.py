numbers = [4, 8, 2, 15, 6]

largest = numbers[0]

for num in numbers: 
    if num > largest:
        largest = num

print(largest)
numbers.append(50) # Append 50 to the list
numbers.remove(4) # Remove 4 from the list
len(numbers) #find the actuly lenght 
for num in numbers: 
    print(num)