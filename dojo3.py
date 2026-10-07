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