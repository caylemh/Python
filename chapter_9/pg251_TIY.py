from random import randint
from random import choice

# --- Dice ---

class Dice:
	"""A class created for a dice with default 'sides' attribute of 6"""
	def __init__(self,sides=6):
		"""Initializing the attributes"""
		self.side = sides

	def roll_die(self):
		""" Getting a random number from randint()"""
		print(f'\nRolling a {self.side}-sided dice:')
		for roll in range(1,11):
			rolled_side = randint(1,self.side)
			print(f'\t- You rolled a {rolled_side}!')

# Create an instance of Dice
# Roll the dice 6 times and print the result
dice1 = Dice()
dice1.roll_die()

# Create an instance of Dice
# Create a 10 sided dice and roll it 10 times
dice2 = Dice(10)
dice2.roll_die()

# Create an instance of Dice
# Create a 20 sided dice and roll it 10 times
dice3 = Dice(20)
dice3.roll_die()


# --- Lottery ---
print('\n--- The Lottery ---')
items = (5,3,7,8,23,55,89,'c','a','p',15,9,1,'f','i')
ticket_nums = []

# Generating 4 random distinct values from the 'items' tuple
while len(ticket_nums) < 4:
	selection = choice(items)
	if selection not in ticket_nums:
		ticket_nums.append(selection)

print('And the winning numbers are...\n\n'
		f'\t{ticket_nums}\n\n'
		'Please check your ticket to see if you\'re the winner!')

# --- Lottery Analysis ---
print('\n--- Lottery Analysis ---\n')
my_ticket = [3,7,'c','f']
numbers=[]
tries = 0

# Generating 4 random values from the 'items' list 
# and storing them in 'numbers' and checking them against 'my_ticket'
# The number of 'tries' have also been recorded.
while True:

	for item in range(1,5):
		selection = choice(items)
		numbers.append(selection)

	if numbers == my_ticket:
		print(f'Prediction: {numbers} == Actual: {my_ticket}')
		print('You have the winning ticket!')
		print(f'\nIt took {tries} tries to get the winner.\n')
		break
	else:
		numbers = []
		tries += 1
		
