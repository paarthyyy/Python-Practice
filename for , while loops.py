numbers = [10, 20, 30]

for num in numbers: #print(num) #print each number in the list
    print(num)
print("--------------------------------------------------")
for i in range(5): #print(i) #print the numbers 0 to 4
    print(i)
print("--------------------------------------------------")
numbers = [10, 20, 30] #print the indices and values of each element in the list

for i in range(len(numbers)): #print(i, numbers[i]) #print the index and value of each element
    print(i, numbers[i])
print("--------------------------------------------------")

x = 1

while x <= 5: #print(x) #print the numbers 1 to 5
    print(x)
    x += 1

print("--------------------------------------------------")
left = 0
right = len(numbers) - 1 #print the indices and values of each element in the list

while left < right: #print(left, numbers[left], right, numbers[right]) #print the index and value of each element
    print(left, numbers[left], right, numbers[right])
    ...