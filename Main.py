import csv
import datetime
import os

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
def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. View All Students")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            load_students()
            print("Listing all students:\n")
            for student in students:
                print(student)
        elif choice == '2':
            break
        else:
            print("Invalid choice!")

# Lecturer Menu
def lecturer_menu():
    load_students()
    while True:
        print("\nLecturer Menu")
        print("1. Register Student")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register_student()
        elif choice == '2':
            break
        else:
            print("Invalid choice!")

# Trainer Menu Implementation
def trainer_menu():
    print("\nTrainer Menu")
    print("1. View Assigned Modules")
    print("2. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Assigned modules functionality not yet implemented.")
        elif choice == '2':
            break
        else:
            print("Invalid choice!")

# Student Menu Implementation
def student_menu():
    print("\nStudent Menu")
    print("1. View Enrolled Modules")
    print("2. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Enrolled modules functionality not yet implemented.")
        elif choice == '2':
            break
        else:
            print("Invalid choice!")

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
            admin_menu()
        elif choice == '2':
            lecturer_menu()
        elif choice == '3':
            trainer_menu()
        elif choice == '4':
            student_menu()
        elif choice == '5':
            print("Exiting application...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
