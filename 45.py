def find_max(n):
    current_max = n[0]
    for num in n[1:]:
        if num>current_max:
            current_max=num
    return current_max
print(find_max([3,11,-2,7,15,4]))
print(find_max([-8,-2,-14,-1]))
print(find_max([42]))
