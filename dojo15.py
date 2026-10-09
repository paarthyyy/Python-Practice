n=int(input())
arr=list(map(int,input().split()))
ok = False
for i in range (n):
    if arr[i]<0:
        ok = True
print('yes'if ok else' hell naww')