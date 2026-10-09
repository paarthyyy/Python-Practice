n = int(input())
arr = list(map(int, input().split()))
first = sum(arr[:n // 2])
second = sum(arr[n // 2:])
if first == second:
    print('Yes')
else:
    print('No')

