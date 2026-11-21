# Q11: Find the second highest score using a loop only, without sort() or max().

scores = [45, 82, 67, 91, 73]

highest = None
second_highest = None

for score in scores:
    if highest is None or score > highest:
        second_highest = highest
        highest = score
    elif score != highest and (second_highest is None or score > second_highest):
        second_highest = score

print(second_highest)
