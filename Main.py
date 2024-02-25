import csv
import datetime
import os
from Compiled import Trainer

from Lecturer import delete_student, update_enrollment, update_profile, view_students
from symbol import trailer

class User:
    def __init__(self, email, username, password, role):
        self.email = email
        self.username = username
        self.password = password
        self.role = role
    
    def update_profile(self, logged_in_user, users, filename):
        print("What do you want to update?")
        print("1. Email")
        print("2. Password")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_email = input("Enter new email: ")
            logged_in_user.email = new_email
        elif choice == "2":
            new_password = input("Enter new password: ")
            logged_in_user.password = new_password
        else:
            print("Invalid choice. Please try again.")
            return

            with open(filename, 'r') as file:
                lines = file.readlines()

            with open(filename, 'w') as file:
                for line in lines:
                    user_data = line.strip().split(',')
                    if user_data[1] == logged_in_user.username:
                        file.write(f"{logged_in_user.email},{logged_in_user.username},{new_password},{logged_in_user.role}\n")
                    else:
                        file.write(line)

            print("Profile updated successfully.")


class Lecturer(User):
    def __init__(self, email, username, password):
        super().__init__(email, username, password, "lecturer")

class Admin(User):
    def __init__(self, email, username, password):
        super().__init__(email, username, password, "admin")
        self.trainers = []

    def register_trainer(self, users, filename):
        email = input("Enter new trainer's email: ")
        username = input("Enter new trainer's username: ")
        password = input("Enter new trainer's password: ")

        new_trainer = trailer(email, username, password, [], [])
        self.trainers.append(new_trainer)
        users.append(new_trainer)

        save_users_to_file(users, filename)
        print(f"Trainer {username} registered successfully.")

    def register_lecturer(self, users, filename):
        email = input("Enter new lecturer's email: ")
        username = input("Enter new lecturer's username: ")
        password = input("Enter new lecturer's password: ")

        new_lecturer = Lecturer(email, username, password)
        self.trainers.append(new_lecturer)
        users.append(new_lecturer)

        save_users_to_file(users, filename)
        print(f"Lecturer {username} registered successfully.")

    def delete_trainer(self, filename):
        username = input("Enter the username of the trainer to delete: ")

        updated_users = []
        found_trainer = None

        with open(filename, 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                email, current_username, password, role = user_data

                if current_username == username and role == 'trainer':
                    found_trainer = True
                else:
                    updated_users.append(','.join([email, current_username, password, role]))

        if found_trainer:
            with open(filename, 'w') as file:
                file.write('\n'.join(updated_users))

            with open('trainers.txt', 'r') as trainer_file:
                trainers_data = trainer_file.readlines()

            with open('trainers.txt', 'w') as trainer_file:
                for line in trainers_data:
                    if username not in line:
                        trainer_file.write(line)
                        
            print(f"Trainer {username} deleted successfully.")
            
        else:
            print(f"Trainer {username} not found or is not a trainer.")
    
    def delete_lecturer(self, filename):
        username = input("Enter the username of the lecturer to delete: ")

        updated_users = []
        found_lecturer = None

        with open(filename, 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                email, current_username, password, role = user_data

                if current_username == username and role == 'lecturer':
                    found_lecturer = True
                else:
                    updated_users.append(','.join([email, current_username, password, role]))

        if found_lecturer:
            with open(filename, 'w') as file:
                file.write('\n'.join(updated_users))
            print(f"Lecturer {username} deleted successfully.")
            
        else:
            print(f"Lecturer {username} not found or is not a lecturer.")

    def assign_trainer(self, filename):
        username = input("Enter the username of the trainer to assign: ")

        found_trainer = False

        with open(filename, 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                email, current_username, password, role = user_data

                if current_username == username and role == 'trainer':
                    found_trainer = True
                    print("Choose the levels to assign to the trainer:")
                    print("1. Beginner")
                    print("2. Intermediate")
                    print("3. Advanced")
                    levels_input = input("Enter the level numbers (comma-separated) : ")
                    levels = []
                    for num in levels_input.split(','):
                        if num == '1':
                            levels.append("Beginner")
                        elif num == '2':
                            levels.append("Intermediate")
                        elif num == '3':
                            levels.append("Advanced")
                        else:
                            print("Invalid level number:", num)
                    modules = input("Enter the modules to assign to the trainer (comma-separated) : ").split(',')

                    with open('trainers.txt', 'a') as trainer_file:
                        trainer_file.write(','.join([current_username] + levels + modules) + '\n')

        if found_trainer:
            print(f"Trainer {username} assigned to levels {','.join(levels)} and modules {','.join(modules)} successfully.")
        else:
            print(f"Trainer {username} not found or is not a trainer.")

    def view_monthly_income_report(self):
        report_filename = "monthly_income_report.txt"

        try:
            with open(report_filename, 'r') as report_file:
                lines = report_file.readlines()

                if not lines:
                    print("\nNo monthly income report available.")
                else:
                    print("\nMonthly Income Report:\n")
                    for line in lines:
                        username, income = line.strip().split(',')
                        print(f"Username: {username}")
                        print(f"Income: RM{income}\n")

        except FileNotFoundError:
            print(f"\nMonthly Income Report file '{report_filename}' not found.")

    def view_feedback(self):
        feedback_filename = "feedback.txt"

        try:
            with open(feedback_filename, 'r') as feedback_file:
                lines = feedback_file.readlines()

                if not lines:
                    print("No feedback available.")
                else:
                    print("\nAll Feedback:\n")
                    for line in lines:
                        feedback_data = line.strip().split(',')
                        trainer = feedback_data[0]
                        feedback = feedback_data[1] if len(feedback_data) > 1 else ""
                        rating = feedback_data[2] if len(feedback_data) > 2 else ""
                        date = feedback_data[3] if len(feedback_data) > 3 else ""

                        print(f"Trainer: {trainer}")
                        print(f"Feedback: {feedback}")
                        if rating:
                            print(f"Rating: {rating}")
                        print(f"Date: {date}\n")
        except FileNotFoundError:
            print(f"Feedback file '{feedback_filename}' not found.")

def load_users_from_file(filename):
    try:
        with open(filename, 'r') as file:
            users = []
            for line in file:
                email, username, password, role = line.strip().split(',')
                users.append(User(email, username, password, role))
            return users
    except FileNotFoundError:
        return []

def save_users_to_file(users, filename):
    with open(filename, 'w') as file:
        for user in users:
            if isinstance(user, Admin):
                file.write(f"{user.email},{user.username},{user.password},{user.role}\n")
            elif isinstance(user, Trainer):
                file.write(f"{user.email},{user.username},{user.password},{user.role}\n")
            elif isinstance(user, Lecturer):
                file.write(f"{user.email},{user.username},{user.password},{user.role}\n")
            else:
                file.write(f"{user.email},{user.username},{user.password},{user.role}\n")

def login(users):
    attempts = 0
    while attempts < 3:
        print("Welcome! Please sign in first.\n")
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in users:
            if user.username == username and user.password == password:
                return user

        print("Invalid credentials. Please try again.")
        attempts += 1

    print("Max login attempts reached. Exiting.")
    return None


def admin_menu(logged_in_user, users, filename):
    admin = Admin(logged_in_user.email, logged_in_user.username, logged_in_user.password)
    while True:
        print("\nAdmin Menu:")
        print("1. Register Trainer")
        print("2. Delete Trainer")
        print("3. Register Lecturer")
        print("4. Delete Lecturer")
        print("5. Assign Trainer to Level and Modules")
        print("6. View Monthly Income Report")
        print("7. View Trainer Feedback")
        print("8. Update Own Profile")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin.register_trainer(users, filename)
            continue
        elif choice == "2":
            admin.delete_trainer(filename)
        elif choice == "3":
            admin.register_lecturer(users, filename)
        elif choice == "4":
            admin.delete_lecturer(filename)
        elif choice == "5":
            admin.assign_trainer(filename)
        elif choice == "6":
            admin.view_monthly_income_report()
        elif choice == "7":
            admin.view_feedback()
        elif choice == "8":
            admin.update_profile(admin, users, filename)
        elif choice == "9":
            print("Exiting Admin Menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def clearscreen():
	os.system("cls")

def get_trainer_name(username):
	with open("trainer_profile.txt","r")as f:
		for line in f:
			parts = line.strip().split(",")
			if len(parts) == 3 and parts[0] == username:
				return {
					'username': parts[0],
					'password': parts[1].strip()
					}
	return None
	
def authenticate_trainer(username, password):
	trainer = get_trainer_name(username)
	if trainer is None:
		return False
	return trainer['password'] == password


def get_stud_name(username):
	with open("students.txt","r")as f:
		for line in f:
			parts = line.strip().split(",")
			if len(parts) == 8 and parts[0] == username:
				return {
					'username': parts[0],
					'password': parts[7].strip()
					}
	return None
	
def authenticate_stud(username, password):
	stud = get_stud_name(username)
	if stud is None:
		return False
	return stud['password'] == password


def student_profile(username):
	with open("students.txt","r") as file: 
		lines = file.readlines()
	for line in lines:
		parts = line.strip().split(",")
		if parts[0] == username:
			age = parts[1]
			TPnum = parts[2]
			email = parts[3]
			contact = parts[4]
			addr = parts[5]
			month = parts[6]
			password = parts[7]
			print(f"Name:{username}\nAge:{age}\nTP Number:{TPnum}\nEmail:{email}\nContact no:{contact}\nAddress:{addr}\nJoined Date:{month}\nPassword:{password}\n")

def update_credentials(filename, username):
	with open(filename,'r')as file:
		lines = file.readlines()
	for i,line in enumerate(lines):
		parts = line.strip().split(",")
		if parts[0] == username:
			parts[1] = str(new_email())
			parts[3] = new_email
			parts[4] = str(new_con())
			parts[5] = str(new_address())
			parts[7] = new_password
			lines[i] = ",".join(parts) + "\n"
	with open(filename,"w") as file:
		file.writelines(lines)

def new_con():
    return new_cont

def new_email():
    return new_age

def show_req(filename, username):
	with open(filename,"r")as file:
		lines = file.readlines()
	for line in lines:
		parts = line.strip().split(",")
		if parts[0] == username:
			req = parts[1]
			print(f"Name:{username}\nRequest:{req}\n")

def send_req(filename, username):
	with open(filename,"r", newline = '\n')as file:
		lines = file.readlines()
	usernames = [line.strip().split(",")[0]for line in lines if line.strip()]
	if username in usernames:
		print("you already have a pending request\nTo request for another you have to delete the previous request.\n")
		enter = input("please press enter to proceed to the main menu...")
		clearscreen()
	else:
		req = input("Please enter your request: ")
		with open(filename,"a", newline = '\n') as file:
			file.write(f"\n{username},{req}")
		print(f"Request:{req}")
		print("You have succesfully added your request.\n")
		enter = input("please press enter to the main menu...")
		clearscreen()
			
def del_req(filename, username):
	lines = []
	found_req = False
	with open(filename, "r") as file:
		for line in file:
			parts = line.strip().split(",")
			if parts and parts[0] == username:
				found_req = True
			else:
				lines.append(line)
	with open(filename,"w") as file:
		file.writelines(lines)
	if found_req:
		print("\nThe request has been deleted.")
		enter = input("press enter to continue...")
	else:
		print("\nNo records found.")
		
def get_schedule_student(username):
	with open("Stud_schedule.txt","r") as file:
		lines = file.readlines()
	for line in lines:
		parts = line.strip().split(",")
		if parts[0] == username:
			day = parts[1]
			classes = parts[2]
			timing = parts[3]
			level = parts[4]
			print(f"Name:{username}\nDay:{day}\nClass:{classes}\nTime:{timing}\nLevel:{level}\n")


def get_invoice(username):
	with open("students_payment","r")as file:
		for line in file:
			parts = line.strip().split(",")
			if parts[1] == username:
				print(line)

def choose_invoice(filename, username):
	with open(filename,"r")as file:
		lines = file.readlines()
		count = 0
		num = []
		new_lines = []
		index_to_choose = None
		for i,line in enumerate(lines):
			parts = line.strip().split(",")
			if parts[0] == username:
				index_to_choose = i
				cn = parts[1]
				cl = parts[2]
				amt = int(parts[3])
				print("")
				print(f"[{count+1}]")
				num.append(count+1)
				print(f"Name:{username}\nClass:{cn}\nLevel:{cl}\nCost:{amt}\n")
				new_lines.append(f"{username},{cn},{cl},{amt}\n")
				count += 1
			else:
				new_lines.append(line)
			if num:
				quest = input("Would you like to pay for this one?(Y or N): ")
				if quest != "Y" and quest != "N":
					print("Please enter Y or N")
				elif quest == "Y":
					pay = int(input("What is the amount that you would like to pay for?: "))
					if pay > amt:
						change = pay - amt
						total = pay - amt - change
						print(f"\nPayment successful.\nReturning leftover funds of RM{change}")
						new_lines[index_to_choose] = f"{username},{cn},{cl},{total}\n"
					elif pay == amt:
						total = pay - amt
						print("Payment Successful.")
						new_lines[index_to_choose] = f"{username},{cn},{cl},{total}\n"
					elif pay < amt:
						print("Insufficient funds")
					else:
						print("enter a number")
					enter = input("press enter to continue...")
				elif quest == "N":
					print("Noted")
					
	with open("invoice.txt","w")as file:
		file.writelines(new_lines)
		
def main_menu_stud(username, password):
	max_attempts = 3
	for attempts in range(max_attempts):
		print("Welcome!\n")
		if authenticate_stud(username, password):
			print("welcome", username)
			break
		else:
			print("Invalid username or password.\n")
			if attempts < max_attempts - 1:
				print(f"you have {max_attempts - attempts -1 } attempts left.\n")	
	else:
		print("Access denied.")	
		
		
	clearscreen()
	print("MAIN MENU\n")
	print("[1]: View your schedule")
	print("[2]: Send or delete requests")
	print("[3]: View invoice")
	print("[4]: Profile")
	print("[5]: Exit")
	dec = int(input("\nWhich option would you like to choose?: "))
	A = True
	while A is True:
		try:
			if dec == 1:
				x = True
				y = True
				while x is True:
					clearscreen()
					back = None
					while back is None:
						try:
							clearscreen()
							print("This is your schedule for the week: \n")
							get_schedule_student(username)
							print("\n [1]main menu\n [2]exit\n")
							back = int(input("Which option would you like to choose?: "))
							if back not in [1,2]:
								raise ValueError
						except ValueError:
							print("\nInvalid input,please enter either 1 or 2\n")
							enter = input("press enter to continue...")
							y = False
					if back == 1:
						clearscreen()
						x = False
						continue
						break
					elif back == 2:
						A = False
						clearscreen()
						print("Exiting program...")	
						break
					else:
						while y is True:
							print("")
			
			elif dec == 2:
				x = True
				y = True
				while x is True:
					clearscreen()
					back = None
					while back is None:
						try:
							clearscreen()
							print("\n***NOTE THAT ONLY ONE REQUEST CAN BE GIVEN AT A TIME***\n")
							show_req("request.txt", username)
							print("\n{1]Make request\n[2]Delete request\n[3]main menu\n[4]exit")
							back = int(input("\nWhich option would you like to choose?: "))
							if back not in [1,2,3,4]:
								raise ValueError
						except ValueError:
							print("\nInvalid input. Please enter a number from 1 - 4\n")
							enter = input("press enter to continue...")
							y = False
					if back == 1:
						send_req("request.txt", username)
					elif back == 2:
						del_req("request.txt", username)
					elif back == 3:
						x = False
						clearscreen()
						continue
					elif back == 4:
						A = False
						clearscreen()
						print("Exiting program...")
						break
					else:
						while y is True:
							print(" ")		
	
			elif dec == 3:
				x = True
				y = True
				while x is True:
					clearscreen()
					back = None
					while back is None:
						try:
							clearscreen()
							print("This is your invoice: ")
							print("_"*25,"\n")
							get_invoice(username)
							print("_"*25,"\n")
							print("[1] Make payment\n[2] Main menu\n[3] exit\n")
							back = int(input("Which option would you like to choose?: "))
							if back not in [1,2,3]:
								raise ValueError
						except ValueError:
							print("\nInvalid input, Please enter a number between 1 - 3")
							enter = input("press enter to continue...")
							y = False
					if back == 1:
						choose_invoice("invoice.txt", username)	
					elif back == 2:
						clearscreen()
						x = False
						continue
					elif back == 3:
						A = False
						clearscreen()
						print("Exiting program...")
						break
					else:
						while y is True:
							print("")
			
			elif dec == 4:
				x = True
				y = False
				while x is True:
					clearscreen()
					back = None
					while back is None:
						try:
							clearscreen()
							student_profile(username)
							print("\n[1]: Update profile\n[2]: Main menu\n[3]: Exit")
							back = int(input("\nWhich option would you like to choose?: "))
							if back not in [1,2,3]:
								raise ValueError
						except ValueError:
							print("\nInvalid input, please enter a number between 1 - 3")
							enter = input("press enter to continue...")
							y = False
					if back == 1:
						print("_"*25)
						try:
							new_age = int(input(f"\nPlease enter the new age for {username}: "))
						except ValueError:
							clearscreen()
							print(f"Invalid. \nnew age must be in numbers.")	
							enter = input("Press enter to continue...")
							continue
							clearscreen()
							new_email = input(f"Please enter the new email for {username}: ")
							new_cont = int(input(f"Please enter your new contact no. for {username}:"))
						except ValueError:
							clearscreen()
							print(f"Invalid.\nnew contact must be in numbers")
							enter = ("Press enter to continue...")	
							clearscreen()
							continue
							new_addr = input(f"Please enter the new Address for {username}:")
							new_password = input(f"Please enter the new password for {username}: ")
							update_credentials("students.txt")
							print("_"*25)
							print("\nNew profile has been updated")
							enter = input("press enter to proceed...")
							clearscreen()
					elif back == 2:
						clearscreen()
						x = False
						continue
					elif back == 3:
						A = False
						clearscreen()
						print("Exiting program...")
						break
					else:
						while y is True:
							print("")

			elif dec == 5:
				clearscreen()
				enter = input("press enter to continue")
				clearscreen()
				A = False
			
			else:
				print("\nInvalid input")
				enter = input("Press enter to continue...")
				clearscreen()
	
		except ValueError:
			print("\ntestInvalid input")
			enter = input("Press enter to continue...")	
			clearscreen()	

# Global variables for storing data
students = []
filename = "students_data.csv"

# Function Definitions for Admin and Lecturer Functionalities
def load_students():
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print("File not found, starting with an empty list of students.")

def register_student():
    print("\n--- Register Student ---")
    student = {
        'name': input("Enter student's name: "),
        'tp_number': input("Enter TP number: "),
        'email': input("Enter email: "),
        'contact_number': input("Enter contact number: "),
        'address': input("Enter address: "),
        'level': input("Enter academic level: "),
        'module': input("Enter module for coaching: "),
        'class_level': input("Enter class level (Beginner/Intermediate/Advanced): "),
        'enrollment_month': datetime.datetime.now().strftime("%B"),
    }
    students.append(student)
    save_students()
    print("Student registered successfully!")

def save_students():
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'tp_number', 'email', 'contact_number', 'address', 'level', 'module', 'class_level', 'enrollment_month']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

# Admin Menu Implementation

# Lecturer Menu
def lecturer_menu():
    load_students()
    while True:
        print("1. Register Student")
        print("2. Update Subject Enrollment")
        print("3. View Registered Students")
        print("4. Update Student Profile")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register_student()
        elif choice == '2':
            update_enrollment()
        elif choice == '3':
            view_students()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


# Trainer Menu Implementation
def trainer_menu(username, password):
	max_attempts = 3
	for attempts in range(max_attempts):
		print("Welcome!\n")
		if authenticate_trainer(username, password):
			print("welcome", username)
			break
		else:
			print("Invalid username or password.\n")
			if attempts < max_attempts - 1:
				print(f"you have {max_attempts - attempts -1 } attempts left.\n")	
	else:
		print("Access denied.")	

	x = True
	while x is True:
		while True:
			try:
				answer = input('Do you wish to add coaching class information ? (Y/N): ')
			except ValueError:
				print("Please enter Y or N")
				continue
			if answer != 'Y' and answer != 'N':
				print("Please enter Y or N to proceed")
			elif answer == 'Y':
				cn = input("Add your class name: ")  #cn = class name
				cl = input("Add your class level: ")  #cl = class level
				charges = input("Add your charges: ")
				day = input("Add the day of the Class: ")
				ct = input("Add the timing of your Class: ")  #ct = class time
				print("\nclass name: ",cn,"\nClass level: ",cl,"charges:", charges,"\nDay: :",day,"\nClass Time: ",ct,"\n" )
				#print(f"Class name:{cn}\n")
				f = open("Coaching.txt", "a")
				f.write("\n"+username+","+cn+","+cl+","+" "+","+charges+","+day+","+ct)  #There is space between cl and charges wwhich is for student name to be updated by lecturer
				f.close()
				print("Record added. Thank you!")
			elif answer == 'N':
				print("Noted. Thank you!")
				break

		while True:
			try:
				answer = input('\nDo you wish to send feedback to the administrator ? (Y/N) :')
			except ValueError:
				print("Please enter Y or N")
				continue
			if answer != 'Y' and answer != 'N':
				print("Please enter Y or N to proceed")
			elif answer == 'Y':
				email = input("Enter your email:")
				SorC = input("\nIs it a suggestion or a complaint?:(S or C): ")
				if SorC != "S" and SorC != "C":
					print("Please enter a suggestion or a complaint\nMake sure that you have entered either S or C.")
					continue
				elif SorC == "S":
					word = "Suggestion:"
				elif SorC == "C":
					word = "Complaint:"
				s_c = input("Enter your suggestion or complain: ")
				print("Name:",username,"\nemail:",email,"\nSuggestion or Complain:",s_c)
				f = open("s_or_c.txt", "a")
				f.write("\n"+username+","+email+","+word+s_c)
				f.close()
				print("Your suggestion or complain has been sent to administration department. Thank you!")
			elif answer == 'N':
				print("Nothing has been sent. Thank you.")
				break


		while True:
			try:
				view = input('Do you wish to view your students enrollment and payment ? (Y/N) :')
				if view == "Y":
					f = open("students_payment.txt","r")
					for line in f:
						parts = line.strip().split(",")
						if parts[0] == username:
							student = parts[1]
							cn = parts[2]
							cl = parts[3]
							charges = parts[4]
							print("\nName of student:" + student + "\nClass:" +cn+ "\nClass level:" +cl+ "\nAmount left:" +charges+"\n")
					f.close()
				elif view == 'N':
					print("Noted. Thank you!")
					break
				else:
					print("Please enter Y or N")
					continue
			except ValueError:
				print("Please enter Y or N")
				continue

		while True:
			try:
				answer = input('Do you wish to update your own profile? (Y/N) :')
			except ValueError:
				print("Please enter Y or N")
				continue
			if answer != 'Y' and answer != 'N':
				print("Please enter Y or N to proceed")
			elif answer == 'Y':
				name = input("Name:")
				password = input("Password:")
				email = input("email:")
				with open("trainer_profile.txt", "r")as file:
					lines = file.readlines()
					for i,line in enumerate(lines):
						parts = line.strip().split(",")
						if parts[0] == username:
							parts[0] = name
							parts[1] = password
							parts[2] = email
							lines[i] = ",".join(parts) + "\n"
				with open("trainer_profile.txt","w")as file:
					file.writelines(lines)
					print("Profile has been updated. Thank you.")
			elif answer == 'N':
				print("No changes.")
				break

		while True:
			i = 0
			try:
				answer = input('Do you wish to update or delete coaching class information? (Y/N) :')
			except ValueError:
				print("Please enter Y or N")
				continue
			if answer != 'Y' and answer != 'N':
				print("Please enter Y or N to proceed")
			elif answer == 'Y':
				try:
					choice = input("Would you like to update or delete class information?(U/D):")
				except ValueError:
					print("Please Enter U or D")
					continue
				if choice != "U" and choice != "D":
					print("Please enter U or D to proceed")
				elif choice == "U":
					with open("Coaching.txt","r")as file:
						lines = file.readlines()
						count = 0
						num = []
						index_to_update = None
						for i,line in enumerate(lines):
							parts = line.strip().split(",")
							if parts[0] == username:
								index_to_update = i
								cn = parts[1]
								cl = parts[2]
								sn = parts[3]
								charges = parts[4]    
								day = parts[5] 
								ct = parts[6]
								print("") 
								print(count+1)
								num.append(count + 1)
								print("Student name:"+sn+"\nClass:"+cn+"\nLevel:"+cl+"\nCharges:"+charges+"\nDay:"+day+"\nTime:"+ct+"\n") 
								count += 1
						if num:
							print(num)
							quest = int(input("Which Schedule do you want to change?: "))
							if 1<= quest <= len(num):
								new_cn = input("\nWhat new class name would you like?: ")
								new_cl = input("What is the new class level?: ")
								new_charge = int(input("What is the new amount?:"))
								new_day = input("When is the new day set?: ")
								new_ct = input("When is the new time?: ")
								print("\nThis is the new schedule")
								print("\nStudent Name:"+sn+"\nClass:"+new_cn+"\nLevel:"+new_cl+"\nCharges:"+str(new_charge)+"\nDay:"+new_day+"\nTime:"+new_ct+"\n")
								lines[index_to_update] = username+","+new_cn+","+new_cl+","+parts[3]+","+str(new_charge)+","+new_day+","+new_ct+"\n"
							else:
								print("Please enter a number between1 and"+str(len(num)))			
					with open("Coaching.txt","w") as file:
							file.writelines(lines)	
		
				elif choice == "D":
					with open("Coaching.txt","r")as file:
						lines = file.readlines()
						count = 0
						num = []
						index_to_delete = []
						for i,line in enumerate(lines):
							parts = line.strip().split(",")
							if parts[0] == username:
								index_to_delete = i
								cn = parts[1]
								cl = parts[2]
								sn = parts[3]
								charges = parts[4]    
								day = parts[5] 
								ct = parts[6]
								print("") 
								print(count+1)
								num.append(count + 1)
								print("Student name:"+sn+"\nClass:"+cn+"\nLevel:"+cl+"\nCharges:"+charges+"\nDay:"+day+"\nTime:"+ct+"\n") 
								count += 1
						if num:
							print(num)
							quest = int(input("Which Schedule do you want to delete?: "))
							if 1<= quest <= len(num):
								with open("Coaching.txt","w")as file:
									for i, line in enumerate(lines):
										if i != index_to_delete:
											file.write(line)
						print("Schedule succesfully deleted.")
			elif answer =="N":
				print("Have a nice day")
				x = False
				break


# Main Menu
def main_menu():
    print("\nMain Menu")
    print("1. Admin Menu")
    print("2. Lecturer Menu")
    print("3. Trainer Menu")
    print("4. Student Menu")
    print("5. Exit")

# Main Function
def main():
	while True:
		main_menu()
		choice = input("Enter your choice: ")
		if choice == '1':
			filename = 'users.txt'
			users = load_users_from_file(filename)
			logged_in_user = login(users)
			if logged_in_user and logged_in_user.role == 'admin':
				admin_menu(logged_in_user, users, filename)
		elif choice == '2':
			lecturer_menu()
		elif choice == '3':
			username = input("Please enter your username: ")
			password = input("Please enter your password: ")
			trainer_menu(username, password)
		elif choice == '4':
			username = input("please enter your username: ")
			password = input("Please enter your password: ")
			main_menu_stud(username, password)
		elif choice == '5':
			print("Exiting application...")
			break
		else:
			print("Invalid choice!")

if __name__ == "__main__":
	main()
 
