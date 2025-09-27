# 🧪 How to Use GitHub Codespaces with This Repository

Welcome, learner. This guide walks you through launching a reproducible cloud-based development environment using GitHub Codespaces and the `devcontainer.json` file included in this archive.

---

## ✅ Prerequisites

- A GitHub account
- Access to this repository (public or collaborator)
- A `.devcontainer/devcontainer.json` file present in the repo

---

## 🪜 Steps to Launch Codespaces

### 1. Open the Repository on GitHub

Navigate to the repository page:
    https://github.com/niaiengineering/cloud-ai-integration-training


### 2. Launch Codespaces

- Click the green `<> Code` button
- Select the `Codespaces` tab
- Click `Create codespace on main`

> This opens a cloud-based VS Code environment with your repo preloaded.

### 3. Wait for Devcontainer Setup

GitHub will detect the `.devcontainer/devcontainer.json` file and begin:
- Pulling the Python image (`mcr.microsoft.com/devcontainers/python:3.11`)
- Installing `pip`
- Running the `postCreateCommand`:
  ```bash
  pip install -r module-1-python-env-setup/requirements.txt
  You’ll see logs in the terminal as the environment is built.

🔍 Verify Setup
Once the Codespace opens:
- Open the terminal (`Ctrl+`` or View → Terminal)
- Run:
python --version
pip list
- 
- Confirm that requests==2.31.0 is installed


Run Sample Code
Navigate to the module folder:
cd module-1-python-env-setup
python hello.py


You should see:
- A greeting message
- GitHub API status code (e.g., 200)