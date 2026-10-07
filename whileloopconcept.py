# a=5
# while a>0:
#   print(a)
#   a-=1
# print()
# for a in range (5,0,-1):
#   print(a)

n=input()
digit_sum=0
while n>0:
  rem=n%10
  digit_sum+=rem
  n=n//10
print(digit_sum)