# Input all external modules
from priviledges import *
from user import User

class Admin(User):
	"""Represents all aspects of a User but specific to an Administrator"""
	def __init__(self,first_name,last_name,gender,race,m_status,profession):
		"""Initialize attributes of the parent class"""
		super().__init__(first_name,last_name,gender,race,m_status,profession)

		self.priviledges = Priviledges()