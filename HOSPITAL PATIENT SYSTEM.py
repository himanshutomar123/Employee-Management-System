print("------------------------------------------------------Hospital Patient System 🏥----------------------------------------------------")

patients=[]

print("===================MENU===============")
print("1.ADD PATIENT")
print("2.VIEW PATIENTS")
print("3.SEARCH PATIENT")
print("4.EDIT PATIENT")
print("5.DISCHARGE PATIENT")
print("6.EXIT")

while True:
    choice = int(input("ENTER YOUR CHOICE:"))

    # ADD PATIENT:-
    if choice == 1:
        name=input("ENTER PATIENT NAME:")
        age=int(input("ENTER AGE:"))
        disease=input("ENTER DISEASE:")
        address=input("ENTER ADDRESS:")
        total_cost=float(input("ENTER TOTAL COST OF TREATMENT:"))

        patient={
            'name':name,
            'age':age,
            'disease':disease,
            'address':address,
            'total_cost':total_cost
        }

        patients.append(patient)
        print("YOUR PATIENT DICTIONARY SUCCESSFULLY ADDED")

    # VIEW PATIENT:-
    elif choice == 2:
        if len(patients) == 0:
            print("NO PATIENT FOUND")

        else:
            for i in patients:
                print(i)

    # SEARCH PATIENT:-
    elif choice == 3:
        search_name=input("ENTER NAME TO SEARCH:")
        found = False

        for i in patients:
            if i['name'].lower() == search_name.lower():
                print("PATIENT FOUND")
                
                print("===============Patients Details===========")
                print("NAME:",i['name'])
                print("AGE:",i['age'])
                print("DISEASE:",i['disease'])
                print("ADDRESS    :", i['address'])
                print("TOTAL COST :", i['total_cost'])
                print("====================================")

                found=True
                break
        if not found:
            print("PATIENT NOT FOUND")

    # EDIT PATIENT:-
    elif choice == 4:
        edit_name=input("ENTER NAME TO EDIT:")
        found = False

        for i in patients:
            if i['name'].lower() == edit_name.lower():
                print("PATIENT FOUND")

                new_name=input("ENTER NEW NAME TO EDIT:")
                new_age=int(input("ENTER AGE OF NEW PATIENT:"))
                new_disease=input("ENTER NEW DISEASE TO EDIT :")
                new_address=input("ENTER NEW ADDRESS TO EDIT:")
                new_total_cost=float(input("ENTER NEW COST OF TREATMENT:"))

                i['name']=new_name
                i['age']=new_age
                i['disease']=new_disease
                i['address']=new_address
                i['total_cost']=new_total_cost

                print("PATIENT UPDATED SUCCESSFULLY")
                found = True
                break
        if not found:
            print("PATIENT NOT FOUND")

    # Discharge Patient:-
    elif choice == 5:
        discharge_name=input("ENTER PATIENT WHO NEEDS TO DISCHARGE:")
        found = False

        for i in patients:
            if i['name'].lower() == discharge_name.lower():
                print("PATIENT FOUND")
                patients.remove(i)

                print("PATIENT DISCHARGE SUCCESSFULLY")

                found=True
                break
        if not found:
            print("PATIENT NOT FOUND")

    # EXIT:-
    elif choice == 6:
        print("THANKS FOR USING THIS HOSPITAL SYSTEM APP")
        break

    else:
        print("INVALID PATIENT")








    




