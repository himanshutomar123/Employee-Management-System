# -------------------ATM MACHINE-------------------------
balance = 1000

while True:

    print("\n===== ATM MACHINE =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is =", balance)

    elif choice == "2":

        amount = int(input("Enter amount to deposit: "))

        balance = balance + amount

        print("Money deposited successfully")

    elif choice == "3":

        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:

            balance = balance - amount

            print("Please collect your cash")

        else:
            print("Insufficient balance")

    elif choice == "4":

        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")