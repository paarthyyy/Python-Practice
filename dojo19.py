n = int(input())
arr = list(map(int, input().split()))

i, j = 0, n - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i +=1
    j -=1

print(*arr)
