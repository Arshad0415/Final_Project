import json

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed  # Now accepts 'completed' status

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Title: {self.title}, Description: {self.description}, Category: {self.category}, Status: {status}"

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== Personal To-Do List Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task Title: ")
            description = input("Task Description: ")
            category = input("Task Category (e.g., Work, Personal, Urgent): ")
            task = Task(title, description, category)
            tasks.append(task)
            print("Task added successfully.")
        
        elif choice == '2':
            display_tasks(tasks)
        
        elif choice == '3':
            display_tasks(tasks)
            task_num = int(input("Enter task number to mark as completed: "))
            if 0 < task_num <= len(tasks):
                tasks[task_num - 1].mark_completed()
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        
        elif choice == '4':
            display_tasks(tasks)
            task_num = int(input("Enter task number to delete: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
