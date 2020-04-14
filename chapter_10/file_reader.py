with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents.rstrip())

# Reading a file line b line
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# Making a list of lines from a file
filename = "pi_digits.txt"
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

# Working with a file's contents
filename = "pi_digits.txt"
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Large Files: One Million Digits
filename = "pi_million_digits.txt"
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()

birthday = input('Enter your birthday, int the form MMDDYY: ')

if birthday in pi_string:
	print('Your birthday appears in the first million digits of pi!')
else:
	print('Your birthday does not appear in the first million digits of pi.')
