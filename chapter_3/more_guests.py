# Creating a 'list' of guests to invite to a dinner

guests = ['Ansel Adams', 'Chase Jarvis', 'Tim Ferris']

print(f'\nGood Day Mr. {guests[0]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[1]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[2]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.\n')

# Replacing a value in the 'list' with another

print(f'Unfortunately Mr. {guests[0]} cannot attend the Special Dinner.')

guests[0] = 'Jerry Caldwell'

print(f'\nGood Day Mr. {guests[0]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[1]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[2]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.\n')

# Adding more values to your 'list' at specific locations in the 'list'

print('Good Day Everyone I have managed to obtain a larger table and therefore I would be inviting more guests. Thank you.')

guests.insert(0, 'William Krill')
guests.insert(2, 'John Stevens')
guests.append('Amy Le Fleur')

print(f'\nGood Day Mr. {guests[0]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[1]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[2]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[3]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Mr. {guests[4]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.')
print(f'Good Day Ms {guests[5]}, you are kindly invited to attend a Special Dinner this evening at the Moulin Rouge at 7PM. Thank You.\n')
