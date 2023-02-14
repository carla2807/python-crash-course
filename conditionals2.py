## conditionals ##
usernames = ['admin', 'andrew', 'carolina', 'david', 'pedro']

for username in usernames:
    
    if username == 'admin':
        print('Hello admin, would you like to see a status report ?')

    elif username != 'admin':
      print('Hello' + " "+ username.title() + "," +  'thank you for log in')

###
current_users = ['admin', 'andrew', 'carolina', 'david', 'pedro'] # 1 list

new_users = ['admin', 'andrew', 'george', 'john', 'lucas'] # 2 list

#
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Sorry {new_user}, name not available')
    else:
        print(f'Great {new_user}, name available')



