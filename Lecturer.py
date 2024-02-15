import datetime

# Sample data structure to hold student and class info
students = []
classes = ['Beginner', 'Intermediate', 'Advanced']

def register_student():
    print("\n--- Student Registration ---")
    student = {
        'name': input("Enter student's name: "),
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
    print("Student registered successfully!")

def update_enrollment():
    print("\n--- Update Subject Enrollment ---")
    tp_number = input("Enter the TP number of the student to update: ")
    for student in students:
        if student['tp_number'] == tp_number:
            print(f"Current enrollment: {student['module']} in {student['class_level']} class")
            student['module'] = input("Enter new module: ")
            student['class_level'] = input("Enter new class level (Beginner/Intermediate/Advanced): ")
            print("Enrollment updated successfully!")
            return
    print("Student not found!")

def view_students():
    print("\n--- Registered Students ---")
    for student in students:
        print(student)

def update_profile():
    print("\n--- Update Student Profile ---")
    tp_number = input("Enter your TP number: ")
    for student in students:
        if student['tp_number'] == tp_number:
            student['email'] = input("Enter new email: ")
            student['contact_number'] = input("Enter new contact number: ")
            print("Profile updated successfully!")
            return
    print("Student not found!")

def main():
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
