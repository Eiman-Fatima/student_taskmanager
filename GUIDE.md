# Step-by-Step Guide (do these on YOUR computer, in order)

Files in this folder:
- `steps/v1_task_manager.py` = the first (basic) version of the app. Start with this.
- `task_manager.py` = the final app (after all features).
- `tests/`, `.github/workflows/tests.yml`, `README.md`, `docs/user-guide.md`, `LAB-REPORT.md`, `lab-evidence/` = ready files you copy in at the right step.

You need: Git, Python 3, a GitHub account. Take a screenshot at every step marked **[SS]** and save it in `lab-evidence/`.

---

## Part A: Setup (do ~5 commits)

1. On GitHub: **New repository** → name `student-task-manager` → **Public** → tick **Add README**, **.gitignore: Python**, **License: MIT** → Create.
2. Clone and set your identity:
   ```bash
   git clone https://github.com/<your-username>/student-task-manager.git
   cd student-task-manager
   git config user.name "Your Name"
   git config user.email "your@email.com"
   git config --list     # [SS]
   ```
3. Build the app in small commits. Copy `steps/v1_task_manager.py` as `task_manager.py`, but do it in pieces:
   ```bash
   # Commit 1: only load_tasks, save_tasks, DATA_FILE (top of the file)
   git status
   git add task_manager.py
   git commit -m "Add task storage with JSON file"

   # Commit 2: add add_task + find_task
   git diff
   git add task_manager.py
   git commit -m "Add add_task and find_task functions"

   # Commit 3: add complete_task + delete_task
   git add task_manager.py
   git commit -m "Add complete and delete task functions"

   # Commit 4: add display_tasks, read_id, main menu
   git add task_manager.py
   git commit -m "Add display and console menu"

   # Commit 5: copy docs/user-guide.md later (Part F). For now push:
   git log --oneline     # [SS] (git status, diff, log)
   git push origin main
   git pull origin main
   ```
   Tip: paste part of the file, commit, paste the next part, commit. This shows real progress.
   Also add `.gitignore` entry `tasks.json` if it is not there.

Quick check: `python task_manager.py` works.

---

## Part C first: Create 4 Issues (needed for PRs)

On GitHub → **Issues → New issue**. Add a label to each (Labels on the right side).

| # | Title | Label |
|---|-------|-------|
| 1 | Validate input and reject empty task titles | `enhancement` |
| 2 | Mark selected tasks as completed (handle invalid id) | `enhancement` |
| 3 | Delete tasks using a valid task id | `enhancement` |
| 4 | Update README and add user guide | `documentation` |

Write 2 to 3 lines of description in each. **[SS]** of the Issues list.

---

## Part B: Feature branches (2 commits each)

Do each branch **starting from main**.

### feature/add-task
```bash
git checkout main
git checkout -b feature/add-task
```
Edit `add_task` in `task_manager.py` so it becomes:
```python
def add_task(tasks, title):
    """Add a new task. Reject empty titles."""
    if title is None or not title.strip():
        raise ValueError("Task title cannot be empty.")
    title = title.strip()
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    return task
```
```bash
git add task_manager.py
git commit -m "Reject empty task titles in add_task"
# copy tests/test_add_task.py into tests/
git add tests/test_add_task.py
git commit -m "Add tests for add_task"
git push -u origin feature/add-task
```

### feature/complete-task
```bash
git checkout main
git checkout -b feature/complete-task
```
Replace `complete_task`:
```python
def complete_task(tasks, task_id):
    """Mark a task as completed."""
    task = find_task(tasks, task_id)
    if task is None:
        raise ValueError(f"No task found with id {task_id}.")
    task["completed"] = True
    return task
```
```bash
git add task_manager.py
git commit -m "Raise error when completing unknown task"
# copy tests/test_complete_task.py
git add tests/test_complete_task.py
git commit -m "Add tests for complete_task"
git push -u origin feature/complete-task
```

### feature/delete-task
```bash
git checkout main
git checkout -b feature/delete-task
```
Replace `delete_task`:
```python
def delete_task(tasks, task_id):
    """Delete a task."""
    task = find_task(tasks, task_id)
    if task is None:
        raise ValueError(f"No task found with id {task_id}.")
    tasks.remove(task)
    return task
```
```bash
git add task_manager.py
git commit -m "Validate task id in delete_task"
# copy tests/test_delete_task.py
git add tests/test_delete_task.py
git commit -m "Add tests for delete_task"
git push -u origin feature/delete-task
```

Compare and inspect:
```bash
git diff main..feature/add-task
git branch -a
git log --oneline --graph --all     # [SS]
```
Why branches are useful (for your report): work on features separately, main stays stable, easy review and rollback.

---

## Part C: Pull Requests (3 of your 5+ merged PRs)

For each of the 3 branches on GitHub: **Compare & pull request** → base `main`.
- In the description write `Closes #1` (add-task), `Closes #2` (complete), `Closes #3` (delete).
- Open **Files changed** → click `+` on a line → write a review comment → **Start a review / Add single comment**. **[SS]** (do this on at least one PR).
- **Merge pull request**. Merge them one by one. They touch different functions so they should merge cleanly. If GitHub shows a conflict, click **Update branch** or resolve it, then merge.

Then locally:
```bash
git checkout main
git pull origin main
```

---

## PR #4: Documentation (Part F, also counts as a merged PR)

```bash
git checkout -b docs/readme-and-guide
# copy README.md (replace yours; put your username in it) and docs/user-guide.md
git add README.md docs/user-guide.md
git commit -m "Update README and add user guide"
git push -u origin docs/readme-and-guide
```
Open a PR with `Closes #4`, review, merge. Then `git checkout main && git pull origin main`.

---

## Part D: Merge conflict (do on purpose)

```bash
git checkout main
echo "" >> README.md
echo "Project status: Planning" >> README.md
git add README.md
git commit -m "Add project status to README"
git push origin main

git checkout -b conflict-a
# edit the line to: Project status: In Progress
git commit -am "Set project status to In Progress"
git push -u origin conflict-a

git checkout main
git checkout -b conflict-b
# edit the SAME line to: Project status: Completed
git commit -am "Set project status to Completed"
git push -u origin conflict-b
```
Merge the first branch (PR #5 on GitHub for `conflict-a`, or locally):
```bash
git checkout main
git merge conflict-a        # works fine
git push origin main
git merge conflict-b        # CONFLICT!
```
Open `README.md`. You will see:
```
<<<<<<< HEAD
Project status: In Progress
=======
Project status: Completed
>>>>>>> conflict-b
```
**[SS] before fixing.** Edit the file: keep one final line (for example `Project status: Completed`) and delete the `<<<<<<<`, `=======`, `>>>>>>>` lines. Do not delete other README content.
```bash
git add README.md
git commit -m "Resolve README status merge conflict"
git push origin main
```
**[SS] after fixing.** Cause (write in your report): both branches changed the same line from the same base commit, so Git could not choose automatically.

For a PR count: open the PR for `conflict-a` on GitHub and merge it there (this is PR #5).

---

## Part E: Tests and GitHub Actions (PR #6)

```bash
git checkout main && git pull origin main
git checkout -b ci/github-actions
mkdir -p .github/workflows
# copy .github/workflows/tests.yml
```
**Make a failed run first (on purpose):** in `tests/test_add_task.py` change `"Study DevOps"` in the assertEqual to `"Wrong"`.
```bash
python -m unittest discover -s tests -v    # shows a failure
git add .github tests
git commit -m "Add GitHub Actions workflow"
git push -u origin ci/github-actions
```
Open a PR to `main` → the **Actions** tab shows a red failed run. **[SS] failed run.**

Fix it (change back to `"Study DevOps"`):
```bash
git commit -am "Fix failing test"
git push
```
Wait for the green check. **[SS] successful run.** Merge the PR. Then `git checkout main && git pull origin main`.

The workflow runs on push to `main` and on PRs to `main`, with `python -m unittest discover -s tests -v`.

---

## Part G: Report and evidence

```bash
git checkout -b docs/lab-report
# copy LAB-REPORT.md and the lab-evidence folder (with your screenshots)
```
- In `LAB-REPORT.md`, replace `<your-username>` and write section 5 (your own difficulty) in your own words. Review the other answers and rewrite them in your own words, because the viva will check this.
```bash
git add LAB-REPORT.md lab-evidence
git commit -m "Add lab report and evidence"
git push -u origin docs/lab-report
```
Open PR, merge (this makes 6+ merged PRs).

---

## Part F: Release v1.0.0

```bash
git checkout main && git pull origin main
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0
```
On GitHub: **Releases → Draft a new release** → choose tag `v1.0.0` → title `v1.0.0` → notes:
```
Student Task Manager v1.0.0
- Add, show, complete, and delete tasks
- Empty title and invalid id validation
- Unit tests and GitHub Actions workflow
- README, user guide, and lab report
```
**Publish release.** **[SS]**

---

## Part H: Final checklist

- [ ] 12+ commits (`git log --oneline | wc -l`)
- [ ] 3 feature branches pushed
- [ ] 4 Issues with labels
- [ ] 5+ merged PRs
- [ ] 1 resolved conflict (screenshots)
- [ ] 3+ tests (you have 6), 1 workflow, 1 failed + 1 successful run (screenshots)
- [ ] v1.0.0 release published
- [ ] `README.md`, `LAB-REPORT.md`, `lab-evidence/` in the repo

Submit: repository URL + release URL (`https://github.com/<your-username>/student-task-manager/releases/tag/v1.0.0`).

## Viva tips
Know how to explain: why you used branches, what caused the conflict and how you fixed it, what the workflow does, and the difference between fetch/pull and merge/rebase.
