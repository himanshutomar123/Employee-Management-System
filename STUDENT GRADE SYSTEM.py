marks = []
print("=" * 50)
print("📝 Student Grade Calculator")
print("=" * 50)
print("1. Enter student name")
print("2. Enter 5 subject marks")
print("3. Calculate total and percentage")
print("4. Display result card")
print("5. Exit")

name = ""
sub1 = sub2 = sub3 = sub4 = sub5 = 0

while True:
    choice = int(input("\nENTER YOUR CHOICE: "))

    if choice == 1:
        name = input("ENTER STUDENT NAME: ")
        print(f"Name '{name}' saved successfully! ✅")

    elif choice == 2:
        sub1 = float(input("ENTER 1st SUBJECT MARKS: "))
        sub2 = float(input("ENTER 2nd SUBJECT MARKS: "))
        sub3 = float(input("ENTER 3rd SUBJECT MARKS: "))
        sub4 = float(input("ENTER 4th SUBJECT MARKS: "))
        sub5 = float(input("ENTER 5th SUBJECT MARKS: "))
        print("Marks saved successfully! ✅")

    elif choice == 3:
        # calculate total
        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = (total / 500) * 100

        # assign grade
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F (Fail)"

        print("Calculated successfully! ✅")

    elif choice == 4:
        # print result card
        print("\n" + "=" * 40)
        print("         RESULT CARD")
        print("=" * 40)
        print(f"Student Name  : {name}")
        print(f"Marks         : {sub1}, {sub2}, {sub3}, {sub4}, {sub5}")
        print(f"Total Marks   : {total} / 500")ex
        print(f"Percentage    : {percentage:.1f}%")
        print(f"Grade         : {grade}")
        print("=" * 40)

    elif choice == 5:
        print("Thanks for using Grade Calculator! 👋")
        break

    else:
        print("Invalid choice! Please enter 1-5")