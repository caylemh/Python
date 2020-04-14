# Person - Use a 'dictionary' to store information about a person you know
person_0 = {
	'firstname': 'Caylem',
	'lastname': 'Harris',
	'age': 36,
	'city': 'JHB',
}

for person in person_0: 
    value = person_0[person]
    print(f'{person.title()}: {value}')

print() #Empty Line

# Favourite Numbers - use dictionary to store people's favourite numbers
favorite_nums = {
    'caylem': 7,
    'courtney': 13,
    'juan': 21,
    'ruben': 27,
    'vusi': 12,
}

for person in favorite_nums: 
    value = favorite_nums[person]
    print(f'{person.title()}\'s favorite number is: {value}')

print() #Empty Line

# Glossary - creating a Python Dictionary of terms

glossary = {
    'conditional testing': 'Refers to the common programming pattern where you perform one action, or a different one. It\'s also known as control flow.',
    'for loop': 'A control flow statement for specifying iteration, which allows code to be executed repeatedly.',
    'command': 'An instruction for the computer. Many commands put together make up algorithms and computer programs.',
    'function': 'A piece of code that you can easily call over and over again. Functions are sometimes called \'procedures.\'',
    'variable': 'A placeholder for a piece of information that can change.',
}

print("Please see the definitions for the following programming terms below:\n")

for term in glossary: 
    definition = glossary[term]
    print(f'\t{term.title()}:\n\t\t {definition}\n')