# City Names
print('---------------------------') # Empty Line
def city_country(city,country):
	"""print the city and country"""
	print(f'"{city.title()}, {country.title()}"')

city_country('johannesburg','south africa')
city_country('lagos','nigeria')
city_country('rio de janeiro', 'brazil')


# Album
print('---------------------------') # Empty line
def make_album(artist, title):
    """Create a dictionary that contains information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('maroon 5', 'songs about jane')
album1 = make_album('jimi hendrix', 'purple haze')
album2 = make_album('jack johnson', 'on and on')

print(album)
print(album1)
print(album2)


# Albums - including the optional song tracks
print('----------------------------') # Empty line
def make_album(artist, title, tracks=0):
    """Create a dictionary that contains information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('jack johnson', 'on and on')
album1 = make_album('maroon 5', 'songs about jane',tracks=8)
album2 = make_album('jimi hendrix', 'purple haze')
album3 = make_album('kiss', 'black rain',tracks=12)

print(album)
print(album1)
print(album2)
print(album3)


#User Albums
print('------------------------------') # Empty line
def make_album(artist, title, tracks=0):
    """Create a dictionary that contains information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album do you like? "
artist_prompt = "Give the artist\'s name? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks!")