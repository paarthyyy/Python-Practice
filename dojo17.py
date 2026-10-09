n = int(input())
arr = list(map(int, input().split()))

ok = True
for i in range(n):
    if arr[i] % 3 != 0:
        ok = False

print('Yes' if ok else 'No')