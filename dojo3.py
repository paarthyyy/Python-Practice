<<<<<<< HEAD
def solve():
    n = int(input().strip())
    if n == 0:
        print("0 0")
        return
    numbers = list(map(int, input().split()))
    even_sum = 0
    negative_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        if num < 0:
            negative_count += 1
    print(f"{even_sum} {negative_count}")

solve()                                                                                                                 
=======
def solve():
    print("=" * 40)
    print("   EVEN SUM & NEGATIVE COUNT FINDER")
    print("=" * 40)
    print()

    n = int(input("How many numbers do you have? ").strip())
    print()

    if n == 0:
        print("You entered 0 numbers.")
        print()
        print("RESULTS")
        print("-" * 40)
        print("Sum of even numbers      : 0")
        print("Count of negative numbers: 0")
        print("=" * 40)
        return

    numbers_input = input(f"Enter your {n} numbers (space separated): ")
    numbers = list(map(int, numbers_input.split()))
    print()

    even_sum = 0
    negative_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num

        if num < 0:
            negative_count += 1

    print("RESULTS")
    print("-" * 40)
    print("Numbers entered           :", numbers)
    print("Sum of even numbers       :", even_sum)
    print("Count of negative numbers :", negative_count)
    print("=" * 40)


solve()
>>>>>>> 0981ad8685c870ca7bf0ce4be72d496e180f8ead
