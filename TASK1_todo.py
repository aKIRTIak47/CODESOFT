tasks = []      # will hold task text, e.g. "Buy milk"
done = []       # will hold True/False for each task, matching by position

while True:
    print("WELLCOME TO THE TO-DO LIST APP")
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")

        if task == "":
            print("Task cannot be empty.")
        else:
            tasks.append(task)
            done.append(False)   # new task starts as not done
            print("YEAH...!Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("Oops...!No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                if done[i]:
                    status = "[Congratulations! it's Done]"
                else:
                    status = "[oops! it's Not yet Done]"
                print(i + 1, ".", tasks[i], status)

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("Sorry...! There are no tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            number = input("Enter Ur task number to delete: ")

            # check the input is actually a number before converting it
            if number.isdigit() and 1 <= int(number) <= len(tasks):
                index = int(number) - 1
                tasks.pop(index)
                done.pop(index)
                print("Congratulations! Task deleted successfully!")
            else:
                print("oops! Invalid task number.")

    # Mark Task as Done
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nHere Your Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            number = input("Enter task number to mark as done: ")

            if number.isdigit() and 1 <= int(number) <= len(tasks):
                index = int(number) - 1
                done[index] = True
                print("Task marked as done! Congratulations Ur task is done!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Thank you for using Our To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")        