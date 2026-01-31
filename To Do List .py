# TO-DO LIST APPLICATION

tasks = []

def show_task():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully!")


def update_task():
    show_task()
    try:
        task_no = int(input("\nEnter task number to update: "))
        new_task = input("Enter new task: ")
        tasks[task_no - 1] = new_task
        print("Task updated successfully!")        

    except:
        print("Invalid input!")


def delete_task():
    show_task()
    try:
        task_no = int(input("\nEnter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f"Task '{removed}' deleted successfully!")
    except:
        print("Invalid input!")


def main():
    while True:
        print()
        print("-----------------")
        print("TO-DO LIST MENU")
        print("-----------------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            show_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thanks for using To-Do List Application!")
            break
        else:
            print("Invalid choice! Please try again.")



main()
