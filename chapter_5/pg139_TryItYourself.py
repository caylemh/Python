# Alien Colors
alien_color = 'green'

# testing if alien_color == 'green'
if 'green' in alien_color:
	print('You have just earned 5 point!!!\n')

'''Another version of the program where if the condition isn't met
	there would be no out put
''' 
if 'orange' in alien_color:
	print('You have just earned 5 point!!!\n')
else:
	print()

# Alien Colors #2 - write an if-else chain

alien_color = 'orange'	#Alien is 'orange'

# Running the 'if' block
if 'orange' in alien_color:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 10 points!!!\n')
else:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 5 points!!!\n')

# Running the 'else' block
alien_color = 'green'	#Alien is 'green'

if 'orange' in alien_color:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 10 points!!!\n')
else:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 5 points!!!\n')

# Alien Color #3 - usinf the if-elif-else chain
alien_color = 'green'	#Alien is 'green'

if 'green' in alien_color:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 5 points!!!\n')
elif 'yellow' in alien_color:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 10 points!!!\n')
else:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 15 points!!!\n')

alien_color = 'yellow'	#Alien is 'yellow'

if 'green' in alien_color:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 5 points!!!\n')
elif 'yellow' in alien_color:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 10 points!!!\n')
else:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 15 points!!!\n')

alien_color = 'red'	#Alien is 'red'

if 'green' in alien_color:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 5 points!!!\n')
elif 'yellow' in alien_color:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 10 points!!!\n')
else:
	print(f'Because the alien\'s color is: {alien_color.title()}, You have earned 15 points!!!\n')


# Stages of Life - if-elif-else chain that determines a person's stage in life
person_age = 23
print(f'Hi there, you are {person_age} years old...')

if person_age < 2:
	print('You are probably an infant.\n')
elif person_age >= 2 and person_age < 4:
	print('You are probably a toddler.\n')
elif person_age >= 4 and person_age < 13:
	print('You are probably a kid.\n')
elif person_age >= 13 and person_age < 20:
	print('You are probably a teenager.\n')
elif person_age >= 20 and person_age < 65:
	print('You are probably an adult.\n')
else:
	print('You are probably an elderly person.\n')

# Favourite Fruits list and using 'if' statements
favourite_fruits = ['guava', 'orange', 'banana']

if 'guava' in favourite_fruits:
	print(f'You really like {favourite_fruits[0].title()}\'s!\n')

if 'orange' in favourite_fruits:
	print(f'You really like {favourite_fruits[1].title()}\'s!\n')

if 'banana' in favourite_fruits:
	print(f'You really like {favourite_fruits[2].title()}\'s!\n')

if 'grapes' in favourite_fruits:
	print(f'You really like {favourite_fruits[3].title()}\'!\n')

if 'apple' in favourite_fruits:
	print(f'You really like {favourite_fruits[4].title()}\'s!\n')
