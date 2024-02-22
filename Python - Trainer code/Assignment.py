#2 Trainer - Add coaching class information (Eg: Class name, Charges, Class schedule, etc)
#1
#answer = input('Do you wish to add coaching class information ? (Y/N): ')
#answer = 'Yes' or 'No'
'''while True:
    try:
        answer = input('Do you wish to add coaching class information ? (Y/N): ')
    except ValueError:
        print("Please enter Y or N:")
        continue
    if answer != "Y" or answer != "N":
        print("Please enter Y or N to proceed: ")
        continue
    else:
        break'''
username = input("Name:")
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
#else:
   #print("Wrong input", "\nPlease enter Y or N to proceed.")

#4 Trainer - Send feedback (suggestion, complain etc) to administrator
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
#else:
    #print("Wrong input", "\nPlease enter Y or N to proceed.")

#3 Trainer - View list of students enrolled and paid for his/her modules
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
#else:
    #print("Wrong input", "\nPlease enter Y or N to proceed.")

#5 - Update own profile
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
			with open("profile.txt", "r")as file:
				lines = file.readlines()
				for i,line in enumerate(lines):
					parts = line.strip().split(",")
					if parts[0] == username:
						parts[0] = name
						parts[1] = password
						parts[2] = email
						lines[i] = ",".join(parts) + "\n"
			with open("profile.txt","w")as file:
				file.writelines(lines)
				print("Profile has been updated. Thank you.")
		elif answer == 'N':
			print("No changes.")
			break

#2 Trainer - Update and delete coaching class information
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
