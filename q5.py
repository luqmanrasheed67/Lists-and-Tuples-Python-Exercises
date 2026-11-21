# Q5: Use list comprehension to make separate lists of even and odd numbers from 1 to 15.

numbers = range(1, 16)

even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print(even_numbers)
print(odd_numbers)
