
"""Student Task Manager - a simple console app to manage tasks."""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks(path=DATA_FILE):
    """Load tasks from a JSON file."""
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks, path=DATA_FILE):
    """Save tasks to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks, title):
    """Validate and add a new task with a unique ID."""
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Task title cannot be empty.")

    title = title.strip()
    next_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    return task


def find_task(tasks, task_id):
    """Find a task using its ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def complete_task(tasks, task_id):
    """Mark a pending task as completed."""
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValueError("Task ID must be a positive number.")

    task = find_task(tasks, task_id)

    if task is None:
        raise ValueError(f"No task found with id {task_id}.")

    if task["completed"]:
        raise ValueError("Task is already completed.")

    task["completed"] = True
    return task


def delete_task(tasks, task_id):
    """Delete a task after validating its ID."""
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValueError("Task ID must be a positive number.")

    task = find_task(tasks, task_id)

    if task is None:
        raise ValueError(f"No task found with id {task_id}.")

    tasks.remove(task)
    return task


def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks yet.")
        return

    for task in tasks:
        mark = "x" if task["completed"] else " "
        print(f"[{mark}] {task['id']}. {task['title']}")


def read_id(prompt):
    """Read and validate a task ID."""
    value = input(prompt).strip()

    if not value.isdigit() or int(value) <= 0:
        raise ValueError("Task ID must be a positive number.")

    return int(value)


def main():
    tasks = load_tasks()

    menu = (
        "\n1. Add task\n"
        "2. Show tasks\n"
        "3. Complete task\n"
        "4. Delete task\n"
        "5. Exit"
    )

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Task title: ")
                add_task(tasks, title)
                print("Task added.")

            elif choice == "2":
                display_tasks(tasks)

            elif choice == "3":
                task_id = read_id("Task id to complete: ")
                complete_task(tasks, task_id)
                print("Task completed.")

            elif choice == "4":
                task_id = read_id("Task id to delete: ")
                delete_task(tasks, task_id)
                print("Task deleted.")

            elif choice == "5":
                save_tasks(tasks)
                print("Goodbye!")
                break

            else:
                print("Invalid option.")
                continue

            save_tasks(tasks)

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
