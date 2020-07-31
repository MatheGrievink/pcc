current_users = ['admin', 'user1', 'user2', 'user3', 'user4']

new_users = ['user4', 'user5', 'user6', 'user7', 'user8']

for user in new_users:
    if user.lower() in current_users:
        print(f"Sorry, this username is not available.")
    else:
        print(f"This username is available!")
            