''' Pizza Topping - asking the user to enter avalue and displaying it until
 'quit' is typed.
 '''
print('\n--- Order your Pizza here!!! ---')
prompt = "\nPlease enter your Pizza topping:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(f'We\'re adding {message.title()} to your pizza!')

# Movie Tickets
print('\n--- Get your Movie Tickets here!!! ---')

prompt = 'Please enter your age to determine ticket prices.'
prompt += '\nEnter \'0\' to quit:'
active = True

while active:
	age = int(input(prompt))

	if age == 0:
		active = False
	elif age > 0 and age < 3:
		print('You are FREE to enter! WooHoo!')
		continue
	elif age >= 3 and age < 12:
		print('The ticket will cost $10!')
		continue
	else:
		print('The ticket will cost $15!')
		continue

# Infinity Loop
print('\n--- An Infinite Loop ---')

num = 3

while num < 4:
	print('To infinity and beyond...')
	