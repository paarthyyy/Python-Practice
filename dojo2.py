a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
per = (a + b + c + d + e) / 5
if per >= 90:
    print("Grade A")
elif per >= 80:
    print("Grade B")
elif per >= 70:
    print("Grade C")
elif per >= 60:
    print("Grade D")
else:
    print("Fail")