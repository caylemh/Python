# Creating a tuple to create alist that cannot be modified
foods = ('mutton curry', 'beef stroganov', 'greek salad', 'gourmet chicken soup', 'steak carbonara')
print('\nThis is the menu:')
for item in foods: print(f'\t{item.title()}')

#Deliberately producing an Error 
#foods[1] = 'bread sticks' # (TypeError: 'tuple' object does not support item assignment)

# Creating a new tuple to create a revised list
foods_update = ('mutton curry', 'greek salad', 'steak carbonara', 'bread sticks', 'italian pasta')
print('\nThis is the revised menu:')
for item in foods_update: print(f'\t{item.title()}')