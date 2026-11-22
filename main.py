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

    if account_name == "admin":
        print("admin account has been chosen, please entern the password")
        admin_password = input("Enter the admin password: ")
        if admin_password == "":
            # Admin Thingys
            for option in admin_options:
                print(option)
    elif account_name == "user":
        user_password = input("Enter the user password: ")
        if user_password == "":
            # User Thingys
            for option in user_options:
                    print(option)
    else:
        print("This is an invalid account name. Please enter 'admin' or 'user'.")
        account_name = input("Enter admin or user: ")
    break  # Exit after


