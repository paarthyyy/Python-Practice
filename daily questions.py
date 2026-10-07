# nums = [3, 1, 2]
# nums.append(5)
# nums.pop(0)
# print(nums)
# ======================================
# a = [1, 2, 3]
# a.insert(1, 10)
# a.extend([4, 5])
# a.pop()
# a.sort(reverse=True)
# print(a)
# =======================================
# x = [1, 2]
# x.append([3, 4])
# print(len(x), x)
# =======================================
# t = (1, 2, 2, 3)
# print(t.count(2), t.index(3), len(t))
# =========================================
# a, b = 4, 7
# a, b = b, a
# print(a, b)
# =========================================
# x = (5)
# y = (5,)
# print(type(x), type(y))
# =========================================
# d = {"a": 1, "b": 2}
# print(d.get("c", 0))
# =========================================
# d = {}
# for ch in "banana":
#     d[ch] = d.get(ch, 0) + 1
# print(d)
# =========================================
# d = {"x": 10}
# print(10 in d)
# =========================================
# s = {1, 2, 2, 3, 3, 3}
# print(len(s))
# =========================================
# a = {1, 2, 3, 4}
# b = {3, 4, 5}
# print(a & b, a - b, b - a, len(a | b))
# =========================================
# x = {}
# print(type(x))
# =========================================
# age = 16
# if age >= 18:
#     print("Adult")
# print("Done")
# =========================================
# x = 3
# if x == 5 or 6:
#     print("yes")
# else:
#     print("no")
# =========================================
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 50:
#     print("C")
# else:
#     print("Fail")
# =========================================

# n=int(input())
# if 10<= n <=50 and n%5!=0:
#   print("true")
# else:
#   print("false")
# =========================================

# marks=60
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 50:
#     print("C")
# else:
#     print("Fail")
# =========================================

# year = int(input("Enter a year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
# =========================================

# n = 15
# if n % 3 == 0:
#     print("Fizz")
# elif n % 5 == 0:
#     print("Buzz")
# elif n % 15 == 0:
#     print("FizzBuzz")
# else:
#     print(n)
# ====================================================================================================================================================================

# find bugg
# n = 15
# if n % 3 == 0:
#     print("Fizz")
# elif n % 5 == 0:
#     print("Buzz")
# elif n % 15 == 0:
#     print("FizzBuzz")
# else:
#     print(n)
# Why it fails:
# When n = 15:

# Python checks the first if statement: n % 3 == 0. Since 15 is divisible by 3, this condition is True.

# It prints "Fizz" and immediately exits the entire if-elif-else block, skipping everything below it.

# Because the n % 15 == 0 check is placed after the individual checks for 3 and 5, the program will never reach the "FizzBuzz" condition.

# How to fix it:
# To make it work properly, you need to put the most restrictive/strictest condition (n % 15 == 0) first so it gets checked before the individual checks:

# Python
# n = 15

# if n % 15 == 0:
#     print("FizzBuzz")
# elif n % 3 == 0:
#     print("Fizz")
# elif n % 5 == 0:
#     print("Buzz")
# else:
#     print(n)
# ====================================================================================================================================================================



