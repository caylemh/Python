# Creating a 'list' of guests to invite to a dinner

guests = ['Ansel Adams', 'Chase Jarvis', 'Tim Ferris']

print(f'\nGood Day Mr. {guests[0]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[1]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[2]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.\n')

# Replacing a value in the 'list' with another

print(f'-- Unfortunately Mr. {guests[0]} cannot attend the Special Dinner. --')

guests[0] = 'Jerry Caldwell'

print(f'\nGood Day Mr. {guests[0]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[1]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[2]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.\n')

# Adding more values to your 'list' at specific locations in the 'list'

print('-- Good Day Everyone I have managed to obtain a larger table and therefore I would be inviting more guests. Thank you. --')

guests.insert(0, 'William Krill')
guests.insert(2, 'John Stevens')
guests.append('Amy Le Fleur')

print(f'\nGood Day Mr. {guests[0]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[1]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[2]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[3]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[4]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Ms {guests[5]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.\n')

# Deleting values from the 'list' and eventually clearing the 'list' of all values

print('-- Evening Everyone, unfortunately I was informed that I can only invite 2 guests! Sadly!-- ')

rem1 = guests.pop(0)
print(f'\nGood Day Mr. {rem1}, regrettably I cannot invite you to the Special Dinner. Thank You.')

rem2 = guests.pop(0)
print(f'Good Day Mr. {rem2}, regrettably I cannot invite you to the Special Dinner. Thank You.')

rem3 = guests.pop(0)
print(f'Good Day Mr. {rem3}, regrettably I cannot invite you to the Special Dinner. Thank You.')

rem4 = guests.pop(-1)
print(f'Good Day Ms {rem4}, regrettably I cannot invite you to the Special Dinner. Thank You.\n')

print(f'** Good Day Mr.{guests[0]} & Mr.{guests[1]}, you are still invited to attend the Special Dinner this evening at the Moulin Rouge at 7PM. Thank You. **\n')

# Remove all values from the 'list' but keep the list and display the contents after

del guests[0]
del guests[0]
print('Unfortunately the Special Dinner has been cancelled! Sorry!')
print(f'Number of Guests invited: {len(guests)}\n')