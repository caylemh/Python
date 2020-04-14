def get_formatted_location(city,country, population=''):
	"""Print the city and country together, nicely formatted"""
	if population:
		location = f'{city}, {country} - population: {population}'
	else:
		location = f'{city}, {country}'

	return location.title()