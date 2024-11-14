# Task Management Web Application

A simple task management application built with Django, where users can create, manage, and track tasks with various attributes, including status, priority, due date, and category. Users can also register and log in to have a personalized task management experience.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Environment Variables](#environment-variables)
5. [Deployment](#deployment)
6. [Built With](#built-with)
7. [License](#license)

---

## Features

- **User Authentication**: Register, log in, and manage a personalized list of tasks.
- **CRUD for Tasks**: Create, read, update, and delete tasks.
- **Task Attributes**:
  - **Title** and **Description**
  - **Status**: To Do, In Progress, Done
  - **Priority**: Low, Medium, High
  - **Due Date** (with validation to prevent past dates unless the task is marked "Done")
  - **Category**: Custom categories for organization
- **Filtering and Search**: Search by title and description, and filter tasks by category, status, and priority.
- **Responsive UI**: Built with Bootstrap for a user-friendly, responsive design.

---

## Installation

Create and Activate a Virtual Environment

```
python3 -m venv .venv
```

```
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Set Up the Database

If you’re using SQLite (default):
No setup is required; SQLite will automatically use db.sqlite3.
If using PostgreSQL:
Create a PostgreSQL database and user.
Update DATABASE_URL in your environment variables (explained below).
Apply Migrations

```
python manage.py migrate
```

Collect Static Files

```
python manage.py collectstatic --noinput
```

Run the Development Server

```python manage.py runserver

```

Your application will be available at http://127.0.0.1:8000.

### Prerequisites

- Python 3.8+
- Sqlite3
- Git

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

### Usage

### Accessing the Application

1. Homepage: Displays the list of tasks (for authenticated users).
2. Register/Login: New users can register, and existing users can log in to manage their tasks.
3. Task CRUD Operations:
   - Create Task: Click "Create New Task" to add a new task.
   - Edit Task: Click "Edit" on a task to update its details.
   - Delete Task: Click "Delete" on a task to remove it.
4. Task Filters and Search:
   - Use the search bar and filters on the homepage to find tasks by title, description, status, priority, and category.

### Built With

1. [Django] - Web framework
2. [Bootstrap] - Frontend framework for responsive design
3. [Sqlite3] - Relational database (optional for production)
