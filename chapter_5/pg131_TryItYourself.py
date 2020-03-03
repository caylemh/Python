# Conditional Tests - Write a sereis of conditional tests
car1 = 'audi'
car2 = 'bmw'

print('Is car1 == audi? I predict: True')
print(car1 =='audi')

print('\nIs car1 == subaru? I predict: False')
print(car1 =='subaru')

print('\nIs car1 != audi? I predict: False')
print(car1 !='audi')

print('\nIs car1 != bmw? I predict: True')
print(car1 !='bmw')

print('\nIs audi in car1? I predict: True')
print('audi' in car1)

print('\nIs audi not in car1? I predict: False')
print('audi' not in car1)

print('\nIs car1 and car2 equal? I predict: False')
print(car1 == car2)

print('\nIs car1 and car2 not equal? I predict: True')
print(car1 != car2)

print('\nIs car1 or car2 equal to audi? I predict: True')
print(car1 == 'audi' or car2 == 'audi')

print('\nIs car1 and car2 equal to bmw? I predict: False')
print(car1 == 'bmw' and car2 == 'bmw')

print('\nIs car1 equal to audi and car2 equal to bmw? I predict: True')
print(car1 == 'audi' and car2 == 'bmw')

# More Conditional tests

# Testing for equality & inequality with strings
color = 'yellow'
print('\nIs the color \'blue\'? I predict: False')
print(color=='blue')

print('\nIs the color \'yellow\'? I predict: True')
print(color=='yellow')

# Tests using the 'lower' method
color = 'Red'
print(f'\nThe color is: {color}')
print('Is the color \'red\'? I predict: False')
print(color=='red')

print('\nIs the color \'red\' using the "lower" method? I predict: True')
print(color.lower()=='red')

''' Numerical tests for equality, inequality, greater than & less than,
greater than or equal to, and less than or equal to.
'''
x = 5
y = 10
print('\nIs x equal to y? I predict: False')
print(x==y)

print('\nIs x not equal to y? I predict: True')
print(x!=y)

print('\nIs x greater than y? I predict: False')
print(x>y)

print('\nIs x less than y? I predict: True')
print(x<y)

print('\nIs x greater than or equal to y? I predict: False')
print(x>=y)

print('\nIs x less than or equal to y? I predict: True')
print(x<=y)

print('\nIs x greater than or equal to 5? I predict: True')
print(x>=5)

print('\nIs y less than or equal to 10? I predict: True')
print(x<=y)

# Tests using 'and' and 'or'

print('\nIs x = 5 and y = 10? I predict: True')
print(x == 5 and y == 10)

print('\nIs x = 8 and y = 10? I predict: False')
print(x == 8 and y == 10)

print('\nIs x = 8 or y = 10? I predict: True')
print(x == 8 or y == 10)

print('\nIs x = 8 or y = 20? I predict: False')
print(x == 8 and y == 20)

# Test  whether an item is in a list

foods = ['pineapple','guava','mango']
item = 'guava'

print('Checking if "guava" is in the list? I predict: True')
if item in foods: 
    print('True') 
else: 
    print('False')


print('Checking if "guava" is not in the list? I predict: False')
if item not in foods: 
    print('True') 
else: 
    print('False')

