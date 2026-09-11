def find_max(a):
    current_max=[0]
    for num in a [1:]:
        if num> current_max:
            current_max = num
print(find_max([3, 11, -2, 7, 15, 4]))  
print(find_max([-8, -2, -14, -1]))      
print(find_max([42])) 