print("=" * 50)
print("WELCOME TO UPDATED STUDENT RESULT MANAGER")
print("=" * 50)

students = []


def add_student():
    student = {
        "Student_Name": input("Enter Student Name: ").capitalize(),
        "Class": int(input("Enter Class: ")),
        "Roll_Number": int(input("Enter Roll Number: ")),
        "marks1": float(input("Enter Marks of Subject 1: ")),
        "marks2": float(input("Enter Marks of Subject 2: ")),
        "marks3": float(input("Enter Marks of Subject 3: "))
    }

    students.append(student)
    print("\nStudent Added Successfully!")


def view_students():
    if len(students) == 0:
        print("\nNo Students Found!")
        return

    print("\n" + "=" * 50)
    print("ALL STUDENTS")
    print("=" * 50)

    for student in students:
        print("-" * 50)
        for key, value in student.items():
            print(f"{key} : {value}")



def search_student():
    name = input("Enter Student Name to Search: ")
    found = False

    for student in students:
        if student["Student_Name"].lower() == name.lower():
            print("\nStudent Found")
            print("-" * 50)
            for key, value in student.items():
                print(f"{key} : {value}")
            found = True
            break

    if not found:
        print("Student Not Found!")



def delete_student():
    name = input("Enter Student Name to Delete: ")
    found = False

    for student in students:
        if student["Student_Name"].lower() == name.lower():
            students.remove(student)
            print("Student Deleted Successfully!")
            found = True
            break

    if not found:
        print("Student Not Found!")



def average():
    if len(students) == 0:
        print("No Students Found!")
        return

    print("\nAVERAGE MARKS")
    print("-" * 50)

    for student in students:
        avg = (student["marks1"] + student["marks2"] + student["marks3"]) / 3
        print(f"{student['Student_Name']} : {avg:.2f}")



def grade_system():
    if len(students) == 0:
        print("No Students Found!")
        return

    print("\nGRADE REPORT")
    print("-" * 50)

    for student in students:
        avg = (student["marks1"] + student["marks2"] + student["marks3"]) / 3

        if avg >= 90:
            grade = "A+"
        elif avg >= 80:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 50:
            grade = "D"
        else:
            grade = "F"

        print(f"{student['Student_Name']} : Average = {avg:.2f} | Grade = {grade}")


def find_topper():
    if len(students) == 0:
        print("No Students Found!")
        return

    topper = students[0]
    highest_avg = (topper["marks1"] + topper["marks2"] + topper["marks3"]) / 3

    for student in students[1:]:
        avg = (student["marks1"] + student["marks2"] + student["marks3"]) / 3

        if avg > highest_avg:
            highest_avg = avg
            topper = student

    print("\n" + "=" * 50)
    print("TOPPER DETAILS")
    print("=" * 50)
    print(f"Name        : {topper['Student_Name']}")
    print(f"Class       : {topper['Class']}")
    print(f"Roll Number : {topper['Roll_Number']}")
    print(f"Average     : {highest_avg:.2f}")


while True:
    print("\n" + "=" * 50)
    print("STUDENT RESULT MANAGER")
    print("=" * 50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Find Average")
    print("6. Grade System")
    print("7. Find Topper")
    print("8. Exit")

    try:
        choice = input("Enter Your Choice: ")
    except ValueError:
        print("Please Enter A Valid Number")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        average()
    elif choice == "6":
        grade_system()
    elif choice == "7":
        find_topper()
    elif choice == "8":
        print("\nThank You for Using Student Result Manager!")
        break
    else:
        print("Invalid Choice! Please Try Again.")