import unittest
from employee import Employee

class RaiseTestCase(unittest.TestCase):
	"""Test for the class Employee"""

	def setUp(self):
		"""Create an instance of the Employee class"""
		self.emp1 = Employee('gary','stone',10000)

	def test_give_default_raise(self):
		"""Test whether the default amount would work"""
		self.emp1.give_raise()
		self.assertEqual(self.emp1.a_salary, 15000)

	def test_give_custom_raise(self):
		self.emp1.give_raise(8000)
		self.assertEqual(self.emp1.a_salary, 18000)

if __name__ == '__main__':
	unittest.main()