a=[2,5,3,2,7,5,9]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print("Duplicate element is:", a[i])