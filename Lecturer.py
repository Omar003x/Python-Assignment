import csv
import datetime

# Global variables
students = []
classes = ['Beginner', 'Intermediate', 'Advanced']
filename = "students_data.csv"

def load_students():
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        # Create the file if it does not exist, with headers
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'tp_number', 'email', 'contact_number', 'address', 'level', 'module', 'class_level', 'enrollment_month']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

def save_students():
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'tp_number', 'email', 'contact_number', 'address', 'level', 'module', 'class_level', 'enrollment_month']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

def register_student():
    print("\n--- Student Registration ---")
    name = input("Enter student's name (or C to cancel): ")
    if name.upper() != 'C':
        student = {
            'name': name,
            'tp_number': input("Enter TP number: "),
            'email': input("Enter email: "),
            'contact_number': input("Enter contact number: "),
            'address': input("Enter address: "),
            'level': input("Enter academic level (Foundation to Degree Level 3): "),
            'module': input("Enter module for coaching: "),
            'class_level': input("Enter class level (Beginner/Intermediate/Advanced): "),
            'enrollment_month': datetime.datetime.now().strftime("%B"),
        }

        students.append(student)
        save_students()  # Save the updated students list to the file
        print("Student registered successfully!")

def update_enrollment():
    print("\n--- Update Subject Enrollment ---")
    tp_number = input("Enter the TP number of the student to update (or C to cancel): ")
    if tp_number.upper() != "C":
        for student in students:
            if student['tp_number'] == tp_number:
                print(f"Current enrollment: {student['module']} in {student['class_level']} class")
                student['module'] = input("Enter new module: ")
                student['class_level'] = input("Enter new class level (Beginner/Intermediate/Advanced): ")
                save_students()  # Save the updated students list to the file
                print("Enrollment updated successfully!")
                return
        print("Student not found!")

def view_students():
    print("\n--- Registered Students ---")
    for student in students:
        print(student)

def update_profile():
    print("\n--- Update Student Profile ---")
    tp_number = input("Enter your TP number (or C to cancel): ")
    if tp_number.upper() != "C":
        for student in students:
            if student['tp_number'] == tp_number:
                student['email'] = input("Enter new email: ")
                student['contact_number'] = input("Enter new contact number: ")
                save_students()  # Save the updated students list to the file
                print("Profile updated successfully!")
                return
        print("Student not found!")

def main():
    load_students()  # Load students data from the file at the start
    while True:
        print("\nAPU Programming Café Management System")
        print("1. Register Student")
        print("2. Update Subject Enrollment")
        print("3. View Registered Students")
        print("4. Update Student Profile")
        print("5. Exit")
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
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()