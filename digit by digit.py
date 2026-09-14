a=int(input())
a=abs(a)
count =0
while a>0:
    count=count+ a%10
    a//=10
print(count)