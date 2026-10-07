name = input()
age = input()
course = input()
exam_id = input()
if name == "":
    print("Error: name cannot be empty")
elif not age.isdigit():
    print("Error: age must be a whole number")
elif not (16 <= int(age) <= 60):
    print("Error: age must be between 16 and 60")
elif course not in ["CSE", "ECE", "MECH"]:
    print("Error: invalid course code")
elif not (exam_id.isdigit() and len(exam_id) == 4):
    print("Error: exam ID must be exactly 4 digits")
else:
    print(f"Registration confirmed for {name}")