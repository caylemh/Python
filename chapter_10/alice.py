# Analyzing Text

def count_words(filename):
	"""Count the approximate number of words in a file"""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f'\n- Sorry, the file \'{filename}\' does not exist.')
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print(f'\nThe file {filename} has about {num_words} words.')

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)