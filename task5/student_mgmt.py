student_list = []

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks


    def __str__(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")


def add_student():
    try:
        name = input("Enter student name: ")
        roll = input("Enter student roll number: ")
        marks = int(input("Enter student marks: "))

        for student in student_list:
            if student.roll == roll:
                print("Roll number already exists.")
        new_student = Student(name, roll, marks)
        student_list.append(new_student)
        print("Student added successfully.")

    except ValueError:
        print("Enter integer value for marks.")


def view_student():
    if not student_list:
        print("No student in list.")
    else:
        print("List of students: ")
        for student in student_list:
            print(f"Name: {student.name}, Roll: {student.roll}, Marks: {student.marks}")


def search_student(roll):
    for student in student_list:
        if student.roll == roll:
            print("Student Found: ")
            print(f"Name: {student.name}, Roll: {student.roll}")
        else:
            print("Student not found")

def update_student(roll):
    for student in student_list:
        if student.roll == roll:
            try:
                new_marks = input("Enter updated marks: ")
                student.marks = float(new_marks)
                print("Student marks updated.")
            except ValueError:
                print("Enter numeric value.")
        else:
            print("Student not found.")

def delete_student(roll):
    for student in student_list:
        if student.roll == roll:
            student_list.remove(student)
            print("Student deleted successfully.")
        else:
            print("Student not found.")

while True:
    print("\n Student Management System")
    print("1. Add Student (add)")
    print("2. View Student (view)")
    print("3. Search Student (search)")
    print("4. Update Student Information (update)")
    print("5. Delete Student (delete)")
    print("6. Exit (exit)")


    choice = input("Enter your choice: ")

    if choice == 'add':
        add_student()
    
    elif choice == 'view':
        view_student()

    elif choice == 'search':
        roll_no = input("Enter roll number to search: ")
        search_student(roll_no)

    elif choice == 'update':
        roll_no = input("Enter roll number to update: ")
        update_student(roll_no)
    
    elif choice == 'delete':
        roll_no = input("Enter roll number to delete: ")
        delete_student(roll_no)

    elif choice == 'exit':
        print("Exiting")
        break
    
    else:
        print("Enter valid choice.")
