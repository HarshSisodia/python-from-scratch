# Virtual Environment
'''
# Virtual Environment

## What is a Virtual Environment?

A **Virtual Environment** is an isolated workspace for a Python project. It creates a separate environment where you can install the libraries and packages required for that project without affecting the Python installation on your computer or other projects.

Think of it as giving every Python project its own personal workspace.

---

## Why Do We Need a Virtual Environment?

Imagine you're working on two different Python projects.

- **Project A** requires **Pandas 3.0.5**
- **Project B** requires **Pandas 1.5.0**

If you install both versions globally, they may conflict with each other, and one of your projects might stop working.

A virtual environment solves this problem by creating a separate environment for each project. This allows every project to use its own package versions independently.

---

## Real-Life Example

Suppose you're working on these two projects:

### Project A (Data Analysis)

Required packages:

- Pandas 3.0.5
- NumPy 2.4.6

### Project B (Old College Project)

Required packages:

- Pandas 1.5.0
- NumPy 1.23.5

Without a virtual environment, installing one version could overwrite the other.

With virtual environments, both projects work perfectly because each project has its own isolated packages.

---

## Create a Virtual Environment

### macOS / Linux

```bash
python3 -m venv myenv
```

### Windows

```bash
python -m venv myenv
```

This command creates a new folder named **myenv** that contains a separate Python environment.

---

## Activate the Virtual Environment

### macOS / Linux

```bash
source myenv/bin/activate
```

### Windows

```bash
myenv\Scripts\activate
```

After activation, your terminal will look something like this:

```text
(myenv) username@computer Project %
```

The **(myenv)** at the beginning tells you that the virtual environment is currently active.

---

## Install Packages

Once the environment is activated, install the packages your project needs.

```bash
pip install pandas
```

Install multiple packages:

```bash
pip install pandas numpy matplotlib
```

These packages are installed **only inside the virtual environment**, not in your global Python installation.

---

## Check Installed Packages

```bash
pip list
```

This displays all packages installed in the current virtual environment.

---

## Save Project Dependencies

Before sharing your project, save all installed packages in a file.

```bash
pip freeze > requirements.txt
```

This creates a **requirements.txt** file containing all project dependencies.

Example:

```text
numpy==2.4.6
pandas==3.0.5
matplotlib==3.10.5
```

---

## Install Packages from requirements.txt

If someone else downloads your project, they can install all required packages using:

```bash
pip install -r requirements.txt
```

This installs every package listed in the **requirements.txt** file.

---

## Verify the Installation

```python
import pandas as pd

print(pd.__version__)
```

Example Output:

```text
3.0.5
```

---

## Deactivate the Virtual Environment

When you're done working on your project, deactivate the environment.

```bash
deactivate
```

Your terminal prompt will return to its normal state.

---

## Delete a Virtual Environment

If you no longer need the environment, simply delete its folder.

macOS / Linux

```bash
rm -rf myenv
```

Windows

Delete the **myenv** folder manually or run:

```cmd
rmdir /s myenv
```

---

# Project Structure

```text
Data-Analysis-Project/
│
├── myenv/
├── app.py
├── requirements.txt
├── data.csv
└── README.md
```

The **myenv** folder stores the project's isolated Python environment, while **requirements.txt** keeps a list of all the packages needed to run the project.

---

# Key Points to Remember

- A virtual environment creates an isolated Python workspace for a project.
- Every Python project should have its own virtual environment.
- Always activate the environment before installing packages.
- Install only the packages required for your current project.
- Use **requirements.txt** to share project dependencies with others.
- Deactivate the environment after finishing your work.

---

# Quick Workflow

```bash
# Create a project folder
mkdir Data-Analysis

# Move into the project
cd Data-Analysis

# Create a virtual environment
python3 -m venv myenv

# Activate it
source myenv/bin/activate

# Install required packages
pip install pandas numpy matplotlib

# Save dependencies
pip freeze > requirements.txt

# Run your Python file
python app.py

# Deactivate the environment
deactivate
```

---

## One-Line Definition

> **A Virtual Environment is an isolated Python workspace that allows each project to have its own packages and dependencies without affecting other Python projects or the global Python installation.**
'''




# ----------------------------------------------------------------------------------------------------------------------------------#




#The "requirement.txt" file
'''
--

# The `requirements.txt` File

A **requirements.txt** file stores a list of all the Python packages and their versions that a project depends on.

Instead of installing each package one by one, you can save them in a single file and install everything with one command. This makes it easy to share your project with others and ensures everyone uses the same package versions.

---

## Why Do We Use `requirements.txt`?

- Keeps track of all project dependencies.
- Makes it easy to share your project.
- Saves time when setting up the project on another computer.
- Ensures everyone installs the same package versions.

---

## Create a `requirements.txt` File

After installing all the required packages, run:

```bash
pip freeze > requirements.txt
```

This command creates a file named **requirements.txt** containing all the installed packages and their versions.

Example:

```text
numpy==2.4.6
pandas==3.0.5
matplotlib==3.10.5
python-dateutil==2.9.0.post0
six==1.17.0
```

---

## Install Packages from `requirements.txt`

If someone downloads your project, they don't need to install every package manually.

They simply run:

```bash
pip install -r requirements.txt
```

This command installs every package listed in the **requirements.txt** file.

---

## Real-Life Example

Imagine you build a Data Science project using these libraries:

- Pandas
- NumPy
- Matplotlib

Instead of telling your friend:

> Install Pandas, then NumPy, then Matplotlib...

You simply send your project with the **requirements.txt** file.

Your friend only needs to run:

```bash
pip install -r requirements.txt
```

Within a few minutes, all the required packages are installed automatically with the correct versions.

---

## Project Structure

```text
Data-Analysis-Project/
│
├── myenv/
├── app.py
├── requirements.txt
└── README.md
```

The **requirements.txt** file makes your project easy to set up on any computer.

---

## Key Points to Remember

- `pip freeze` saves all installed packages and their versions.
- `requirements.txt` helps recreate the same environment on another machine.
- Always create or update this file before sharing your project.
- Install all dependencies using `pip install -r requirements.txt`.

'''