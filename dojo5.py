def max_num(paarth):
    current_max = [0]
    for i in paarth [1:]:
        if i > current_max:
            current_max=i
    return current_max        
print(max_num([2,4,1,7,54,3]))
print(max_num([-8, -2, -14, -1]))      
print(max_num([42]))