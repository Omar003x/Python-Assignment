# Import All Pages #
from pages.student import studentPage
from pages.lecturer import lecturerPage
from pages.admin import adminPage
from pages.trainer import trainerPage

# Importing OS to Clear Terminal (line 172) #
import os

# Importing JSON to Read Data from Text File #
import json

# Importing Getpass to Mask User Password Input #
import getpass

import datetime

# Read Data Text File with JSON #
db = open("data.txt", "r")
data = json.load(db)

def dataUpdater(data):
    # Overwriting Data #
    data = json.dumps(data, indent=2)

    # Updating Data in Text File # 
    db = open("data.txt", "w")
    db.write(data)

    # Message # 
    print(f"Account successfully created!")

    # Reloading Data #
    db = open("data.txt", "r")
    data = json.load(db)

# Home #
def homePage():

    # Home Page Welcoming #
    print("Welcome to APU Café")

    # Home Page Navigator #
    while True:
        homeMenuChoice = input("1. Log in \n2. Sign up\n3. Exit\n")

        match homeMenuChoice:
            case '1' :
                logIn()
            case '2' :
                signUp()
            case '3' :
                print("Thanks for using APU Café!")
                break
            case other:
                print("Invalid choice!")          

# Sign Up #
def signUp():
    # Make Local Data Accessible #
    global data
    
    print("Creating an account")

    # TP Number #
    userValid = False

    while userValid == False:
     
        userTPNumber = str(input("Enter your TP number: TP"))
        
        if not userTPNumber.isnumeric or not len(str(userTPNumber)) == 6:
            print("Invalid TP Number!")
        else:
            for user in data["users_data"]:
                if f"TP{userTPNumber}" == user["user_tp"]:
                    print("TP number is already existing!")
                    return
            else:
                userValid = True
                              
     
    # Name #
    while True:
      userFirstName = input("Enter your First name: ")
      userLastName = input("Enter your Last name: ")

      if userFirstName.isalpha() and userLastName.isalpha():
          break
      else:
          print("Name includes unallowed characters!")
      
    userName = (f"{userFirstName.capitalize()} {userLastName.capitalize()}")
    
    # Password #
    while True:
        userPassword = getpass.getpass(prompt="Enter your Password: ")
        userPasswordConfirm = getpass.getpass(prompt="Confirm your Password: ")

        if userPassword == userPasswordConfirm:
            if len(userPassword) < 8:
                print("Password too short!")
            else:
                break
        else:
            print("Password does not match!")

    # User Role Assigner #      
    while True:
        userRoleChoice = input("1. Admin \n2.Lecturer \n3.Trainer \n4.Student\n")

        userRole = "unassigned"

        match userRoleChoice:
            case '1' :
                userRole = "admin"
                break
            case '2' :
                userRole = "lecturer"
                break
            case '3' :
                userRole = "trainer"
                break
            case '4' :
                userRole = "student"
                break
            case other:
                print("Invalid choice!")

    currentDate = datetime.date.today()

    # New User Formatting #
    new_user = {"user_tp":f"TP{userTPNumber}", "password":userPassword, "fullname":userName, "role":userRole, "creation_date":f"{currentDate}"}

    # Adding the User to Database # 
    data["users_data"].append(new_user)

    dataUpdater(data)

# Log in # 
def logIn():
    # Make Local Data Accessible #
    global data
    
    # In Case No User is Assigned #
    if len(data["users_data"]) == 0:
        print("No users assigned! Please sign up.")
    else:
        # Setting Variables #
        attempts = 3
        loggedIn = False

        # Loop to Compare Entered Credentials to Database #
        while (attempts + 1) > 0 and loggedIn == False :
                
                # User Input #
                print("Kindly Log In")
                enteredTP = input("TP number: TP")
                enteredPasskey = getpass.getpass(prompt="Password: ")
                for user in data["users_data"]:


                    if user["user_tp"] == (f"TP{enteredTP}") and user["password"] == enteredPasskey:

                        print("successful log in!")
                        loggedIn = True
                    
                        name = user["fullname"].split()[0]
                        print(f"Hello, {name}!")

                        # Redirect to Page Respective to User Role #
                        match user["role"]:
                            case "admin":
                                adminPage()
                                break
                            case "trainer":
                                trainerPage()
                                break
                            case "student":
                                studentPage(user, data, dataUpdater)
                                break
                            case "lecturer":
                                lecturerPage ()
                                break
                            case other:
                                print("Role unassigned! Please contact an APU Café admin.")
                
                # Attempts Counter #
                else:
                    if attempts == 0 :
                        print("Too much attempts, try again later.")
                        break
                    else:
                        os.system('cls')
                        print(f"Invalid TP number or password! {attempts} attempts left")
                        attempts-=1
                                     
# Home Page Initiator #
homePage()