# Using sorting functions on your lists

locations = ['Peru', 'Greenland', 'Bora Bora', 'Antartica', 'Namibia']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# Checking the length of lists

guests = ['Ansel Adams', 'Chase Jarvis', 'Tim Ferris']

print(f'\nGood Day Mr. {guests[0]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[1]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[2]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.\n')

print(f'The number of guests who are invited: {len(guests)}\n')

# Creating a list using each function used in Chapter 3 at least once

motorcycles = ['honda', 'ktm', 'kawasaki', 'ducati']

print(f'Normal list: {motorcycles}')
print(f'Temp Sorting: {sorted(motorcycles)}')
print(f'Temp Reversing: {sorted(motorcycles, reverse=True)}')
motorcycles.reverse()
print(f'Permanent Sorting: {motorcycles}')
motorcycles.reverse()
print(f'Reversing previous sorting: {motorcycles}')
motorcycles.sort()
print(f'Permanent Sorting: {motorcycles}\n')
print(f'The length of the motorcycles list: {len(motorcycles)}\n')

motorcycles.append('triumph')
motorcycles.insert(1,'suzuki')
motorcycles.insert(-2,'yamaha')
print(f'Motorcycles added to the list, {motorcycles[1].title()} & {motorcycles[-3].title()}: {motorcycles}\n')

owned = 'ktm'

motorcycles.remove('ktm')

print(f'I currently own a {owned} so I have removed it from the list.\n')
print(sorted(motorcycles))

del motorcycles[0]
print(f'\nDucati is too expensive so I deleted it!')
print(sorted(motorcycles))

notaste = motorcycles.pop(3)
print(f'\nThe {notaste.title()} is definitely not my type of motorcycle')
print(f'{sorted(motorcycles)}\n')

