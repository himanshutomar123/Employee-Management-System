print("=" * 50)
print("Welcome To Expense Tracker APP ")
print("=" * 50)

expenses=[]

from datetime import date


def add_expenses():
    amount = float(input("Enter TotaL Amount You Spent ="))

    if amount <= 0:
        print("Amount Must Be Greater Than 0")
        return
    expense = {
        'ID'            : len(expenses) + 1,
        "Date"          : str(date.today()),
        'Category'      :input("Enter Type (Food,Travel,Books) ="),
        'Description'   :input("Enter More Details Like ('What You Have Eaten' or Where You Have Travelled ="),
        'Amount'        : amount,
        'Payment Method': input("Payment Method (Cash/UPI/Card) = "),
        'Merchant'      : input("Store/Restaurant = "),
        'Notes'         : input("Any notes (optional) = "),
        'Time'          : input("Time (HH:MM) = "),

    }
    expenses.append(expense)
    print("\n Expense Added Successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No Expenses Found")
        return
    for expense in expenses:
        print("=" * 50)
        for key, value in expense.items():
            print(f"{key} :{value}")

def search_expenses():
    Search_Expense = input("Enter Expense Category OR ID TO Find = ")
    found = False

    for expense in expenses:
        if str(expense["ID"]) == Search_Expense or expense["Category"].lower() == Search_Expense.lower():
            print("=" * 50)
            for key, value in expense.items():
                print(f"{key} : {value}")
            found = True

    if not found:
        print("Expense Not Found")

def edit_expenses():
    Edit_Expense = input("Enter Expense ID To Edit = ")
    found = False

    for expense in expenses:
        if str(expense["ID"]) == Edit_Expense:
            print("=" * 50)
            for key, value in expense.items():
                print(f"{key} : {value}")
            found = True
            break

    if not found:
        print("Expense Not Found")

def delete_expenses():
    Delete_Expense = input("Enter Expense ID To Delete = ")
    found = False

    for expense in expenses:
        if str(expense["ID"]) == Delete_Expense:
            expenses.remove(expense)
            print("\nExpense Deleted Successfully")
            found = True
            break

    if not found:
        print("Expense Not Found")

        
def update_expenses():
    Update_Expense = input("Enter Expense ID To Update = ")
    found = False

    for expense in expenses:
        if str(expense["ID"]) == Update_Expense:
            print("Expense Found")

            expense['Category'] = input("Enter New Expense Category = ")
            expense['Description'] = input("Enter New Expense Description = ")
            expense['Amount'] = float(input("Enter New Expense Amount = "))
            expense['Payment Method'] = input("Enter New Payment Method = ")
            expense['Merchant'] = input("Enter New Store/Restaurant = ")
            expense['Notes'] = input("Enter New Notes (optional) = ")
            expense['Time'] = input("Enter New Time (HH:MM) = ")

            found = True
            print("\nExpense Updated Successfully")
            break

    if not found:
        print("Expense Not Found")

def total_expenses():
    total = 0
    total = sum(expense['Amount'] for expense in expenses)
    print(f"\n Total Expenses =  ₹{total:.2f}")

def category_wise_total():
    totals = {}

    for expense in expenses:
        category = expense["Category"]

        if category in totals:
            totals[category] += expense["Amount"]
        else:
            totals[category] = expense["Amount"]

    print("\nCategory-wise Expenses")
    print("-" * 30)

    for category, amount in totals.items():
        print(f"{category}: ₹{amount:.2f}")


while True:
    print("\n" + "=" * 50)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Update Expense")
    print("7. Total Expenses")
    print("8. Category-wise Total")
    print("9. Exit")

    try:
        choice = int(input("Enter Your Choice = "))
    except ValueError:
        print("Please Enter A Valid Number")
        continue

    if choice == 1:
        add_expenses()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        search_expenses()

    elif choice == 4:
        edit_expenses()

    elif choice == 5:
        delete_expenses()

    elif choice == 6:
        update_expenses()

    elif choice == 7:
        total_expenses()

    elif choice == 8:
        category_wise_total()

    elif choice == 9:
        print("Thank You For Using Expense Tracker!")
        break

    else:
        print("Invalid Choice")