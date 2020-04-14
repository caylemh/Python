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

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# Assigning a value directly to the attribute
my_new_car.odometer_read = 23

# Using a method to assign the value to the attribute
my_new_car.update_odometer(40)

# Caliing the method
my_new_car.read_odometer()

# New instance
my_used_car1 = Car('subaru','outback',2015)
print(my_used_car1.get_descriptive_name())

my_used_car1.update_odometer(23_500)
my_used_car1.read_odometer()

my_used_car1.increment_odometer(100)
my_used_car1.read_odometer()