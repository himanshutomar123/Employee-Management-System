print("---------------------------------------------WELCOME TO CONTACT BOOK----------------------------------------------")

contacts=[]
print("===========MENU=========")
print("1.Add contact")
print("2.View all contact")
print("3.Search contact")
print("4.Edit contact")
print("5.Delete Contact")
print("6.Exit")

while True:
    choice =int(input("ENTER YOUR CHOICE:"))
    # ADD CONTACT:-
    if choice == 1:
        name=input("ENTER NAME=")
        mob_no=int(input("ENTER MOBILE NUMBER="))
        if len(mob_no) != 10:
            print("INVALID NUMBER")

        contact={
            'name':name,
            'mob_no':mob_no
        }
        contacts.append(contact)
        print("YOUR LIST IS ADDED SUCCESSFULLY")

    # VIEW ALL CONTACT:-
    elif choice == 2:
        if len(contacts)== 0:
            print("NO CONTACT FOUND")
        else:
            for i in contacts:
                print(i)

    # SEARCH CONTACT:-
    elif choice == 3:
        search_name=input("ENTER NAME TO SEARCH=")
        found = False

        for contact in contacts:
            if contact['name'].lower()==search_name.lower():
                print("CONTACT FOUND")
                print("NAME:",contact['name'])
                print("MOBILE NUMBER:",contact['mob_no'])
                found = True
                break

        if not found:
            print("CONTACT NOT FOUND")
    
    # EDIT CONTACT:-
    elif choice == 4:
        edit_name=input("ENTER NAME TO EDIT=")

        found=False
        
        for contact in contacts:
            if contact['name'].lower() == edit_name.lower():
                print("CONTACT FOUND")

                new_name=input("ENTER NEW NAME:")
                new_mob=int(input("ENTER NEW MOBILE NUMBER:"))
                contact['name']=new_name
                contact['mob_no']=new_mob

                print("CONTACT UPDATED SUCCESSFULLY")
                found= True
                break
        if not found:
            print("CONTACT NOT FOUND")

    # DELETE CONTACT:-
    elif choice == 5:
        delete_name=input("ENTER NAME TO DELETE:")

        found=False

        for contact in contacts:
            if contact['name'].lower() == delete_name.lower():
                print("CONTACT FOUND")
                contacts.remove(contact)
                print("CONTACT DELETE SUCCESSFULLY")

                found= True
                break

        if not found:
            print("CONTACT NOT FOUND")

    # Exit:-
    elif choice == 6:
        print("THANKS FOR USING THIS CONTACT BOOK APP:")
        break
    else:
        print("INVALID CONTACT")








