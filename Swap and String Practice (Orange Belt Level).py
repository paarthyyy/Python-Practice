#--------------------The Tools, One at a Time---------------------------------#
#           Tool 1: Strings are like lists of characters
#           Tool 2: Negative indexes count from the end
#           Tool 3: Slicing (cutting a piece)
#           Tool 4: Strings cannot be changed in place
#           Tool 5: The list trick (to “edit” a string)
#           Tool 6: Swapping
#           Tool 7: Useful string methods
#           Tool 8: Comparing characters
#           Tool 9: Reading strings from input
#           Mini cheat sheet
#           Quick check (try without running)
s = "hello"
# index:   0   1   2   3   4
# char:    h   e   l   l   o
s = "hello"
print(s[0])     # h
print(s[4])     # o
print(len(s))   # 5
print("--------------------------------------------------------")    

for i in range(len(s)):
    print(s[i],end=' ')    # h, e, l, l, o (one per line)
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
print("--------------------------------------------------------")    
arr = [1, 2, 3]
arr[0] = 9          # fine -> [9, 2, 3]
print("--------------------------------------------------------")    
s = "hello"
chars = list(s)                 # ['h', 'e', 'l', 'l', 'o']
chars[0] = 'J'                  # ['J', 'e', 'l', 'l', 'o']
s = ''.join(chars)              # 'Jello'
print(s)
print("--------------------------------------------------------")    
arr = [1, 2, 3, 4, 5]
arr[0], arr[4] = arr[4], arr[0]
print(arr)      # [5, 2, 3, 4, 1]
print("--------------------------------------------------------")    
a = 10
b = 20
a, b = b, a
print(a, b)     # 20 10
print("--------------------------------------------------------")    
s = "python"
chars = list(s)
chars[0], chars[-1] = chars[-1], chars[0]
s = ''.join(chars)
print(s)        # nythop
print("--------------------------------------------------------")    
s = "python"
chars = list(s)
chars[0], chars[-1] = chars[-1], chars[0]
s = ''.join(chars)
print(s)        # nythop
print("--------------------------------------------------------")    
s = "Hello World"
print(s.lower())            # hello world
print(s.upper())            # HELLO WORLD
print(s.count('l'))         # 3   (how many times 'l' appears)
print(s.replace('l', 'L'))  # HeLLo WorLd
print("  hi  ".strip())     # hi  (removes spaces at both ends)
print("--------------------------------------------------------")    
sentence = "I love python"
words = sentence.split()
print(words)                # ['I', 'love', 'python']
print(len(words))           # 3
print("--------------------------------------------------------")    
print('a' in "banana")          # True
print('z' in "banana")          # False
print('x' in "aeiou")           # False
print("--------------------------------------------------------")    
s = "hello"
s.upper()           # result thrown away!
print(s)            # hello  (unchanged)
s = s.upper()       # save it
print(s)            # HELLO
print("--------------------------------------------------------")    
print('a' == 'a')           # True
print('a' < 'b')            # True (alphabetical order)
print('a' <= 'h' <= 'z')    # True (is 'h' between a and z?)
print("--------------------------------------------------------")    
print('a'.islower())    # True
print('A'.isupper())    # True
print('5'.isdigit())    # True
print('a'.isalpha())    # True
print("--------------------------------------------------------")    
# "HelloWorld".isalpha()   # True
# "Hello World".isalpha()  # False (contains a space)
# "Python3".isalpha()      # False (contains a number)
# "Café".isalpha()         # True (Unicode letters are supported)
# "".isalpha()             # False (empty string)
#print("--------------------------------------------------------")    
# arr = list(map(int, input().split()))   # "1 2 3"  -> [1, 2, 3]
# s = input()                              # "hello"  -> "hello"
# words = input().split()                  # "I love it" -> ['I', 'love', 'it']
# print("--------------------------------------------------------")    
# I want to...	Write
# Last character	s[-1]
# First 3 characters	s[:3]
# Reverse	s[::-1]
# Edit a character	list(s), edit, ''.join(...)
# Swap two spots	a[i], a[j] = a[j], a[i]
# Count a letter	s.count('a')
# Is it in the string?	ch in "aeiou"
# Split into words	s.split()
# Glue words together	' '.join(words)
#print("--------------------------------------------------------")    
# Quick check (try without running)
# What does "banana"[1:4] give?
# What does "banana"[::-1] give?
# What does "abc"[-1] give?
# What does ''.join(['x', 'y', 'z']) give?
# What does "a b c".split() give?

# Answers: ana, ananab, c, xyz, ['a', 'b', 'c'].
