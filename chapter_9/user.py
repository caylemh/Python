from priviledges import *

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