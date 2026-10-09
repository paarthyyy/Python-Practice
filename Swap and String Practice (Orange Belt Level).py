s = "hello"
# index:   0   1   2   3   4
# char:    h   e   l   l   o
s = "hello"
print(s[0])     # h
print(s[4])     # o
print(len(s))   # 5
for i in range(len(s)):
    print(s[i],end=' ')    # h, e, l, l, o (one per line)
print("--------------------------------------------------------")    
for ch in s:
    print(ch,end=' ')
print()
print(s[-1])    # o  (last character)
print(s[-2])    # l  (second last)
print(s[2])
print("--------------------------------------------------------")    
s = "123456789"
#iex=012345
print(s[0:3])   # pyt   (indexes 0, 1, 2)
print(s[2:5])   # tho   (indexes 2, 3, 4)
print(s[:4])    # pyt   (no start = from the beginning)
print(s[3:])    # hon   (no end = to the very end)
print(s[:])     # python (everything)
print("--------------------------------------------------------")    
print(s[::-1])  # nohtyp   (step -1 walks backwards)
print(s[::2])   # pto      (every 2nd character)