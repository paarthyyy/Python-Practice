n=int(input())
arr=list(map(int, input().split()))
ok=True
for i in range (n-1):
    if arr[i]%3!=0:
        ok = False
print('yes'if ok else'no')