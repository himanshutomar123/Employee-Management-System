                                                            # ------ TO DO APP------ #

print("======== WELCOME TO DO APP ========")

tasks = []

while True:

    print("\n1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter Your Choice Which Task Do You Want To First: "))

    # ADD TASK
    if choice == 1:
        task_name = input("Enter Task Name: ")
        # Now Add To List.
        tasks.append(task_name)
        print("Task Added Successfully")

    # VIEW TASK
    elif choice == 2:

        if len(tasks) == 0: # MEANS 0==0
            print("No Task Found")

        else:
            print("\n======= ALL TASKS =======")

            for i in range(len(tasks)):
                  print(f"{i + 1}. {tasks[i]}")

    # REMOVE TASK
    elif choice == 3:

        if len(tasks) == 0:
            print("No Tasks To Remove")

        else:
            print("\n======= YOUR TASKS =======")

            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            remove_task = int(input("Enter Task Number You Want To Remove: "))

            if remove_task > 0 and remove_task <= len(tasks):
                
# MAKING DELETED VARIABLE TO STORE DELETED TASK:
                deleted = tasks.pop(remove_task - 1)

                print("Removed Successfully:", deleted)

            else:
                print("Invalid Task Number")

    # EXIT
    elif choice == 4:
        print("Thanks For Using TO-DO APP")
        break

    # INVALID CHOICE
    else:
        print("Invalid Choice")
