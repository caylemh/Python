# --- Multiple Modules ---
from user import User
from admin1 import Admin
from priviledges import Priviledges

user1 = Admin('anna','levine','f','caucasian','single','developer')

user1.describe_user()
user1.priviledges.show_priviledges()

user1_privs = ['can delete a post','can share a post','can ban a user']
user1.priviledges.priviledges = user1_privs

print('\nUpdating Priviledges...')
user1.priviledges.show_priviledges()