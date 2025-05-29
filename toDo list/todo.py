import os
import json
import time

TASKS_FILE = 'tasks.json'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def banner():
    print("""
╔══════════════════════════════════╗
    My Stylish To-Do List App  
╚══════════════════════════════════╝
""")
    print(" Organize your life. One task at a time.\n")

def show_tasks(tasks):
    if not tasks:
        print(" No tasks yet. Add one now!\n")
    else:
        print(" Your Tasks:\n")
        for i, task in enumerate(tasks, 1):
            status = "✅ Done" if task['done'] else "⏳ Pending"
            print(f"{i}. {task['title']} - {status}")

def add_task(tasks):
    title = input("\n Enter your task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(" Task added!\n")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("\n Enter task number to mark as done: "))
        tasks[choice-1]["done"] = True
        save_tasks(tasks)
        print(" Task marked as done!\n")
    except (ValueError, IndexError):
        print(" Invalid choice!\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("\n Enter task number to delete: "))
        task = tasks.pop(choice-1)
        save_tasks(tasks)
        print(f" Deleted task: {task['title']}\n")
    except (ValueError, IndexError):
        print(" Invalid choice!\n")

def main_menu():
    tasks = load_tasks()
    while True:
        clear_screen()
        banner()
        show_tasks(tasks)
        print("""
 Menu Options:
  1️  Add Task
  2️  Mark Task as Done
  3️  Delete Task
  4️  Exit
""")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            mark_done(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("\n Thank you for using My To-Do List App! 🌸\n")
            time.sleep(1)
            break
        else:
            print(" Invalid choice!\n")

        input(" Press Enter to return to the menu...")

if __name__ == "__main__":
    main_menu()
