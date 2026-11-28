# Imports
import csv

# Named Variables
continue_running = True

path_to_users = "/users.csv"
path_to_companys = "/company.csv"

# Admin
admin_options = [
    "1. View Users",
    "2. Verify User",
    "3. Delete User"
]

def admin_option_1():
    with open(path_to_users, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)


def admin_option_2():
    with open(path_to_users, "r", encoding="utf-8") as f:
        print(f.read())

    choice = input("Enter the username to approve: ").strip()

    if choice in choice:
        choice[choice]["approved"] = True
        print(f"{choice} is now approved")
    else:
        print("User not found")


def admin_option_3():
    print("Success")


# User
user_options = [
    "1. Create Company Account",
    "2. Create User",
    "3. Logout"
]

def user_option_1():
    company = input("What is the company name? ")
    with open("company.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([company])

    print("Company Name Added Successfully!")

def user_option_2():
    username = input("What is the username? ")
    with open("user.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([username])

        print("User Added Successfully!")

def user_option_3():
    print("Success")


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
                admin_option_1()

            elif admin_choice == 2:
                admin_option_2()

            elif admin_choice == 3:
                admin_option_3()

            else:
                print("Failed")

    elif account_name == "user":
        user_password = input("Enter the user password: ")

        if user_password == "":
            # User Thingys
            for option in user_options:
                print(option)

            user_choice = int(input("Please enter the number of the option you choose: "))

            if user_choice == 1:
                user_option_1()

            elif user_choice == 2:
                user_option_2()

            elif user_choice == 3:
                user_option_3()

            else:
                print("Failed")

    else:
        print("This is an invalid account name. Please enter 'admin' or 'user'.")

    break  # Exit after one attempt
