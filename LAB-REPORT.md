# Lab Report - Student Task Manager (CSC418)

**Name:** Eiman  
**Course:** DevOps for Cloud Computing  
**Repository:** https://github.com/<your-username>/student-task-manager  
**Release:** https://github.com/<your-username>/student-task-manager/releases/tag/v1.0.0

## 1. Git vs GitHub; add, commit, push

Git is a version control tool that runs on my computer and tracks changes in my files. GitHub is a website that hosts Git repositories online so people can share and collaborate.

- `git add` puts changed files in the staging area, ready for the next commit.
- `git commit` saves a snapshot of the staged files in the local history with a message.
- `git push` uploads my local commits to the remote repository on GitHub.

## 2. Branches, Pull Requests, and merge conflicts

Branches let me work on a feature separately without breaking the main code. A Pull Request (PR) asks to merge a branch into main, and lets others review the changes and discuss them before merging.

A merge conflict happens when two branches change the same line of the same file differently, so Git cannot decide which change to keep.

## 3. Fetch vs pull; merge vs rebase

- `git fetch` downloads new commits from the remote but does not change my working files. `git pull` is fetch plus merge, so it updates my current branch too.
- `git merge` joins two branches and creates a merge commit, keeping the full history. `git rebase` moves my commits on top of another branch, giving a straight, cleaner history but rewriting commits.

## 4. GitHub Issues and Actions

Issues track tasks, bugs, and ideas in one place with labels and descriptions, so the team knows what to do. GitHub Actions runs automated workflows, such as tests, on every push or PR. This catches errors early and saves manual checking.

## 5. One difficulty and how I solved it

**Difficulty:** <write your own: e.g., the merge conflict in README.md showed conflict markers and I was not sure which lines to keep.>  
**Solution:** <write your own: e.g., I opened the file, kept both changes in the correct form, removed the markers, ran `git add` and `git commit`.>
