todo_list = []
bin_list = [] 

def display_help():
    print("Available commands:")
    print("add -> Add a task to the to-do list.")
    print("complete -> Mark a task as complete.")
    print("view all -> View the current tasks in the to-do list.")
    print("view complete -> View all the completed tasks in the to-do list.")
    print("delete -> Delete a task.")
    print("view incomplete -> View all the incomplete tasks in the to-do list.")
    print("view bin -> View all the deleted tasks in the bin.")
    print("restore -> Restore a deleted task from the bin.")
    print("clear bin -> Delete all tasks permanently from the bin.")
    print("help -> Display all the help messages.")
    print("exit -> Exit the program.\n")

def add_task():
    task_description = input("Enter task description: ")

    if task_description in [task["description"] for task in todo_list]:
        print("Task already exists.")

    task = {"description": task_description, "status": "incomplete"}
    todo_list.append(task)
    print("Task added successfully.\n")


def mark_complete():
    task_number = int(input("Enter task number to mark as complete: "))

    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number.")

    task = todo_list[task_number - 1]
    task["status"] = "complete"
    print("Task marked as complete.\n")


def view_all_tasks():
    print("Tasks:")
    for task_index, task in enumerate(todo_list):
        status = "Incomplete" if task["status"] == "incomplete" else "Complete"
        print(f"{task_index + 1}. {task['description']} -> ({status})\n")



def view_completed_tasks():
    completed_tasks = [task for task in todo_list if task["status"] == "complete"]

    if not completed_tasks:
        print("No completed tasks.\n")
        return

    print("Completed tasks:")
    for task_index, task in enumerate(completed_tasks):
        print(f"{task_index + 1}. {task['description']}\n")


def delete_task():
    task_number = int(input("Enter task number to delete: "))

    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number.\n")

    task = todo_list[task_number - 1]

    permanent_deletion = input(f"Permanently delete task '{task['description']}'? (y/n): ")

    if permanent_deletion != "y":
        bin_list.append(task)
        todo_list.remove(task)
        print("Task moved to bin.\n")

    todo_list.remove(task)
    print("Task deleted permanently.\n")


def view_incomplete_tasks():
    incomplete_tasks = [task for task in todo_list if task["status"] == "incomplete"]

    if not incomplete_tasks:
        print("No incomplete tasks.\n")
        return

    print("Incomplete tasks:")
    for task_index, task in enumerate(incomplete_tasks):
        print(f"{task_index + 1}. {task['description']}\n")


def view_bin():
    if not bin_list:
        print("Bin is empty.\n")
        return

    print("Tasks in the bin:")
    for task_index, task in enumerate(bin_list):
        print(f"{task_index + 1}. {task['description']}\n")


def restore_task():
    view_bin()
    if not bin_list:
        print("No tasks in the bin to restore.\n")
        return

    task_number = int(input("Enter task number to restore: "))

    if task_number < 1 or task_number > len(bin_list):
        print("Invalid task number.\n")
        return

    task = bin_list[task_number - 1]
    todo_list.append(task)
    bin_list.remove(task)
    print("Task restored.\n")


def clear_bin():
    bin_list.clear()
    print("Bin cleared.\n")


while True:
    display_help()
    command = input("Enter a command: ").lower()

    if command == "add":
        add_task()
    elif command == "complete":
        mark_complete()
    elif command == "view all":
        view_all_tasks()
    elif command == "view complete":
        view_completed_tasks()
    elif command == "delete":
        delete_task()
    elif command == "view incomplete":
        view_incomplete_tasks()
    elif command == "view bin":
        view_bin()
    elif command == "restore":
        restore_task()
    elif command == "clear bin":
        clear_bin()
    elif command == "help":
        display_help()
    elif command == 'exit':
        confirm_exit = input("Are you sure you want to exit? (yes/no): ").lower()
        if confirm_exit == 'yes':
            print("Exiting...")
            break
        else:
            continue
    else:
        print("Invalid command! Enter 'help' to see available commands.")
