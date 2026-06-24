def calculator():
    while True:
        print("=" * 100)
        print("CALCULATOR APP ")
        print("=" * 100)
        print("Enter 'exit' to quit")

        num1 = input("ENTER FIRST NUMBER: ")
        if num1.lower() == "exit":
            break

        operator = input("ENTER OPERATOR (+, -, *, /): ")
        if operator.lower() == "exit":
            break

        num2 = input("ENTER SECOND NUMBER: ")
        if num2.lower() == "exit":
            break

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                print("Result:", num1 + num2)
            elif operator == "-":
                print("Result:", num1 - num2)
            elif operator == "*":
                print("Result:", num1 * num2)
            elif operator == "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Cannot divide by zero")
            else:
                print("Invalid operator")

        except ValueError:
            print("Error: Please enter valid numbers")

calculator()