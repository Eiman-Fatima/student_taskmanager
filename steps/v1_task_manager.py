"""Student Task Manager - a simple console app to manage tasks."""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks(path=DATA_FILE):
    """Load tasks from a JSON file. Return an empty list if missing."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path=DATA_FILE):
    """Save tasks to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, title):
    """Add a new task."""
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    return task


def find_task(tasks, task_id):
    """Return the task with the given id, or None if not found."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def complete_task(tasks, task_id):
    """Mark a task as completed."""
    task = find_task(tasks, task_id)
    if task:
        task["completed"] = True
    return task


def delete_task(tasks, task_id):
    """Delete a task."""
    task = find_task(tasks, task_id)
    if task:
        tasks.remove(task)
    return task


def display_tasks(tasks):
    """Print all tasks."""
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        mark = "x" if t["completed"] else " "
        print(f"[{mark}] {t['id']}. {t['title']}")


def read_id(prompt):
    """Read an integer id from the user."""
    value = input(prompt).strip()
    if not value.isdigit():
        raise ValueError("Task id must be a number.")
    return int(value)


def main():
    tasks = load_tasks()
    menu = (
        "\n1. Add task\n2. Show tasks\n3. Complete task\n"
        "4. Delete task\n5. Exit"
    )
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                add_task(tasks, input("Task title: "))
                print("Task added.")
            elif choice == "2":
                display_tasks(tasks)
            elif choice == "3":
                complete_task(tasks, read_id("Task id to complete: "))
                print("Task completed.")
            elif choice == "4":
                delete_task(tasks, read_id("Task id to delete: "))
                print("Task deleted.")
            elif choice == "5":
                save_tasks(tasks)
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
                continue
            save_tasks(tasks)
        except ValueError as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
