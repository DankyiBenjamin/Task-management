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

### Prerequisites

- Python 3.8+
- PostgreSQL (if using a PostgreSQL database locally)
- Git

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
