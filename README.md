# Student Task Manager
Project Status: Under Testing

A small Python console application to manage student tasks, built to practice Git and GitHub workflows.

## Features

- Add tasks (empty titles are rejected)
- Display all tasks
- Mark tasks as completed
- Delete tasks by id
- Tasks are saved in `tasks.json`

## Setup

1. Install Python 3.8 or newer.
2. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/student-task-manager.git
   cd student-task-manager
   ```

## Usage

```bash
python task_manager.py
```

Choose an option from the menu (add, show, complete, delete, exit). See `docs/user-guide.md` for details.

## Running Tests

```bash
python -m unittest discover -s tests -v
```

Tests also run automatically with GitHub Actions on every push and pull request to `main`.

## License

MIT License. See `LICENSE`.
