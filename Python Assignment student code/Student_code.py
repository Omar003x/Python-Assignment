import os
count = 0
def clearscreen():
	os.system("cls")

def student_profile():
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

		
def update_credentials(filename):
	with open(filename,'r')as file:
		lines = file.readlines()
	for i,line in enumerate(lines):
		parts = line.strip().split(",")
		if parts[0] == username:
			parts[1] = str(new_age)
			parts[3] = new_email
			parts[4] = str(new_cont)
			parts[5] = new_addr
			parts[7] = new_password
			lines[i] = ",".join(parts) + "\n"
	with open(filename,"w") as file:
		file.writelines(lines)
		
def show_req(filename):
	with open(filename,"r")as file:
		lines = file.readlines()
	for line in lines:
		parts = line.strip().split(",")
		if parts[0] == username:
			req = parts[1]
			print(f"Name:{username}\nRequest:{req}\n")

def send_req(filename):
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
			
def del_req(filename):
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
		
def get_schedule_student():
	with open("Stud_schedule.txt","r") as file:
		lines = file.readlines()
	for line in lines:
		parts = line.strip().split(",")
		if parts[0]  == username:
			day = parts[1]
			classes = parts[2]
			timing = parts[3]
			level = parts[4]
			print(f"Name:{username}\nDay:{day}\nClass:{classes}\nTime:{timing}\nLevel:{level}\n")


def get_invoice():
	with open("invoice.txt","r")as file:
		for line in file:
			if line.startswith(f"{username}"):
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
		
'''def read_invoice(file_name):
	invoice = {}
	with open(file_name, "r")as file:
		for line in file:
			username, amount = line.strip().split(",")
			invoice[username] = int(amount)
	return invoice'''

'''def subtract_amount(invoice, username, amount):
	if username in invoice:
		amount = int(invoice[username])
		invoice[username] = str(amount - pay)
		if amount - pay < 0:
			print(f"returning leftover amount: {amount - pay}")
		return True
	else:
		print(f"{username} not found in the invoice")
		return False'''

'''def write_invoice(file_name, invoice):
	with open(file_name, "w")as file:
		for username, amount in invoice.items():
			file.write(f"{username},{amount}\n")'''
	
def main_menu_stud():
	print("MAIN MENU\n")
	print("[1]: View your schedule")
	print("[2]: Send or delete requests")
	print("[3]: View invoice")
	print("[4]: Profile")
	print("[5]: Exit")
	dec = int(input("\nWhich option would you like to choose?: "))
	return dec



username = input("Name:")
clearscreen()
A = True
while A is True:
	try:
		dec = main_menu_stud()
		
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
						get_schedule_student()
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
						show_req("request.txt")
						print("\n{1]Make request\n[2]Delete request\n[3]main menu\n[4]exit")
						back = int(input("\nWhich option would you like to choose?: "))
						if back not in [1,2,3,4]:
							raise ValueError
					except ValueError:
						print("\nInvalid input. Please enter a number from 1 - 4\n")
						enter = input("press enter to continue...")
						y = False
				if back == 1:
					send_req("request.txt")
				elif back == 2:
					del_req("request.txt")
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
						get_invoice()
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
						student_profile()
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
			print("Exiting program...")
			A = False
		else:
			print("\nInvalid input")
			enter = input("Press enter to continue...")
			clearscreen()
	except ValueError:
		print("\ntestInvalid input")
		enter = input("Press enter to continue...")	
		clearscreen()	
		
