# 🧭 Module 2 – Python Invocation Meets Cloud Breath

*From foundational syntax to orchestrating with AWS IAM and S3*

---

## 🎯 Learning Objectives

- Revisit core Python concepts with annotated examples  
- Introduce `boto3` and AWS credentials setup  
- Perform basic AWS operations using Python  
- Reinforce reproducibility with `.env`, `requirements.txt`, and commit rituals  

---

## 🪜 Module Structure

### 🧪 Part 1: Python Refresher (Local Invocation)

**Folder**: `python_refresher/`

- `data_types.py`: Strings, lists, dicts with civic metaphors  
- `control_flow.py`: `if`, `for`, `while` with annotated logic  
- `functions.py`: Define and invoke simple functions  
- `file_io.py`: Read/write files with reproducibility notes  
- `api_call.py`: Use `requests` to call a public API  

> Each script includes comments that connect syntax to orchestration thinking.

---

### 🌩️ Part 2: AWS Invocation with `boto3`

**Folder**: `aws_invocation/`

- `setup_env.md`: Guide to AWS credentials and `.env` setup  
- `list_s3_buckets.py`: Use `boto3` to list S3 buckets  
- `list_iam_users.py`: Use `boto3` to list IAM users  
- `requirements.txt`: Includes `boto3`, `python-dotenv`  
- `.gitignore`: Includes `.env`, `__pycache__/`, etc.  

> Scripts include onboarding comments and reproducibility fingerprints.

---

### 🧘 Part 3: Reinforcement & Reflection

**Folder**: `learning_reinforcement/`

- `module2_reinforcement_tasks.md`: Checklist of learner tasks  
- `learning_log.md`: Template for personal reflection  
- `commit_rituals.md`: Sample poetic commit messages  

---

## 🧰 Devcontainer Support

**Folder**: `.devcontainer/`

- `devcontainer.json`: Python image, installs `boto3`, `python-dotenv`  
- VS Code extensions:  
  - `ms-python.python`  
  - `ms-python.black-formatter`  
  - `ms-python.flake8`  
  - `ms-python.isort`  

---

## 🪄 README.md Highlights

- Poetic header: *“From local breath to cloud invocation”*  
- Visual flowchart of module structure  
- Links to each subfolder with brief descriptions  
- Reflection prompt: *“What does it mean to invoke the cloud with clarity?”*

---

> This module bridges syntax and stewardship—inviting learners to breathe reproducibility into their cloud rituals.