# User Guide

## Starting the app

```bash
python task_manager.py
```

You will see this menu:

```
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

## Adding a task

Choose `1` and type a title. Empty titles are rejected with an error message.

## Showing tasks

Choose `2`. Each task is shown with its id. `[x]` means completed and `[ ]` means pending.

```
[ ] 1. Finish DevOps lab
[x] 2. Read chapter 4
```

## Completing a task

Choose `3` and enter the task id.

## Deleting a task

Choose `4` and enter a valid task id. An unknown id shows an error and nothing is deleted.

## Exiting

Choose `5`. Your tasks are saved in `tasks.json` and loaded again next time.
