# 🧭 Module 1: Python Environment Setup

Welcome, steward of reproducible code and civic clarity.

This module guides you through setting up a Python development environment with modular precision and onboarding grace. You’ll learn how to install Python, manage dependencies, create virtual environments, and prepare your workspace for legacy-worthy contributions.

---

## 🎯 Objectives

- Install Python and `pip`
- Understand dependency management with `requirements.txt`
- Create and activate a virtual environment (`venv`)
- Install dependencies inside the environment
- Exit the environment gracefully
- Launch VS Code from the command line
- Use `.gitignore` to maintain hygiene
- Understand the role of `devcontainer.json`
- Run a sample Python program

---

## 🪜 Setup Steps

### 1. 🔧 Install Python & pip

- Download Python from [python.org](https://www.python.org/downloads/)
- Ensure `pip` is installed:  
  ```bash
  python --version
  pip --version

  2. 📁 Create Project Folder
Navigate to this module’s folder:
cd cloud-ai-integration-training/module-1-python-env-setup


3. 🧪 Create Virtual Environment
python -m venv venv_module1


4. 🚪 Activate Environment
- macOS/Linux:
source venv_module1/bin/activate
- Windows:
source venv_module1\Scripts\activate
-Git Bash on Windows:
source venv_module1/Scripts/activate

5. 📦 Install Dependencies
pip install -r requirements.txt


6. 🧘 Exit Environment
deactivate



💻 Launch VS Code
From the module folder:
code .


If code is not recognized, install the VS Code CLI from the Command Palette:
Shell Command: Install 'code' command in PATH


📜 Dependency Management
- requirements.txt lists all packages needed for this module.
- Use pip freeze > requirements.txt to capture your environment.
- Semantic versioning (==, >=) helps maintain reproducibility.

🧹 .gitignore
This file excludes unnecessary files from version control:
venv/
__pycache__/


“A clean repo is a kind invitation to future contributors.”


🧪 devcontainer.json (Optional)
This file defines a reproducible Codespaces environment:
- Pre-installs dependencies
- Configures Python settings
- Ensures onboarding clarity for learners

🧾 Sample Code
Run the sample program:
python hello.py


It will greet you and touch the GitHub API.

🪄 Reflection
“You’ve built your first coding sanctuary. What did you learn about stewardship, reproducibility, and clarity?”


🛤️ Next Steps
Commit your work with a poetic message:
git add .
git commit -m "feat: summon Python sanctuary with reproducibility rituals"


Then explore the next module in your archive.
