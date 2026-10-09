n=int(input())
arr=list(map(int,input().split()))
ok = True
for i in range (n-1):
    if arr[i] - arr[i+1]>2:
        ok = False
print('yes' is ok else'no')