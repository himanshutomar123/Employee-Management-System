print("=" * 60)
print("Welcome To Employee Management System")
print("=" * 60)

employees = []

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee By ID")
    print("4. Update Employee Details")
    print("5. Delete Employee")
    print("6. Exit")

    try:
        choice = int(input("\nEnter Your Choice = "))
    except ValueError:
        print("Please Enter a Valid Number")
        continue

    # ---------------- ADD EMPLOYEE ----------------
    if choice == 1:
        employee = {
            'Employee_ID': input("Enter Employee ID = "),
            'Name': input("Enter Employee Name = "),
            'Age': int(input("Enter Employee Age = ")),
            'Gender': input("Enter Employee Gender = "),
            'Phone_Number': input("Enter Employee Phone Number = "),
            'Email_ID': input("Enter Employee Email = "),
            'Address': input("Enter Employee Address = "),
            'Department': input("Enter Employee Department = "),
            'Designation': input("Enter Employee Designation = "),
            'Salary': float(input("Enter Employee Salary = ")),
            'Joining_Date': input("Enter Joining Date = ")
        }

        employees.append(employee)
        print("\nEmployee Added Successfully")

    # ---------------- VIEW EMPLOYEES ----------------
    elif choice == 2:
        if len(employees) == 0:
            print("No Employees Found")
        else:
            print("\n================ ALL EMPLOYEES ================")
            for employee in employees:
                print("\n-----------------------------------")
                print(f"Employee ID   : {employee['Employee_ID']}")
                print(f"Name          : {employee['Name']}")
                print(f"Age           : {employee['Age']}")
                print(f"Gender        : {employee['Gender']}")
                print(f"Phone Number  : {employee['Phone_Number']}")
                print(f"Email         : {employee['Email_ID']}")
                print(f"Address       : {employee['Address']}")
                print(f"Department    : {employee['Department']}")
                print(f"Designation   : {employee['Designation']}")
                print(f"Salary        : {employee['Salary']}")
                print(f"Joining Date  : {employee['Joining_Date']}")

    # ---------------- SEARCH EMPLOYEE ----------------
    elif choice == 3:
        search_id = input("Enter Employee ID To Search = ")
        found = False

        for employee in employees:
            if employee['Employee_ID'] == search_id:
                print("\nEmployee Found")
                print("-----------------------------------")
                for key, value in employee.items():
                    print(f"{key} : {value}")
                found = True
                break

        if not found:
            print("Employee Not Found")

    # ---------------- UPDATE EMPLOYEE ----------------
    elif choice == 4:
        name = input("Enter Employee Name To Update = ")
        found = False

        for employee in employees:
            if employee['Name'].lower() == name.lower():
                print("Employee Found")

                employee['Salary'] = float(input("Enter New Salary = "))
                employee['Designation'] = input("Enter New Designation = ")

                print("Employee Updated Successfully")
                found = True
                break

        if not found:
            print("Employee Not Found")

    # ---------------- DELETE EMPLOYEE ----------------
    elif choice == 5:
        name = input("Enter Employee Name To Delete = ")
        found = False

        for employee in employees:
            if employee['Name'].lower() == name.lower():
                employees.remove(employee)
                print("Employee Deleted Successfully")
                found = True
                break

        if not found:
            print("Employee Not Found")

    # ---------------- EXIT ----------------
    elif choice == 6:
        print("Thanks For Using Employee Management System")
        break

    else:
        print("Invalid Choice, Try Again")