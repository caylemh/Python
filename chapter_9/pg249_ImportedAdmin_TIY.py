# --- Imported Admin ---
from admin import *

admin1 = Admin('anna','levine','f','caucasian','single','developer')
admin1.describe_user()
admin1.priviledges.show_priviledges()
admin1_priviledges = ['can delete a post','can share a post','can ban a user']
admin1.priviledges.priviledges = admin1_priviledges

print('\nUpdating User priviledges...')
admin1.priviledges.show_priviledges()