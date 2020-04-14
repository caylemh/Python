# People - Create a list(people) of dictionaries (person_*) and display them

print('People and their info:')	
person_0 = {
	'firstname': 'Caylem',
	'lastname': 'Harris',
	'age': 36,
	'city': 'JHB',
	}

person_1 = {
	'firstname': 'Courtney',
	'lastname': 'Alexander',
	'age': 17,
	'city': 'JHB',
	} 

person_2 = {
	'firstname': 'Tatenda',
	'lastname': 'Kumbula',
	'age': 18,
	'city': 'JHB',
	}

people = [person_0, person_1, person_2]

for person in people: 
    print(f'\t{person}')


# Pets - Create a list(pets) of dictionaries (animal_*) and display them
print('\nPets and their owners:')

animal_0 = {
	'type': 'cat',
	'owner': 'angie',
}

animal_1 = {
	'type': 'dog',
	'owner': 'tatenda',
}

animal_2 = {
	'type': 'monkey',
	'owner': 'ruben',
}

pets = [animal_0, animal_1, animal_2]

for animal in pets:
	print(f'\t{animal}')


''' Favourite Places - making a list(places) for each key(person) in the dictionary
						(favourite places) '''
print('\nPeople and their favourite places:')

favorite_places = {
	'caylem': ['peru', 'bora bora'],
	'mpho': ['lagos'],
	'juan': ['antigua bay', 'seychelles', 'taiwan'],
}

for person, locations in favorite_places.items():
	if len(locations) < 2:
		print(f'\n\t{person.title()}\'s favourite location is: ')
	else:
		print(f'\n\t{person.title()}\'s favourite locations are: ')

	for location in locations:
		print(f'\t\t{location.title()}')


# Favourite Numbers
print('\nPeople and their favourite numbers:')
favorite_nums = {
    'caylem': [7,8,10],
    'courtney': [13,16,33],
    'juan': [21,5],
    'ruben': [27,17],
    'vusi': [12,24,30],
}

for person, numbers in favorite_nums.items(): 
    print(f'\n\t{person.title()}\'s favourite numbers are: ')
    for number in numbers:
    	print(f'\t\t{number}')


# Cities
print('\nCities and their information:')

cities = {
	'lima': {'country': "peru", 'population':40000, 'fact': 'Three-quarters '
			'of the world\'s alpaca population lives in Peru. The national animal is\n'
			'\t\t\tthe vicuna, a small camelid similar to the alpaca. It comes in 22 natural\n'
			'\t\t\tcolors and its wool is considered the world\'s most luxurious fabric.',
    		},
    'victoria': {'country': 'seychelles', 'population':98000, 'fact': 'Some of '
    			'the rarest species of birds can be found in Seychelles, including the\n'
    			'\t\t\tbare-legged Scops Owl or Syer.',
    			},
    'abuja': {'country': 'nigeria', 'population':201000, 'fact': 'The country\'s'
    		' film industry, known as Nollywood, is one of the largest film producers\n'
    		'\t\t\tin the world, second only to India\'s Bollywood.',
    		},
    	}


for city, info in cities.items(): 
    
    country = info['country'].upper()
    population = info['population']
    fact = info['fact']

    print(f'\n\tWelcome to {city.title()}, in {country}.\n')
    print(f'\tPopulation:\t{population}')
    print(f'\n\tFact:\t{fact}.\n')


# Extensions
print('\nExtending the \'favourite_languages.py\' program:')

favorite_languages = {
	'jen': {
		'language': ['python', 'c++'],
		'experience': 8,
		},
	'sarah': {
		'language': ['ruby'],
		'experience': 5,
		},
	'edward': {
		'language': ['c++'],
		'experience': 2,
		},
	'phil': {
		'language': ['python', 'ruby'],
		'experience': 6,
		},
	}

for name, lang_info in favorite_languages.items():
	language = lang_info['language']
	exp = lang_info['experience']

	if len(language) < 2:
		print(f'\n{name.title()}\'s favorite language is:')
	else:
		print(f'\n{name.title()}\'s favorite languages are:')

	print(f'\tLanguage:\t{language}')
	print(f'\tExperience:\t{exp}')