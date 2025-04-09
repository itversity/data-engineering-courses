---
title: "Lecture 0: VS Code Setup for Data Engineering on GCP"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## 🎯 Lecture Objective

> **Why is this important?**

Before diving into building data pipelines and cloud services on GCP, you need a **solid local development setup**. This foundational step ensures you can:

✅ Write and run Python code confidently  
✅ Use **VS Code** as your primary IDE for productivity  
✅ Maintain compatibility across **Mac and Windows**  
✅ Seamlessly transition from local to cloud-based workflows  
✅ Follow consistent project structures with industry best practices

> ⚡ **Real-World Relevance:**  
Many GCP services like Cloud Functions, Cloud Run, and Dataflow start from **local Python scripts**. A properly configured environment helps you **test locally** before deploying to the cloud.


---

## 🛠️ What Will We Do?

You will learn to:

✅ Set up Python 3.11+ on your machine  
✅ Use Git Bash (Windows) as a Linux emulator  
✅ Configure VS Code with the right extensions and settings  
✅ Create a structured project folder  
✅ Set up a Python virtual environment  
✅ Create and run your first Python script  
✅ Integrate the correct Python interpreter

---

## 💻 Pre-requisites

- Python 3.11 or 3.12 installed
- VS Code installed
- Git Bash installed (Windows only)
- Familiarity with basic terminal commands

---

## 🐍 Validate Python Installation

### Run in Terminal:

```bash
python3.11 --version
python3.12 --version
```

> ⚠️ If not installed, download from: https://www.python.org/downloads/

---

## 🧪 Why Git Bash on Windows?

> Native PowerShell may not behave like Unix.

✅ Git Bash simulates a **Linux-like shell**  
✅ Works better with scripting and Python tooling  
✅ Compatible with most GCP CLI tools

👉 Install from: https://git-scm.com/downloads

---

## ⚙️ Setup VS Code

1. Install VS Code from https://code.visualstudio.com/
2. Install Python Extension by Microsoft
3. (Windows only) Configure Git Bash as default terminal

---

## 🧭 Set Git Bash as Default Terminal (Windows)

1. Press `Ctrl+Shift+P` → "Preferences: Open Settings (UI)"  
2. Search for `Terminal > Integrated > Default Profile`  
3. Select **Git Bash**

---

## 📁 Create Project Directory

```bash
cd ~
mkdir -p Projects/data-engineering-on-gcp
cd Projects/data-engineering-on-gcp
code .
```

> This will open the folder directly in VS Code

---

## 🐍 Set Up Virtual Environment

```bash
python3.11 -m venv deg-venv
```

### Activate:

- **Mac/Linux**
```bash
source deg-venv/bin/activate
```

- **Windows (Git Bash)**
```bash
source deg-venv/Scripts/activate
```

---

## 🗂 Build App Structure

```bash
mkdir -p apps/hello_world
cd apps/hello_world
echo 'print("Hello World")' > hw.py
```

> You just created your first simple Python app!

---

## 🧠 Link Python Interpreter

In VS Code:

1. Open Command Palette → `Python: Select Interpreter`  
2. Choose:  
   - `deg-venv/bin/python` (Mac/Linux)  
   - `deg-venv/Scripts/python.exe` (Windows)

> Ensures your script uses the virtual environment

---

## ▶️ Run Your Python Script

Open `hw.py` and run:

```bash
python hw.py
```

✅ Output:
```
Hello World
```

---

## ✅ Recap & Validation

Make sure you:

- [x] Installed Python 3.11 or 3.12  
- [x] Installed VS Code + Python Extension  
- [x] (Windows) Set Git Bash as terminal  
- [x] Created `Projects/data-engineering-on-gcp`  
- [x] Created & activated `deg-venv`  
- [x] Built folder `apps/hello_world` with `hw.py`  
- [x] Linked VS Code to the interpreter  
- [x] Ran the script and saw output

---

## 🚀 What’s Next?

Now that your environment is ready, we’ll start building actual data pipelines and services using:

- Python
- GCP Storage & Pub/Sub
- Cloud Functions & Cloud Run
- BigQuery

👉 Let’s get coding!
