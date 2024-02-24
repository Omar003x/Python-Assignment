import json

# Base User class
class User:
    def __init__(self, email, username, password, role):
        self.email = email
        self.username = username
        self.password = password
        self.role = role

    def update_profile(self):
        print("What do you want to update?")
        print("1. Email")
        print("2. Password")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.email = input("Enter new email: ")
            print("Email updated successfully.")
        elif choice == "2":
            self.password = input("Enter new password: ")
            print("Password updated successfully.")
        else:
            print("Invalid choice. Please try again.")

# Derived classes for specific roles
class Trainer(User):
    def __init__(self, email, username, password):
        super().__init__(email, username, password, "trainer")
        # Trainer-specific attributes can be added here

class Lecturer(User):
    def __init__(self, email, username, password):
        super().__init__(email, username, password, "lecturer")
        # Lecturer-specific attributes can be added here

class Admin(User):
    def __init__(self, email, username, password):
        super().__init__(email, username, password, "admin")

    # Admin-specific methods
    def register_user(self, users):
        new_email = input("Enter new user's email: ")
        new_username = input("Enter new user's username: ")
        new_password = input("Enter new user's password: ")
        new_role = input("Enter new user's role (admin/trainer/lecturer/student): ")
        new_user = User(new_email, new_username, new_password, new_role)
        users.append(new_user)
        print(f"{new_role.capitalize()} '{new_username}' registered successfully.")

    def delete_user(self, users):
        username_to_delete = input("Enter the username of the user to delete: ")
        user_found = False
        for user in users:
            if user.username == username_to_delete:
                users.remove(user)
                user_found = True
                print(f"User '{username_to_delete}' deleted successfully.")
                break
        if not user_found:
            print(f"User '{username_to_delete}' not found.")

# Function to simulate loading users from a file
def load_users():
    # Placeholder for actual file loading logic
    return []

# Function to simulate saving users to a file
def save_users(users):
    # Placeholder for actual file saving logic
    pass

def main():
    users = load_users()
    current_user = None

    while True:
        print("\nWelcome to the User Management System")
        if not current_user:
            print("1. Login")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                for user in users:
                    if user.username == username and user.password == password:
                        current_user = user
                        print(f"Welcome, {current_user.username}!")
                        break
                else:
                    print("Invalid credentials.")
            elif choice == "2":
                break
        else:
            if current_user.role == "admin":
                admin = Admin(current_user.email, current_user.username, current_user.password)
                print("1. Register User")
                print("2. Delete User")
                print("3. Logout")
                choice = input("Enter your choice: ")
                if choice == "1":
                    admin.register_user(users)
                elif choice == "2":
                    admin.delete_user(users)
                elif choice == "3":
                    current_user = None
            # Additional role-specific functionalities can be implemented here
            else:
                print("1. Update Profile")
                print("2. Logout")
                choice = input("Enter your choice: ")
                if choice == "1":
                    current_user.update_profile()
                elif choice == "2":
                    current_user = None

    save_users(users)

if __name__ == "__main__":
    main()
