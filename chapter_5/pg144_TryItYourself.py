# Hello Admin Exercise
#Creating a list containing 'usernames'
users = ['arnold', 'caylem', 'juan', 'tash', 'admin']

for user in users:
    if user.lower() == 'admin':
        print(f'Welcome {user.title()}, would you like to see a status report?')
    elif user.lower() in users:
        print(f'Welcome {user.title()}, you have just logged in successfully!')
    else:
        print(f'Welcome Guest, you have just logged in successfully!')

print() # Empty line

# No Users - Add if test to check that list isn't empty

users = []

if users:
    for user in users:
        if user.lower() == 'admin':
            print(f'Welcome {user.title()}, would you like to see a status report?')
        elif user.lower() in users:
            print(f'Welcome {user.title()}, you have just logged in successfully!')
        else:
            print(f'Welcome Guest, you have just logged in successfully!')
else:
    print('We need to find some users!')

print() # Empty Line

# Checking Usernames
current_users = ['arnold', 'caylem', 'juan', 'tash', 'adele', 'amy']
new_users = ['caylem', 'gerald', 'adele', 'william', 'leo']

for user in new_users:
    if user.lower() in current_users:
        print(f'Please enter a new user name! {user.lower()} is currently being used!')
    else:
        print(f'The user name {user.lower()} is available! Proceed!')

print() # Empty line

# Ordinal Numbers - print and ordinal list of numbers

ordinals = [1,2,3,4,5,6,7,8,9]

for ordinal in ordinals:
    if ordinal == 1:
        print(f'{ordinal}st')
    elif ordinal == 2:
        print(f'{ordinal}nd')
    elif ordinal == 3:
        print(f'{ordinal}rd')
    else:
        print(f'{ordinal}th')