student = {
    "name": "Paarth", #name of the student
    "age": 17,        #age of the student
    "marks": 85       #marks obtained by the student
}
print(student["name"])
print(student["age"])
print(student["marks"])

if "age" in student: #a check to see if the key "age" exists in the student dictionary
    print("Age exists")