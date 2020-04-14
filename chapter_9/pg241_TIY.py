# --- Restaurant ---
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

# Creating an instance of the new IceCreamStand class
icecream1 = IceCreamStand('soft serve')
icecream1.flavours = ['smooth vanilla','crisp mint','decadent chocolate','salty caramel']

icecream1.describe_restaurant()
icecream1.describe_flavours()


# --- Admin ---
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

class Admin(User):
	"""Represents all aspects of a User but specific to an Administrator"""
	def __init__(self,first_name,last_name,gender,race,m_status,profession):
		"""Initialize attributes of the parent class"""
		super().__init__(first_name,last_name,gender,race,m_status,profession)

		self.priviledges = ['can add a post','can delete a post', 'can ban a user']

	def show_priviledges(self):
		print(f'\n{self.f_name.title()} has the following Administrator priviledges:')
		for priviledge in self.priviledges:
			print(f'\t- {priviledge.title()}')


# Instance 1
user1 = User('anna','levine','f','caucasian','single','developer')
user3 = Admin('lorey','cusack','f','asian','divorced','haridresser')
user3.describe_user()
user3.show_priviledges()


# --- Addition of a Priviledges Class ---
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
		self.priviledges = Priviledges()

	def greet_user(self):
		"""Print a personalised welcome message"""
		print(f'\nWelcome {self.f_name.title()} great to have you back!')

	def describe_user(self):
		"""Print the user's profile"""
		print(f'\n--- User Info Summary: ---\n'
				f'\tFirst Name:\t\t{self.f_name.title()}\n'
				f'\tLast Name:\t\t{self.l_name.title()}\n'
				f'\tGender:\t\t\t{self.gender.upper()}\n'
				f'\tRace:\t\t\t{self.race.title()}\n'
				f'\tMarital Status:\t{self.status.title()}\n'
				f'\tProfession:\t\t{self.prof.title()}'
				)

class Admin(User):
	"""Represents all aspects of a User but specific to an Administrator"""
	def __init__(self,first_name,last_name,gender,race,m_status,profession):
		"""Initialize attributes of the parent class"""
		super().__init__(first_name,last_name,gender,race,m_status,profession)

		self.priviledges = Priviledges()


class Priviledges:
	"""Modeling a priviledges class"""
	def __init__(self,priviledges=[]):
		"""Initializing the attributes"""
		self.priviledges = priviledges

	def show_priviledges(self):
		"""Checking priviledges"""
		print(f'\nThis User has the following Administrator priviledges:')
		if self.priviledges:
			for priviledge in self.priviledges:
				print(f'\t- {priviledge.title()}')
		else:
			print(f'\t- No priviledges assigned!')

# Instance 1: User
user1 = User('anna','levine','f','caucasian','single','developer')
user1.describe_user()
user1.priviledges.show_priviledges()


# Instance 2: Admin
user3 = Admin('lorey','cusack','f','asian','divorced','hairdresser')
user3.describe_user()
user3.priviledges.show_priviledges()

print('\nAdding priviledges...')

user3_priviledges = ['can add a post','can delete a post','can ban a user']
user3.priviledges.priviledges = user3_priviledges

user3.priviledges.show_priviledges()


# --- Battery Upgrade ---
class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_read = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"\n{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage"""
		print(f'This car has {self.odometer_read} miles on it.')

	def update_odometer(self,mileage):
		"""Set odometer reading to the given value.
			Reject the change if it attempts to roll the odometer back."""
		if mileage >= self.odometer_read:
			self.odometer_read = mileage
		else:
			print('You cannot roll back an odometer!')

	def increment_odometer(self,miles):
		"""Add the given amount to the odometer."""
		self.odometer_read += miles

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

class Battery:
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		
		print(f"\t- This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		"""Setting different values for the attributes"""
		if self.battery_size == 75:
			self.battery_size = 100
			print('\n Your battery has been upgraded to a capacity of 100 kWh...')
		else:
			print('\n Your battery has already been upgraded. Thank you!')

# Create an instance of the ElectricCar class
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()