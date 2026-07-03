# UPDATED EMPLOYEE MANAGEMENT SYSTEM =
print("=" * 60)
print("Welcome To Updated Employee Management System")
print("=" * 60)

employees =[]

def add_employee():
    employee ={
        'Employee_ID': input("Enter Employee Id ="),
        'Name': input("Enter Employee Name =").strip().capitalize(),
        'Age' : int(input("Enter Employee Age =")),
        'Gender': input("Enter Employee Gender (Male/Female) = ").strip().capitalize(),
        'Mobile_Number':int(input("Enter Employee Mobile Number =")),
        'Email_ID': input("Enter Employee Email ="),
        'Address':input("Enter Employee Address ="),
        'Department': input("Enter Employee Department =").capitalize(),
        'Designation':input("Enter Employee Designation =").capitalize(),
        'Salary':float(input("Enter Employee Salary=")),
        'Experience':int(input("Enter Employee Experience =")),
        'Joining_Date':input("Enter Joining Date =")
        }
    employees.append(employee)
    print("\nEmployees Added Successfully")

def view_employee():
    if len(employees) == 0:
        print("No Employees Found")
        return
    
    print("=" * 50)
    print("All Employees")
    print("=" * 50)
    for employee in employees:
        print("\n--------------------------------------------")
        for key,value in employee.items():
            print(f"{key}: {value}")

        
def search_employee():
    search_employee = int(input("Enter Employee ID To Search Employee ="))
    found = False

    for employee in employees :
        if employee['Employee_ID'] == search_employee:
            print("\nEmployee Found")
            print("-----------------------------------------------------")
            for key,value in employee.items():
                print(f"{key}  : {value}")
                found = True
                break
    if not found :
        print("Employee Not Found")

def update_employee():
    Employee_Name = input("Enter Employee Name To Update His Details =")
    found = False

    for employee in employees :
        if employee['Name'] == Employee_Name.lower():
            print("Employee Found")

            employee['Salary']      = float(input("Enter Updated Salary ="))
            employee['Designation'] = input("Enter New Designation = ")

            print("Employee Updated Successfully")
            found = True
            break
        if not found :
            print("Employee Not Found")

def delete_employee():
    Employee_Name = input("Enter Employee Name To Delete =")
    found = False

    for employee in employees:
        if employee['Name'] == Employee_Name.lower():
            print("Employee Found")
            employees.remove(employee)
            print("Employee Deleted Successfully")

            found = True
            break
    if not found :
        print("Employee Not Found")

while True:
    print("\n Add Employee")
    print("2. View Employees")
    print("3. Search Employee By ID")
    print("4. Update Employee Details")
    print("5. Delete Employee")
    print("6. Exit")

    try:
        choice = int(input("Enter Your Choice ="))
    except ValueError:
        print("Please Enter A Valid Number")
        continue

    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employee()

    elif choice == 3:
        search_employee()
    
    elif choice == 4:
        update_employee()

    elif choice == 5:
        delete_employee()

    elif choice == 6:
        print("Thanks For Using Employee Management System")
        break
    else:
        print("Invalid Choice, Try Again")
        

    


            



            

            
            


    


