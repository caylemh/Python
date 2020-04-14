class Settings:
	"""A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (59, 59, 59)

		# Ship settings
		self.ship_speed = 1.5
		self.ship_limit = 3

		#Bullet settings
		self.bullet_speed = 1.2
		self.bullet_width = 4
		self.bullet_height = 18
		self.bullet_color = (200,60,0)
		self.bullets_allowed = 3

		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 20

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		# How quickly the alien values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 1.2
		self.alien_speed = 1.0

		#Scoring
		self.alien_points = 50

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

	def increase_speed(self):
		"""Increase the speed settings and alien point values"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		# print(self.alien_points)