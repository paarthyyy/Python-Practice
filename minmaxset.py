d = input("Enter numbers : ")
a = [int(x) for x in d.split()]
max_val = a[0]
min_val = a[0]
for num in a:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print("max =", max_val)
print("min =", min_val)