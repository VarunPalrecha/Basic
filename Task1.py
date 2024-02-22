class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("To-Do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")

    def add_task(self):
        task_name = input("Enter Task's Name: ")
        self.tasks.append({'name': task_name, 'completed':False})
        print(f"Task '{task_name}' has been added to the list.\n")

    def mark_completed(self):
        self.display_tasks()
        task_number = self.get_task_number()
        if 1<= task_number <= len(self.tasks):
            self.tasks[task_number-1]['completed'] = True
            print(f"Task '{self.tasks[task_number - 1]['name']}' marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self):
        self.display_tasks()
        task_number = self.get_task_number()
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' removed from your to-do list.")
        else:
            print("Invalid task number.")

    def get_task_number(self):
        while True:
            try:
                return int(input("Enter the task number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            to_do_list.display_tasks()
        elif choice == '2':
            to_do_list.add_task()
        elif choice == '3':
            to_do_list.mark_completed()
        elif choice == '4':
            to_do_list.remove_task()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()