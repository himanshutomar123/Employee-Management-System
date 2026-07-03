print("=" * 50)
print("🏦 Welcome To Bank Management System ⭐⭐⭐⭐⭐")
print("=" * 50)

accounts = []

def create_account():
    account ={
        'Name'       :input("Enter Name ="),
        'Account_No' :input("Enter Account Number ="),
        'Balance'    :float("Enter Balance In Account =")
    }

    accounts.append(account)
    print("\nAccount Created Successfully!")

def view_members():
    if len(accounts) == 0:
        print("\n No Member Found")
        return
    print("\n" + "=" * 50)
    print("ALL MEMBERS")
    print("=" * 50)
    
    for account in accounts:
        print("=" * 50)
        for key,value in accounts.items():
            print(f"{key} : {value}")

def deposit():
    acc_no = int(input("Enter Account Number: "))
    found = False

    for account in accounts:
        if account["Account_no"] == acc_no:
            print("\n Account Found")
            amount = float(input("Enter Amount to Deposit: "))
            account["balance"] += amount
            print("Money Deposited Successfully!")
            return
        found = True
        break
    if not found :
        print("Account Not Found!")

def withdraw():
    acc_no = int(input("Enter Account Number ="))
    found = False

    for account in accounts:
        if account['Account_No'] == acc_no:
            print("\n Account Found")
            amount = float(input("Enter Amount To Withdraw"))
            if amount <= account["balance"]:
                account["balance"] -= amount
                print("Withdrawal Successful!")
            else:
                print("Insufficient Balance!")
        found = True
        break
    if not found :
        print("Account Not Found!")

def check_balance ():
    acc_no = int(input("Enter Account Number ="))
    found = False

    for account in accounts:
        if account['Account_No'] == acc_no:
            print("\n Account Found")
            print("\n ====================Balance===================")
            print(f"Name: {account['name']}")
            print(f"Balance: {account['balance']}")

        found = True
        break
    if not found:
        print("Account Not Found")

def view_accounts():
    if len(accounts) == 0:
        print("No Accounts Found!")
        return

    for acc in accounts:
        print("-" * 40)
        print(f"Name: {acc['name']}")
        print(f"Account No: {acc['account_no']}")
        print(f"Balance: {acc['balance']}")


def search_account():
    name = input("Enter Name to Search: ").lower()

    for account in accounts:
        if account["name"].lower() == name:
            print("Account Found!")
            print(account)
            return

    print("Account Not Found!")

while True:
    print("\n" + "=" * 40)
    print("BANK MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Create Account")
    print("2. View Members")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. View All Accounts")
    print("7. Search Account")
    print("8. Exit")

    try:
        choice = input("Enter Your Choice =")
    except ValueError:
        print("Please Enter Valid Number")

    if choice == 1:
        create_account()
    elif choice == 2:
        view_members()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        check_balance()
    elif choice == 6:
        view_accounts()
    elif choice == 7:
        search_account()
    elif choice == "8":
        print("\nThank You for Using Student Result Manager!")
        break
    else:
        print("Invalid Choice! Please Try Again.")


        
        
            

    

    



        




    