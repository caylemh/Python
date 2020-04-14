# Rental Car - Execute this code in your console
prompt = 'What type of car would you like to rent?'

car = input(prompt)# Asking the user for input to the question

print(f'Let me see if I can find a {car} for you!\n')


# Restaurant Seating
prompt = 'How many people are in your dinner group?'
table = int(input(prompt))

if table >= 8:
	print('Sorry , but you will have to wait for a table!')
else:
	print('Your table is ready!')


#Multiples of 10
prompt = 'Please enter a number?'
report = int(input(prompt))

if report % 10 == 0:
	print('This number is a multiple of 10!')
else:
	print('This number is not a multiple of 10!')