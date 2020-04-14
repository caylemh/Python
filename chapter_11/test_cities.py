import unittest
from city_functions import get_formatted_location

class LocationsTestCase(unittest.TestCase):
	"""Tests for the 'city_functions.py'"""

	def test_city_country(self):
		"""Do the city and country like Santiago, Chile work?"""
		format_location = get_formatted_location('santiago','chile')
		self.assertEqual(format_location, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Do Santiago, chile - population: 5000000 work?"""
		format_location = get_formatted_location('santiago','chile',5000000)
		self.assertEqual(format_location, 'Santiago, Chile - Population: 5000000')


if __name__ == '__main__':
	unittest.main()
