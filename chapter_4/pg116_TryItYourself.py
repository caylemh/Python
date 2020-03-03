
# Slices - using one the existing programs to display what 'slices' do
cubes = []
for value in range(1,11):
	cubes.append(value**3)
print(f'\n{cubes}\n')

print(f'The first three items in the "cubes" list are: {cubes[:3]}')
print(f'The first three items from the middle of the "cubes" list are: {cubes[4:7]}')
print(f'The last three items in the "cubes" list are: {cubes[-3:]}\n\n')

# My Pizzas, Your Pizzas - using 'slices' to create an independant copy of a list
pizzas = ['marguerita','pepperoni','chicken tikka','something meaty']

for pizza in pizzas:
	print(pizza.title())
	print(f'I love the {pizza.title()} pizza!\n')

print('I absolutely love pizza!!!\n')

friend_pizzas = pizzas[:]

pizzas.append('hawaiian')
friend_pizzas.append('vegetarian')

print(f'My favourite pizzas are:\t')
for pizza in pizzas[:]:
	print(f'\t{pizza.title()}')

print(f'\nMy friend\'s favourite pizzas are:\t')
for pizza in friend_pizzas[:]:
	print(f'\t{pizza.title()}')

# More Loops - using 'for' loops to print lists

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print('\nMy favorite foods are:')
for my_food in my_foods: print(f'\t{my_food.title()}')

print("\nMy friend's favorite foods are:")
for f_food in friend_foods: print(f'\t{f_food.title()}')