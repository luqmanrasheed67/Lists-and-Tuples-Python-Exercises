# Q10: Print each student's score, find the topper, and make a list of students who passed with 70 marks or above.

students = [("Ali", 85), ("Sara", 92), ("Ahmed", 76), ("Hina", 64)]

for name, marks in students:
    print(f"{name} scored {marks}.")

topper = students[0]
for student in students:
    if student[1] > topper[1]:
        topper = student

passed_students = [name for name, marks in students if marks >= 70]

print("topper", topper[0], topper[1])
print(passed_students)
