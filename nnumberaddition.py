n = int(input("Enter a number: "))

total_sum = 0
for i in range(1, n + 1):
    total_sum += i  

print(f"Sum of the first {n} numbers:", total_sum)