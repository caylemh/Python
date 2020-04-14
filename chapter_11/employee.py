class Employee:
	"""Stores details of an Employee"""

	def __init__(self,first_name,last_name, annual_salary):
		"""Initializing theattributes to be used"""
		self.f_name = first_name.title()
		self.l_name = last_name.title()
		self.a_salary = annual_salary

	def give_raise(self, amount=5000):
		self.a_salary += amount
