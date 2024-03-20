class TodoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = True
        else:
            print("Invalid Task Index!")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid Task Index!")

    def display_task(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "pending"
            print(f"{i + 1}.{task['task']} - {status}")


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. View task")
        print("5. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            task = input("Enter task to add:")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter index of task to complete:")) - 1
            todo_list.complete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter index of task to remove:")) - 1
            todo_list.remove_task(task_index)
        elif choice == "4":
            todo_list.display_task()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "_main_":
    main()
