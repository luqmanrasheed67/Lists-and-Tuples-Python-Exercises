# Q2: Print the total, average, highest, lowest marks, and count how many marks are above 70 using a loop.

marks = [78, 92, 65, 88, 54]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

above_70 = 0
for mark in marks:
    if mark > 70:
        above_70 += 1

print(total)
print(average)
print(highest)
print(lowest)
print(above_70)
