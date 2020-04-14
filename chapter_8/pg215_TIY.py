# Sandwiches
def sandwich(*items):
	'''printing te items'''
	print('\nSandwiches:')
	for item in items:
		print(f'\t- {item.title()}')

# Calling the function 3 times with varying arguments passed
sandwich('bagel','cheese & tomato','chicken & mayonaisse')
sandwich('cheese & onion','grilled bagel')
sandwich('rye & tofu')


#User Profiles
(print('\nUser Profiles Exercise'))

def build_profile(first, last,**user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert','einstein',
				location='princeton',
				field='physics')

my_profile = build_profile('caylem','harris',
				location='eldorado park',
				field='programming',
				marital_status='married'
				)

print(user_profile)
print(my_profile)


# Cars
print('\nA Dictionary for car information')
def car_info(manuf,model,**other):
	"""Creating a dictionary about cars"""
	other['manufacturer'] = manuf
	other['model'] = model
	return other

car = car_info('ford','focus st',
				color='red',
				feature='performance package',
				)

car1 = car_info('subaru','impreza sti',
				color='royal blue',
				feature='rally package',
				)

print(car)
print(car1)