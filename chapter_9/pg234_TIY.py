# Number Served

# Restaurant
class Restaurant:
	"""Modeling a restaurant"""
	def __init__(self,restaurant_name,cuisine_type):
		"""Initialize the restaurant name and cuisine type attributes"""
		self.restaurant = restaurant_name
		self.cuisine = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Print the restaurant name and cuisine type"""
		print(f'\nThe restaurant\'s name is: {self.restaurant.title()}\n'
				f'and they specialise in {self.cuisine.title()} cuisine.')

	def open_restaurant(self):
		print(f'{self.restaurant.title()} is OPEN for business!')

	def read_served(self):
		print(f'\n{self.restaurant.title()} has served {self.number_served} customers. Wow!')

	def set_number_served(self,num_customers):
		""" Adding the given amount to num_customers"""
		self.number_served = num_customers

	def increment_served(self,served):
		"""Add more customers to number_served everytime this method is called"""
		self.number_served += served
		print(f'\n{self.restaurant.title()} has served {self.number_served} customers today. Thank you!\n')


restaurant1 = Restaurant('mugg & bean','american bistro')
restaurant1.number_served = 154

restaurant1.describe_restaurant()
restaurant1.read_served()

# Changing the value and printing
restaurant1.number_served = 205
restaurant1.read_served()

# Calling the method and passing the parameters
restaurant1.set_number_served(335)
restaurant1.read_served()
restaurant1.increment_served(300)


# Login Attempts
# Users
class User:
	"""Modeling a User Profile"""
	def __init__(self,first_name,last_name,gender,race,m_status,profession):
		"""Initialize all the relevant attributes"""
		self.f_name = first_name
		self.l_name = last_name
		self.status = m_status
		self.prof = profession
		self.gender = gender
		self.race = race
		self.login_attempts = 0

	def greet_user(self):
		"""Print a personalised welcome message"""
		print(f'\nWelcome {self.f_name.title()} great to have you back!')

	def describe_user(self):
		"""Print the user's profile"""
		print(f'\nUser Info Summary:\n'
				f'\tFirst Name:\t\t{self.f_name.title()}\n'
				f'\tLast Name:\t\t{self.l_name.title()}\n'
				f'\tGender:\t\t\t{self.gender.upper()}\n'
				f'\tRace:\t\t\t{self.race.title()}\n'
				f'\tMarital Status:\t{self.status.title()}\n'
				f'\tProfession:\t\t{self.prof.title()}'
				)

	def read_login_attempts(self):
		print(f'\n\tUnsuccessful login attempts: {self.login_attempts}')

	def increment_login_attempts(self,attempt):
		self.login_attempts += attempt

	def reset_login_attempts(self):
		self.login_attempts = 0
		print(f'\n\tYou login attempts have been reset to: {self.login_attempts}')

user1 = User('anna','levine','f','caucasian','single','developer')

user1.greet_user()
user1.describe_user()
user1.increment_login_attempts(1)
user1.increment_login_attempts(5)
user1.read_login_attempts()
user1.reset_login_attempts()