# Imports



# Named Variables
continue_running = True

admin_options = ["1. View Users", 
                 "2. Add User", 
                 "3. Delete User"]

user_options = ["1. View Profile",
                "2. Edit Profile",
                "3. Logout"]



# Code

while continue_running:
    account_name = input("Enter admin or user: ")
    admin_password = input("Enter admin account password: ")
    user_password = input("Enter user account password: ")

    if account_name == "admin" and admin_password == "":
        print("Welcome, admin!")
        # Admin Thingys
        for option in admin_options:
            print(option)
    elif account_name == "user" and user_password == "":
        print("Welcome, user!")
        # User Thingys
        for option in user_options:
            print(option)
    else:
        print("This is an invalid account name. Please enter 'admin' or 'user'.")
        account_name = input("Enter admin or user: ")
    break  # Exit after


