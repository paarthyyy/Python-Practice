def find_max(numbers):
    # Step 1: Assume the first element is the largest so far
    current_max = numbers[0]

    # Step 2: Loop through the remaining numbers
    for num in numbers[1:]: 
        # Step 3: If we find a larger number, update current_max
        if num > current_max:
            current_max = num

    # Step 4: Return the result after checking all elements  
    return current_max


# Test cases
print(find_max([3, 11, -2, 7, 15, 4]))  # Output: 15
print(find_max([-8, -2, -14, -1]))      # Output: -1
print(find_max([42]))                   # Output: 42