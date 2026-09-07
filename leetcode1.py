input_arr = [2, 7, 11, 15,15,11]
target = int(input("Enter the target value: "))
found = False

for i in range(len(input_arr)):
    for j in range(i + 1, len(input_arr)):
        if input_arr[i] + input_arr[j] == target:
            print([i, j])
            found = True

if not found:
    print("No solution found")
            