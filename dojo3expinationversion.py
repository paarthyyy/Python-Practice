def solve():
    # Print a decorative title banner using "=" repeated 40 times
    print("=" * 40)
    # Print the title text, centered manually with spaces
    print("   EVEN SUM & NEGATIVE COUNT FINDER")
    # Print another line of "=" to close the banner
    print("=" * 40)
    # Print a blank line for spacing
    print()

    # Ask the user how many numbers they will enter, read it as text,
    # strip extra whitespace, and convert it to an integer
    n = int(input("How many numbers do you have? ").strip())
    # Print a blank line for spacing
    print()

    # Check if the user said they have 0 numbers
    if n == 0:
        # Tell the user 0 numbers were entered
        print("You entered 0 numbers.")
        # Print a blank line for spacing
        print()
        # Print a section header for the results
        print("RESULTS")
        # Print a dashed line under the header
        print("-" * 40)
        # Since there are no numbers, sum of evens is 0
        print("Sum of even numbers      : 0")
        # Since there are no numbers, count of negatives is 0
        print("Count of negative numbers: 0")
        # Print a closing line of "=" 
        print("=" * 40)
        # Exit the function early, skipping everything below
        return

    # Ask the user to type their numbers separated by spaces, and save the raw text
    numbers_input = input(f"Enter your {n} numbers (space separated): ")
    # Split the text into pieces at each space, convert each piece to an int,
    # and store the whole list in "numbers"
    numbers = list(map(int, numbers_input.split()))
    # Print a blank line for spacing
    print()

    # Start a counter to keep track of the total of even numbers
    even_sum = 0
    # Start a counter to keep track of how many negative numbers there are
    negative_count = 0

    # Loop through each number in the list, one at a time
    for num in numbers:
        # Check if the current number is even (no remainder when divided by 2)
        if num % 2 == 0:
            # Add this even number to the running total
            even_sum += num

        # Check if the current number is negative
        if num < 0:
            # Increase the negative counter by 1
            negative_count += 1

    # Print a section header for the results
    print("RESULTS")
    # Print a dashed line under the header
    print("-" * 40)
    # Show the full list of numbers the user entered
    print("Numbers entered           :", numbers)
    # Show the final sum of all even numbers
    print("Sum of even numbers       :", even_sum)
    # Show the final count of negative numbers
    print("Count of negative numbers :", negative_count)
    # Print a closing line of "="
    print("=" * 40)


# Call the solve() function so the program actually runs
solve()