n = int(input())
arr=list(map(int,input().split()))
ok = True
i, j = 0, n - 1
while i<j:
    if arr[i] !=arr[i]:
        ok = False
    i+=1
    j-=1
print('yes'if ok else 'no')
