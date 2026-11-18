# Imports



# Named Variables
continue_running = True

admin_options = ["View Users", 
                 "Add User", 
                 "Delete User"]

user_options = ["View Profile",
                "Edit Profile",
                "Logout"]



# Code

while continue_running:
    account_name = input("Enter admin or user: ")

    if account_name == "admin":
        print("Welcome, admin!")
        # Admin-specific functionality can be added here
        print(admin_options)
    elif account_name == "user":
        print("Welcome, user!")
        # User-specific functionality can be added here
        print(user_options)
    else:
        print("This is an invlalid account name. Please enter 'admin' or 'user'.")
        account_name = input("Enter admin or user: ")
    break  # Exit the loop after one iteration for demonstration purposes


