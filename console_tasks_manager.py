import json
import os
import argparse
from datetime import datetime

# File path for storing tasks
TASKS_FILE = "tasks.json"

# Initialize the JSON file if it doesn't exist
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump([], file)

def load_tasks():
    """Load tasks from the JSON file."""
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "not done",
        "created_at": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def update_task(task_id, description):
    """Update a task's description."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            save_tasks(tasks)
            print(f"Task updated: {description}")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task with ID {task_id} deleted.")

def mark_task(task_id, status):
    """Mark a task as done, in progress, or not done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task with ID {task_id} not found.")

def list_tasks(filter_status=None):
    """List tasks, optionally filtering by status."""
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    for task in tasks:
        print(f"{task['id']}: {task['description']} - {task['status']}")

# Command line argument parser setup
parser = argparse.ArgumentParser(description="Task Manager Application")
subparsers = parser.add_subparsers(dest="command")

# Add task command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", type=str, help="Description of the task")

# Update task command
update_parser = subparsers.add_parser("update", help="Update an existing task")
update_parser.add_argument("id", type=int, help="ID of the task to update")
update_parser.add_argument("description", type=str, help="New description of the task")

# Delete task command
delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("id", type=int, help="ID of the task to delete")

# Mark task command
mark_parser = subparsers.add_parser("mark", help="Mark a task as done, in progress, or not done")
mark_parser.add_argument("id", type=int, help="ID of the task to mark")
mark_parser.add_argument("status", type=str, choices=["done", "in progress", "not done"], help="New status of the task")

# List tasks command
list_parser = subparsers.add_parser("list", help="List tasks")
list_parser.add_argument("--status", type=str, choices=["done", "in progress", "not done"], help="Filter by task status")

# Main execution logic
args = parser.parse_args()

if args.command == "add":
    add_task(args.description)
elif args.command == "update":
    update_task(args.id, args.description)
elif args.command == "delete":
    delete_task(args.id)
elif args.command == "mark":
    mark_task(args.id, args.status)
elif args.command == "list":
    list_tasks(args.status)
else:
    parser.print_help()
