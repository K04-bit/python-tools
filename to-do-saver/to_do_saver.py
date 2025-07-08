# to_do_saver.py

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("📭 No tasks found.")
            else:
                print("\n📋 Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("🗂️ No task file yet. Start by adding a task.")

print("📝 To-Do List App")
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice!")
