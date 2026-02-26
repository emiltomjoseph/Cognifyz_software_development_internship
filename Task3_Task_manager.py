class Task:
    def __init__(self, name):
        self.name = name
        self.done = False


tasks = []


while True:
    print("\n TASK MANAGER ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task name: ")
        new_task = Task(task_name)
        tasks.append(new_task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                status = "Completed" if tasks[i].done else "Pending"
                print(f"{i+1}. {tasks[i].name} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i in range(len(tasks)):
                status = "Completed" if tasks[i].done else "Pending"
                print(f"{i+1}. {tasks[i].name} - {status}")

            try:
                num = int(input("Enter task number to mark as completed: "))
                tasks[num-1].done = True
                print("Task updated successfully.")
            except:
                print("Invalid input.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                status = "Completed" if tasks[i].done else "Pending"
                print(f"{i+1}. {tasks[i].name} - {status}")

            try:
                num = int(input("Enter task number to delete: "))
                removed_task = tasks.pop(num-1)
                print(f"Task '{removed_task.name}' deleted.")
            except:
                print("Invalid input.")

    elif choice == "5":
        print("Exiting... Goodbye!")
        break

    else:
        print("Please choose a valid option.")