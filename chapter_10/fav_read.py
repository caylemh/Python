import json

# Reading the favourite_num.json file
filename = 'favourite_num.json'
with open(filename) as f:
	fav_num = json.load(f)

print(f'Your favourite number is {fav_num}.')