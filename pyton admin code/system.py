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

class Trainer(User):
    def __init__(self, email, username, password, levels, modules_taught):
        super().__init__(email, username, password, "trainer")
        self.levels = levels
        self.modules_taught = modules_taught

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

        new_trainer = Trainer(email, username, password, [], [])
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

def trainer_menu(logged_in_user, users, filename):
    trainer = Trainer(logged_in_user.email,logged_in_user.username,logged_in_user.password,[],[])
    while True:
        print("\nTrainer Menu:")
        print("1. View Modules Taught")
        print("2. Update Profile")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def lecturer_menu(logged_in_user, users, filename):
    lecturer = Lecturer(logged_in_user.email,logged_in_user.username,logged_in_user.password)
    while True:
        print("\nLecturer Menu:")
        print("1. View Courses")
        print("2. Update Profile")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def student_menu(logged_in_user, users, filename):
    while True:
        print("\nStudent Menu:")
        print("1. View Enrolled Courses")
        print("2. Update Profile")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            # Student.update_profile(logged_in_user, users, filename)
            pass
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

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


# Main
filename = 'users.txt'
users = load_users_from_file(filename)

logged_in_user = login(users)

if logged_in_user and logged_in_user.role == 'admin':
    admin_menu(logged_in_user, users, filename)

if logged_in_user and logged_in_user.role == 'trainer':
    trainer_menu(logged_in_user, users, filename)

if logged_in_user and logged_in_user.role == 'lecturer':
    lecturer_menu(logged_in_user, users, filename)

if logged_in_user and logged_in_user.role == 'student':
    student_menu(logged_in_user, users, filename)
