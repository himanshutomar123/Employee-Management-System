                                            # EXPENSE TRACKER PROJECT

expenses = []   # List of all expenses in the form of dictionary.

print("WELCOME TO EXPENSE TRACKER:")

while True:
    print("\n====== MENU ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))

    # ADD EXPENSE
    if choice == 1:
        date = input("Enter The Date: ")
        category = input("Enter Type (Food, Travel, Books): ")
        description = input(
            "Enter More Details (What you ate / Where you traveled): "
        )
        amount = float(input("Total Amount You Spent: "))

        # EXPENSE DICTIONARY
        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }

        expenses.append(expense)

        print("\nExpense Added Successfully!")

    # VIEW ALL EXPENSES
    elif choice == 2:

        if len(expenses) == 0:
            print("NO EXPENSES ADDED")

        else:
            print("\n====== ALL EXPENSES ======")

            count = 1

            for item in expenses:
                print(
                    f"Expense {count}: "
                    f"{item['date']}, "
                    f"{item['category']}, "
                    f"{item['description']}, "
                    f"{item['amount']}"
                )

                count += 1

    # VIEW TOTAL EXPENSES
    elif choice == 3:

        total = 0

        for item in expenses:
            total += item["amount"]

        print("\nTOTAL SPENT =", total)

    # EXIT
    elif choice == 4:
        print("Thanks for using Expense Tracker!")
        break

    else:
        print("INVALID CHOICE")
    