#======================================= Student Result Management System ⭐ (Highly Recommended) =============================================


print("WELCOME TO STUDENT MANAGEMENT SYSTEM")

print("============MENU===========")
print("1.ADD STUDENT")
print("2.STORE MARKS")
print("3.DISPLAY ALL STUDENTS")
print("4.CALCULATE AVERAGE")
print("5.GRADE SYSTEM")
print("6.TOPPER STUDENT")
print("7.SEARCH STUDENT")
print("8.DELETE STUDENTS")
print("9.RANK STUDENTS")
print("10.NUMPY STATISTICS")
print("11.EXIT")


students=[]


choice=int(input("ENTER YOUR CHOICE="))


while True:
    if choice == 11:
        print("THANKS")
        break
    else:
        print("Invalid")

        
    if choice == 1:
        name=input("ENTER STUDENT NAME:")
        roll_number=int(input("ENTER STUDENT ROLL NUMBER:"))
    
    elif choice == 2:
        marks1=int(input("ENTER MARKS OF SUBJECT 1="))
        marks2=int(input("ENTER MARKS OF SUBJECT 2="))
        marks3=int(input("ENTER MARKS OF SUBJECT 3="))

        student={
            'name':name,
            'roll_number':roll_number,
            'marks1':marks1,
            'marks2':marks2,
            'marks3':marks3
            
        }
        student.append(students)
        print("STUDENTS ADDED SUCCESSFULLY")



    elif choice == 3:

        if len(students)== 0:
            print("No students found")


        else:  
            print("\n =====ALL STUDENTS=======")
            for i in students:
               print(
                    f"Name: {i['name']}, "
                    f"Roll No: {i['roll_number']}, "
                    f"Marks: {i['marks1']}, {i['marks2']}, {i['marks3']}"
                )
               
               
    elif choice == 4:
        average =i['marks1']+i['marks2']+i['marks3']/len(students)
        print(f"{i['name']} AVERAGE ={average}")

    elif choice == 5:
        def calculate_grade(avg):

            if avg >= 90:
                return "A+"

            elif avg >= 80:
                 return "A"

            elif avg >= 70:
                return "B"

            elif avg >= 60:
                return "C"

            elif avg >= 50:
                return "D"

            else:
                return "Fail"
    
   
            
    elif choice == 6:
        topper_name=""
        topper_average=0
        for i in students:
            average=( i['marks1'] +
                    i['marks2'] +
                    i['marks3']
                )/len(students)
        
        if average>topper_average:
            topper_average=average
            topper_name=i['name']
            print("TOPPER NAME:",topper_name)
            print("TOPPER AVERAGE:",topper_average)


        




        

    
