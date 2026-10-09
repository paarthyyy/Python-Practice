n=int(input())
arr=list(map(int,input().split()))
ok = False
for i in range (n-1):
    if arr[i]==arr[i+1]:
        ok = True
print('yes'if ok else 'no')