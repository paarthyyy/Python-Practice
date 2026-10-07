while True:
  text=input("enter your age :").strip()
  if text.isdigit():
    age = int(text)
    break
  print("please enter a valide number")
is_student=input("are you a student ?(yes / no):").strip().lower()

if age <5:
  price=0
elif age <=18 :
  price=100
else :
  if is_student=="yes":
    price=150
  else:
    price=200
print(f"your ticket price is ${price}")
