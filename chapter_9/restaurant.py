class Restaurant:
	"""Modeling a restaurant"""
	def __init__(self,restaurant_name,cuisine_type):
		"""Initialize the restaurant name and cuisine type attributes"""
		self.restaurant = restaurant_name
		self.cuisine = cuisine_type

	def describe_restaurant(self):
		"""Print the restaurant name and cuisine type"""
		print(f'\nThe restaurant\'s name is: {self.restaurant.title()}\n'
				f'and they specialise in {self.cuisine.title()} cuisine.')

	def open_restaurant(self):
		print(f'{self.restaurant.title()} is OPEN for business!')

class IceCreamStand(Restaurant):
	"""Represents all aspects of a Restaurant but specific to an IceCreamStand"""
	def __init__(self,restaurant_name,cuisine_type='ice cream'):
		"""Initialize attributes of the parent class"""
		super().__init__(restaurant_name,cuisine_type)

		self.flavours = []

	def describe_flavours(self):
		"""Prints the flavours"""
		print('\nWe have the following flavours available:')
		for flavour in self.flavours:
			print(f'\t- {flavour.title()}')

	def describe_restaurant(self):
		"""Print the restaurant name and cuisine type"""
		print(f'\nThe restaurant\'s name is: {self.restaurant.title()}\n'
				f'and they specialise in {self.cuisine.title()}')