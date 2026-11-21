# Q4: Create a new list without duplicates, keep the original order, and use a loop with not in instead of set().

nums = [3, 1, 3, 2, 1, 5]
unique_nums = []

for number in nums:
    if number not in unique_nums:
        unique_nums.append(number)

print(unique_nums)
