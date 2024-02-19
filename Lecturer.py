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
                save_students()
                print("Enrollment updated successfully!")
                return
        print("Student not found!")

def delete_student():
    print("\n--- Delete Student ---")
    tp_number = input("Enter the TP number of the student to delete (or C to cancel): ")
    if tp_number.upper() != "C":
        for i, student in enumerate(students):
            if student['tp_number'] == tp_number:
                del students[i]
                save_students()
                print("Student deleted successfully!")
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
                save_students()
                print("Profile updated successfully!")
                return
        print("Student not found!")

def main():
    load_students()
    while True:
        print("\nAPU Programming Café Management System")
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

if __name__ == "__main__":
    main()
