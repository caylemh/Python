import json
# Favourite Number

filename = 'favourite_num.json'
with open(filename, 'w') as f:
	num = input('What is your favourite number? ')
	json.dump(num,f)