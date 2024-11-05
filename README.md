# Task Manager CLI Application

This Python script is a command-line interface (CLI) application for managing tasks. It allows you to add, update, delete, mark, and list tasks, with the task data stored in a JSON file (`tasks.json`). Tasks are identified by unique IDs and can have a status of "not done," "in progress," or "done."

## Features

- Add a new task
- Update a task's description
- Delete a task
- Mark a task as done, in progress, or not done
- List all tasks or filter by status

## Prerequisites

- Python 3.6 or higher

## Setup

1. Clone this repository or download the script file.
2. Ensure Python 3 is installed on your system.

## Usage

Each command has its own functionality. Here are the main commands and how to use them:

### 1. Add a Task

To add a new task with a description:

```bash
python task_manager.py add "Your task description here"
```

### 2. Update a Task

To update an existing task's description by providing its ID:

```bash
python task_manager.py update <task_id> "Updated task description"
```

Example:

```bash
python task_manager.py update 1 "New description for task 1"
```

### 3. Delete a Task

To delete a task by its ID:

```bash
python task_manager.py delete <task_id>
```

Example:

```bash
python task_manager.py delete 1
```

### 4. Mark a Task

To change the status of a task (e.g., mark as "done", "in progress", or "not done"):

```bash
python task_manager.py mark <task_id> <status>
```

Example:

```bash
python task_manager.py mark 1 done
```

### 5. List Tasks

To list all tasks, optionally filtering by status:

```bash
python task_manager.py list
```

To filter by status:

```bash
python task_manager.py list --status <status>
```

Example:

```bash
python task_manager.py list --status done
```

## JSON File

Tasks are stored in a `tasks.json` file in the same directory as the script. If this file does not exist, it will be created automatically.

## Example

Here is an example sequence of commands:

```bash
python task_manager.py add "Buy groceries"
python task_manager.py add "Finish project"
python task_manager.py mark 1 done
python task_manager.py list
python task_manager.py delete 2
```

## Error Handling

The script will notify you if you attempt to update, delete, or mark a task that does not exist by ID.

## Repository

You can find the repository on GitHub here: [COMMANDLINE_TASKS_MANAGER](https://github.com/DossoAboubakar/COMMANDLINE_TASKS_MANAGER/blob/main/README.md)

## License

This project is open-source and available for all.
