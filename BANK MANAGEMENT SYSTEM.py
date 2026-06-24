accounts = []

print("🏦 WELCOME TO BANK MANAGEMENT SYSTEM")

while True:
    print(""" 1. Create Account
              2. Login Account
              3. Check Balance
              4. Deposit Money
              5. Exit """)

    choice = int(input("ENTER YOUR CHOICE: "))

    # CREATE ACCOUNT
    if choice == 1:
        account = {
            "name": input("ENTER NAME: ").strip(),
            "age": int(input("ENTER AGE: ")),
            "gender": input("ENTER GENDER: ").lower().strip(),
            "mobile_no": input("ENTER MOBILE NO: ").strip(),
            "email": input("ENTER EMAIL: ").strip(),
            "address": input("ENTER ADDRESS: ").strip(),
            "account_no": input("ENTER ACCOUNT NO: ").strip(),
            "pin": input("ENTER PIN: ").strip(),
            "account_type": input("ENTER TYPE (saving/current): ").lower().strip(),
            "balance": float(input("ENTER INITIAL DEPOSIT: "))
        }

        accounts.append(account)
        print("ACCOUNT CREATED SUCCESSFULLY")

    # LOGIN
    elif choice == 2:
        acc_no = input("ENTER ACCOUNT NO: ").strip()
        pin = input("ENTER PIN: ").strip()

        logged_in = None

        for acc in accounts:
            if acc["account_no"] == acc_no and acc["pin"] == pin:
                logged_in = acc
                break

        if logged_in:
            print("LOGIN SUCCESSFUL")
        else:
            print("INVALID DETAILS")

    # CHECK BALANCE
    elif choice == 3:
        acc_no = input("ENTER ACCOUNT NO: ").strip()

        found = False

        for acc in accounts:
            if acc["account_no"] == acc_no:
                print("YOUR BALANCE IS:", acc["balance"])
                found = True
                break

        if not found:
            print("ACCOUNT NOT FOUND")

    # DEPOSIT MONEY
    elif choice == 4:
        acc_no = input("ENTER ACCOUNT NO: ").strip()
        amount = float(input("ENTER AMOUNT TO DEPOSIT: "))

        found = False

        for acc in accounts:
            if acc["account_no"] == acc_no:
                acc["balance"] += amount
                print("MONEY DEPOSITED SUCCESSFULLY")
                print("NEW BALANCE:", acc["balance"])
                found = True
                break

        if not found:
            print("ACCOUNT NOT FOUND")

    # EXIT
    elif choice == 5:
        print("THANK YOU FOR USING BANK SYSTEM")
        break

    else:
        print("INVALID CHOICE")