# Q6: Use slicing only to move the first two items of the list to the end.

r = [1, 2, 3, 4, 5]

r = r[2:] + r[:2]

print(r)
