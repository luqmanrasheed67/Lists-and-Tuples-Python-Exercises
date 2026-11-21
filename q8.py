# Q8: Unpack the student tuple, show the error from trying to change it, then update the marks by converting it to a list and back to a tuple.



student = ("BSIT-12", "Sara", 88)

roll_no, name, marks = student

print(f"Roll No: {roll_no}")
print(f"Name: {name}")
print(f"Marks: {marks}")

student[2] = 95

student_list = list(student)
student_list[2] = 95
student = tuple(student_list)

print(student)
