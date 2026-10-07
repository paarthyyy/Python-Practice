password = input()

upper = 0
lower = 0
digit = 0
special = 0

for char in password:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    else:
        special += 1

categories = 0
if upper > 0:
    categories += 1
if lower > 0:
    categories += 1
if digit > 0:
    categories += 1
if special > 0:
    categories += 1

length = len(password)
if length >= 8 and categories == 4:
    strength = "Strong"
elif length >= 6 and categories >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special:", special)
print("Strength:", strength)