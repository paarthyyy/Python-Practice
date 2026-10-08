n, target = map(int, input().split())
arr = list(map(int, input().split()))

i, j = 0, n - 1
found = False
while i < j:
    s = arr[i] + arr[j]
    if s == target:
        found = True
        break
    elif s < target:
        i += 1
    else:
        j -= 1

print('Yes' if found else 'No')

