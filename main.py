# Imports


# Named Variables
continue_running = True

# Admin
admin_options = [
    "1. View Users",
    "2. Add User",
    "3. Delete User"
]

admin_option_1 = "Success"

# User
user_options = [
    "1. View Profile",
    "2. Edit Profile",
    "3. Logout"
]

user_option_1 = "Success"


# Code

while continue_running:
    account_name = input("Enter admin or user: ")

    if account_name == "admin":
        print("Admin account has been chosen, please enter the password")
        admin_password = input("Enter the admin password: ")

        if admin_password == "":
            # Admin Thingys
            for option in admin_options:
                print(option)

            admin_choice = int(input("Please enter the number of the option you choose: "))

            if admin_choice == 1:
                print(admin_option_1)

    elif account_name == "user":
        user_password = input("Enter the user password: ")

        if user_password == "":
            # User Thingys
            for option in user_options:
                print(option)

            user_choice = int(input("Please enter the number of the option you choose: "))

            if user_choice == 1:
                print(user_option_1)

    else:
        print("This is an invalid account name. Please enter 'admin' or 'user'.")

    break  # Exit after one attempt
