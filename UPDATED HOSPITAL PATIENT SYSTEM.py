print("=" * 50)
print("Welcome To Hospital Patient System")
print("=" * 50)

patients =[]

def add_patient():
    patient={
        "Patient_ID"    : input("Enter Patient ID = "),
        "Name"          : input("Enter Patient Name = ").capitalize().strip(),
        "Age"           : int(input("Enter Patient Age = ")),
        "Gender"        : input("Enter Gender (Male/Female/Other) = ").capitalize(),
        "Phone"         : input("Enter Phone Number = "),
        "Address"       : input("Enter Patient Address = ").capitalize(),
        "Disease"       : input("Enter Disease = ").capitalize,
        "Doctor"        : input("Assigned Doctor = ").capitalize(),
        "Admission_Date": input("Admission Date (DD/MM/YYYY) = "),
        "Fees"          : float(input("Enter Consultation Fees = "))
    }
    
    patients.append(patient)
    print("\n Details Added Successfully")

def view_patient():
    if len(patients) == 0:
        print("No Patient Found")
        return
    
    print("\n" + "=" * 50)
    print("ALL MEMBERS")
    print("=" * 50)

    for patient in patients:
        print("=" * 50)
        for key,value in patients.items():
            print(f"{key} : {value}")

def search_patient():
    name = input("Enter Patient Name To Find =")
    found = False

    for patient in patients:
        if patient["Name"].lower() == name.lower():
            print("\n Patient Found")
            print("=" * 50)
            for key,value in patients.items():
                print(f"{key} : {value}")
            found = True
            break

        if not found:
            print("No Patient Found")
def edit_patient():
    edit_name=input("Enter Patient Name To Edit:")
    found = False

    for patient in patients:
        if patient["Name"].lower() == edit_name.lower():
            print("\n Patient Found")
            patient['Name']     = input("Enter New Edit Patient Name =")
            patient["Address" ] = input("Enter Patient Address = ")

            print("\nDetails Updated Successfully")
            found = True
            break
        if not found :
            print("No Patient Found")

def discharge_patient():
    discharge_name=input("ENTER PATIENT WHO NEEDS TO DISCHARGE:")
    found = False

    for patient in patients:
        if patient['name'].lower() == discharge_name.lower():
            print("\nPATIENT FOUND")
            patients.remove(patient)
            print("Patient Discharged Successfully")
            found = True
            break
    if not found:
        print("No Patient Found")

while True:
    print("1.Add Patient")
    print("2.View Patient")
    print("3.Search Patient")
    print("4.Edit Patient")
    print("5.Discharge Patient")
    print("6.Exit")
  

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







    