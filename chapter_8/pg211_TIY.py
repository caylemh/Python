
# Messages
def show_messages(messages):
	''' print a message '''
	for msg in messages:
		print(f'{msg}')

msgs = ['Hello!', 'I love you!', 'Please leave me alone!']

# Calling the function with a list passed as an argument
show_messages(msgs)

print() #Empty line

# Sending Messages
def send_messages(show_messages,sent_messages):
	''' make a list of sent messages and print '''
	while show_messages:
		message = msgs.pop()
		sent_messages.append(message)

def show_messages(messages):
	''' print a message '''
	for msg in sent_msgs:
		print(f'{msg}')

msgs = ['Hello!', 'I love you!', 'Please leave me alone!']
sent_msgs = []

# Calling the function with a list passed as an argument
send_messages(msgs,sent_msgs)
show_messages(msgs)


# Archived Messages
def send_messages(show_messages,sent_messages):
	''' make a list of sent messages and print '''
	while show_messages:
		message = show_messages.pop()
		sent_messages.append(message)

def show_messages(messages):
	''' print a message '''
	for msg in messages:
		print(f'{msg}')

msgs = ['Hello!', 'I love you!', 'Please leave me alone!']
sent_msgs = []

# sending a copy of my list to the function
send_messages(msgs[:],sent_msgs)
# Calling the function with a list passed as an argument
print('Thi is the created list.')
show_messages(sent_msgs)

print() #Empty line

# printing the original list to show that it hasn't been overwritten
print('This is the original list')
show_messages(msgs)