
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