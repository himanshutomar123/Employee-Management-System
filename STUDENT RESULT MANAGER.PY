# ======================================================STUDENT MANAGER PROJECT ============================================
student={}


while True:
    print("==================MENU===================")
    print("1.ADD STUDENTS")
    print("2.VIEW ALL STUDENTS")
    print("3.CHECK RESULT")
    print("4.EXIT")

    print("\n------WELCOME TO STUDENT MANAGER APP------------")
    choice = int(input("ENTER YOUR CHOICE:"))

    # ADD STUDENT:-
    if choice == 1:
        name=input("ENTER STUDENT NAME:")
        roll_number=int(input("ENTER ROLL NUMBER:"))
        marks=float(input("ENTER MARKS:"))
        
        student[name]={
            "roll_number":roll_number,
            "marks":marks
        }
        print(f"{name} successfully ADDED")

    # VIEW ALL STUDENT:-
    elif choice == 2:
        if not student:
            print("NO STUDENT FOUND")
        else:
            print("\n=============== STUDENT LIST ===============")
            for name ,details in student.items():
                print(f"name:name")
                print(f"roll_number:{details['roll_number']}")
                print(f"marks:{details['marks']}")
                print("-------------------------------------------")
    # CHECK RESULT:-
    elif choice == 3:
        name=input("ENTER STUDENT NAME:")
        if name in student:
            marks=student[name]["marks"]
            if marks>=40:
                print(f"{name}:PASS")
            else:
                print(f"{name}:FAIL")
        else:
            print("STUDENT NOT FOUND")

    # EXIT:-
    elif choice == 4:
        print("THANKS FOR USING THIS APP")
        break
    else:
        print("INVALID")
                      





              



