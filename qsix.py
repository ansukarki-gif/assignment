student = {
    "name": "ram",
    "age": 19,
    "course": "BCA",
    "marks": 78
    }

print("Student Information:")
print(student)

student["marks"] += 5

if student["marks"]>=40:
    student["status"] = "pass"
else:
    student["status"]="fail"
    print("Updated Dictionary:")
    print(student)

