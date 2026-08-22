print("Simple Calculator")
a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
c=input("Enter an operator (+, -, *, /): ")
if c=='+':
    print(a, "+", b, "=", a + b)
elif c=='-':
    print(a, "-", b, "=", a - b)
elif c=='*':
    print(a, "*", b, "=", a * b)
elif c=='/':
    if b==0:
        print("Cannot divide by zero.")
    else:
        print(a, "/", b, "=", a / b)
else:
    print("Invalid operator")