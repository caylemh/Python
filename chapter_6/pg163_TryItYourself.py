# Glossary - creating a Python Dictionary of terms

glossary = {
    'conditional testing': 'Refers to the common programming pattern where you perform one action, or a different one. It\'s also known as control flow.',
    'for loop': 'A control flow statement for specifying iteration, which allows code to be executed repeatedly.',
    'command': 'An instruction for the computer. Many commands put together make up algorithms and computer programs.',
    'function': 'A piece of code that you can easily call over and over again. Functions are sometimes called \'procedures.\'',
    'variable': 'A placeholder for a piece of information that can change.',
}

# Adding 5 more glossary terms to the dictionary

glossary['data'] = 'Information. Often, quantities, characters, or symbols that are the inputs and outputs of computer programs.'
glossary['debugging'] = 'Finding and fixing errors in programs.'
glossary['function call'] = 'The piece of code that you add to a program to indicate that the program should run the code inside a function at a certain time.'
glossary['parameter'] = 'An extra piece of information that you pass to the function to customize it for a specific need.'
glossary['python'] = 'Python is a widely used general-purpose, high-level programming language.'

print("Please see the definitions for the following programming terms below:\n")

for term in glossary: 
    definition = glossary[term]
    print(f'\t{term.title()}:\n\t\t {definition}\n')


# Rivers - make a dictionary containing 3 major rivers

rivers = {'nile': 'egypt', 'zambezi': 'africa', 'mekong': 'china'}

# A loop printing a sentence about each river.
for river in rivers: 
    country = rivers[river].title()
    print(f'The {river.title()} river runs through {country}\n')

# A loop to print each river
print('The Rivers:')
for river in rivers: 
    print(f'\t{river.title()}')

# A loop to print each country
print('\nThe Countries:')
for river in rivers.values(): 
    print(f'\t{river.title()}')


# Polling - code used on pg 97 (favourite_languages.py)
print('\nThese are the Poll results:\n')

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

new_people = ['andrew', 'clayton', 'jen', 'hadley', 'edward']

for person in new_people:
	
	if person in favorite_languages:
		print(f'\tThank you {person.title()}, for responding & taking our poll!\n\tYou Rock!!!\n')
	else:
		print(f'\tHi {person.title()}, have you taken our poll?\n\tPlease do so now. Thank you!\n')
