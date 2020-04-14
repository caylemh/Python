# Deli
print('\n--- Order your sandwich right here!!! ---\n')

sandwich_orders = ['new york bagel', 'ham dagwood', 'grilled cheese & onion']
finished_sandwiches = []

active = True

while sandwich_orders:
	# Remove sandwiches from the original list
	sandwich = sandwich_orders.pop()
	print(f'I have just finished your \'{sandwich.title()}\' sandwich. Enjoy!')

	# Add sandwiches to new list
	finished_sandwiches.append(sandwich)

# Print the completed sandwiches
print('\nThese are the completed sandwiches:')
for finished in finished_sandwiches:
	print(f'\t{finished.title()}')


# No Pastrami
print('\n--- Order your sandwich right here!!! ---\n')

sandwich_orders = ['new york bagel', 'pastrami', 'ham dagwood', 'pastrami', 'grilled cheese & onion', 'pastrami']
finished_sandwiches = []

# Delete 'pastrami' orders from list
print('Sorry everyone, we have run out of Pastrami!\n')
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

active = True

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f'I have just finished your \'{sandwich.title()}\' sandwich. Enjoy!')

	finished_sandwiches.append(sandwich)

# Print the completed sandwiches
print('\nThese are the completed sandwiches:')
for finished in finished_sandwiches:
	print(f'\t{finished.title()}')


#Dream Vacation
print('\n--- Poll users about their dream vacation ---')
# Create an empty dictionary
responses = {}

polling_active = True

while polling_active:
	# Prompt user for the values
	name = input('\nPlease enter your name: ')
	location = input('If you could visit one place in the world, where would you go?')

	#Store the values in your dictionary
	responses[name] = location

	# Find out of the user wants to store more values
	repeat = input('\nWould another person like to respond? (yes/no)?')
	if repeat == 'no':
		polling_active = False

# Polling is now complete, show the responses
print('\n--- Thank you for partiipating in the poll. Here are the results: ---\n')
for name, response in responses.items():
	print(f'{name.title()} would like to visit {response.title()} if the opportunity presented itself!')


