# -- T-Shirt --
def make_shirt(size,text):
	''' function that accepts parameters for 'size' and 'text' to be displayed '''
	print(f'Your shirt size is: {size.title()}\n'
			f'The message to be printed on the T-Shirt is:\n\t {text}\n'
			)
# Call the function ith arguments
make_shirt('m','I love Python!!!')


# -- Large Shirts --
def make_shirt(text,size='large'):
	''' function that accepts parameters for 'size' and 'text' to be displayed '''
	print(f'Your shirt size is: {size.title()}\n'
			f'The message to be printed on the T-Shirt is:\n\t {text}\n'
			)
# Call the function ith arguments
make_shirt(text='I love Python!!!')
make_shirt('Happy Birthday! Not!', 'medium')

# -- Cities --
def describe_city(city, country='peru'):
	print(f'{city.title()} is in {country.title()}.')

describe_city('agrat')
describe_city('ishian')
describe_city('tian','china')