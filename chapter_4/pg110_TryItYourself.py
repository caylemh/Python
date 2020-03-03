# Counting to Twenty - using a 'for' loop
for value in range(21):
	print(value)

# One Million - making a list to contain the numbers from 1 to 1000000
numbers = list(range(1,1000001))
print(numbers)

# Summing a Million - using the min(), max() and sum() functions
print(f'\nThe smallest number in the list is: {min(numbers)}')
print(f'The largest number in the list is: {max(numbers)}')
print(f'The sum of all the numbers in the list is: {sum(numbers)}\n')

# Odd Numbers - using the third argument in the range() function
for odd_num in range(1,21,2): print(odd_num)
print("")

# Threes - making a list of the multiples of 3 from 3 to 30 using a 'for' loop to print them
for value in range(3,31,3): print(value)


# Cubes - numbers raised to the power of 3
cubes = []
for value in range(1,11):
	cubes.append(value**3)
print(f'\n{cubes}\n')

# Cube Comprehension
cubes = [value**3 for value in range(1,11)]
print(f'\n{cubes}\n')