# 🌩️ Module 2 – Python Invocation Meets Cloud Breath

*From foundational syntax to orchestrating with AWS IAM and S3*

This module bridges the breath of local Python invocation with the rhythm of cloud orchestration. Learners revisit core syntax, then ascend into AWS rituals using `boto3`, all while honoring reproducibility and onboarding clarity.

---

## 🎯 Learning Objectives

- Refresh Python fundamentals with annotated examples  
- Invoke AWS IAM and S3 using `boto3`  
- Practice object-oriented design for cloud resources  
- Reinforce reproducibility with `.env`, `requirements.txt`, and commit rituals  

---

## 🗂️ Folder Structure
module-2-python-cloud-bridge/
    aws_invocation/
        cloud_resource_class.py
        iam_user_class.py    
    devcontainer/
        devecontainer.json    
    learning_reinforcement/
        learning_log.md
        module2_practice.md
    python_refresher/
        api_call.py
        control_flow.py
        data_types.py
        file_io.py
        functions.py
        object_oriented.py
    venv_module2/
        all the files in this folder will hold the dependencies
    .gitignore
        this file will have entries of all files and folders that are NOT committed to the remote repo
    module2_scope.md
    README.md
    requirements.txt

---
## 🧪 Practice Rituals

See [`learning_reinforcement/module2_practice.md`](learning_reinforcement/module2_practice.md) for hands-on tasks:
- Refresh syntax with civic metaphors
- Invoke AWS services using `boto3`
- Reflect and commit with poetic messages

---

## 🧘 Reflection & Stewardship

Use [`learning_reinforcement/learning_log.md`](learning_reinforcement/learning_log.md) to record:
- What surprised you?
- What errors taught you?
- What reproducibility fingerprint did you leave?

---

## 🪄 Devcontainer Setup

Launch in GitHub Codespaces or locally:
- Python 3.11 image
- Pre-installed: `boto3`, `requests`, `python-dotenv`
- VS Code extensions for formatting and linting

See [`devcontainer/devcontainer.json`](devcontainer/devcontainer.json) for details.

---

## 🔐 AWS Credential Setup

Create a `.env` file with your credentials:
```env
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_DEFAULT_REGION=us-east-1