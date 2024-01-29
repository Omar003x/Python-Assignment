# Import necessary modules
from pages.student import studentPage
from pages.lecturer import lecturerPage
from pages.admin import adminPage
from pages.trainer import trainerPage
import os
import json
import getpass
import datetime 

# Function to load data from file
def loadData():
    with open("data.txt", "r") as db:
        return json.load(db)

# Function to update data in file
def dataUpdater(data):
    with open("data.txt", "w") as db:
        json.dump(data, db, indent=2)
    print("Account successfully created!")

# Home Page
def homePage(data):
    print("Welcome to APU Café")
    while True:
        homeMenuChoice = input("1. Log in \n2. Sign up\n3. Exit\n")
        if homeMenuChoice == '1':
            logIn(data)
        elif homeMenuChoice == '2':
            signUp(data)
        elif homeMenuChoice == '3':
            print("Thanks for using APU Café!")
            break
        else:
            print("Invalid choice!")

# Sign Up Function
def signUp(data):
    print("Creating an account")
    userTPNumber = input("Enter your TP number (TPxxxxxx): ")
    if not userTPNumber.startswith("TP") or not userTPNumber[2:].isdigit() or len(userTPNumber) != 8:
        print("Invalid TP Number!")
        return

    for user in data["users_data"]:
        if userTPNumber == user["user_tp"]:
            print("TP number is already existing!")
            return

    userFirstName = input("Enter your First name: ").capitalize()
    userLastName = input("Enter your Last name: ").capitalize()
    userName = f"{userFirstName} {userLastName}"

    userPassword = getpass.getpass(prompt="Enter your Password: ")
    userPasswordConfirm = getpass.getpass(prompt="Confirm your Password: ")
    if userPassword != userPasswordConfirm:
        print("Passwords do not match!")
        return
    if len(userPassword) < 8:
        print("Password too short!")
        return

    userRole = input("Choose your role (1. Admin, 2. Lecturer, 3. Trainer, 4. Student): ")
    roleDict = {'1': 'admin', '2': 'lecturer', '3': 'trainer', '4': 'student'}
    userRole = roleDict.get(userRole, 'unassigned')
    if userRole == 'unassigned':
        print("Invalid choice!")
        return

    currentDate = str(datetime.date.today())
    new_user = {
        "user_tp": userTPNumber,
        "password": userPassword,
        "fullname": userName,
        "role": userRole,
        "creation_date": currentDate
    }
    data["users_data"].append(new_user)
    dataUpdater(data)

# Log In Function
def logIn(data):
    if not data["users_data"]:
        print("No users assigned! Please sign up.")
        return

    attempts = 3
    while attempts > 0:
        enteredTP = input("TP number: TP")
        enteredPasskey = getpass.getpass(prompt="Password: ")
        for user in data["users_data"]:
            if user["user_tp"] == f"TP{enteredTP}" and user["password"] == enteredPasskey:
                print("Successful log in!")
                name = user["fullname"].split()[0]
                print(f"Hello, {name}!")
                roleFunction = {
                    "admin": adminPage,
                    "lecturer": lecturerPage,
                    "trainer": trainerPage,
                    "student": lambda: studentPage(user, data, dataUpdater)
                }
                roleFunction.get(user["role"], lambda: print("Role unassigned! Please contact an APU Café admin."))()
                return
        attempts -= 1
        if attempts:
            print(f"Invalid TP number or password! {attempts} attempts left")
        else:
            print("Too many attempts, try again later.")
            break

# Main
if __name__ == "__main__":
    data = loadData()
    homePage(data)
