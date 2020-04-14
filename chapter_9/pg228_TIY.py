
# Restaurant
class Restaurant():
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

# Create one intance of Restaurant
rest1 = Restaurant('romans pizza','italian')

rest1.describe_restaurant()
rest1.open_restaurant()

# Create a second instance of Restaurant
rest2 = Restaurant('mugg & bean','american bistro')

rest2.describe_restaurant()
rest2.open_restaurant()

# Create a third instance of Restaurant
rest3 = Restaurant('le freak','french')
rest3.describe_restaurant()
rest3.open_restaurant()


# Users
class User():
	"""Modeling a User Profile"""
	def __init__(self,first_name,last_name,gender,race,m_status,profession):
		"""Initialize all the relevant attributes"""
		self.f_name = first_name
		self.l_name = last_name
		self.status = m_status
		self.prof = profession
		self.gender = gender
		self.race = race

	def greet_user(self):
		"""Print a personalised welcome message"""
		print(f'\nWelcome {self.f_name.title()} great to have you back!')

	def describe_user(self):
		"""Print the user's profile"""
		print(f'User Info Summary:\n'
				f'\tFirst Name:\t\t{self.f_name.title()}\n'
				f'\tLast Name:\t\t{self.l_name.title()}\n'
				f'\tGender:\t\t\t{self.gender.upper()}\n'
				f'\tRace:\t\t\t{self.race.title()}\n'
				f'\tMarital Status:\t{self.status.title()}\n'
				f'\tProfession:\t\t{self.prof.title()}'
				)

# Instance 1
user1 = User('anna','levine','f','caucasian','single','developer')

user1.greet_user()
user1.describe_user()

# Instance 2
user2 = User('john','melvick','m','coloured','mareied','salesman')

user2.greet_user()
user2.describe_user()

# Instance 3
user3 = User('lorey','cusack','f','asian','divorced','haridresser')

user3.greet_user()
user3.describe_user()