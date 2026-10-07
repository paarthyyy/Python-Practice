d= input("enter numbers:")
a= [int(x) for x in d.split()]#for split
max_val = float('-inf')
second_max = float('-inf')
for num in a:
    if num > max_val:
        second_max = max_val
        max_val = num
    elif num > second_max and num != max_val:
        second_max = num
print("max =", max_val)
print("2nd max =", second_max)