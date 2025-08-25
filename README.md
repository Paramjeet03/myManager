# MyManager

**MyManager** is a full-stack Task and Account Management System built with a modern frontend and a secure backend. It provides role-based access, CRUD operations for tasks and users, and maintains daily logs for accountability.

---

## Table of Contents

- [Features](#features)  
- [Technology Stack](#technology-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [API Endpoints](#api-endpoints)  
- [Authentication & Authorization](#authentication--authorization)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- **User Roles:** Admin and regular user roles.  
- **Task Management:** Create, read, update, delete tasks.  
- **Account Management:** Admin can manage user accounts.  
- **Daily Logs:** Automatic logging of actions for accountability.  
- **JWT Authentication:** Secure login system.  
- **Responsive Frontend:** Built with HTML, CSS, JS, and Tailwind.  
- **RESTful API:** Backend API powered by FastAPI.  

---

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript, Tailwind CSS  
- **Backend:** Python with FastAPI  
- **Database:** MySQL  
- **Authentication:** JWT (JSON Web Tokens)  
- **Dependencies:** Listed in `requirements.txt`  

---

## Installation

1. **Clone the repository**  
```bash
git clone https://github.com/Paramjeet03/myManager.git
cd myManager
```

2. **Setup Python virtual environment**  
```bash
python -m venv env
```

3. **Activate environment**  
- Windows:  
```bash
env\Scripts\activate
```  
- Linux/Mac:  
```bash
source env/bin/activate
```

4. **Install backend dependencies**  
```bash
pip install -r requirements.txt
```

5. **Setup MySQL database**  
- Create a database, e.g. `mymanager`  
- Create a DB user with privileges on that DB  
- Configure your connection string in `database.py` or via `.env` file:  
  ```env
  DB_HOST=localhost
  DB_PORT=3306
  DB_USER=your_user
  DB_PASSWORD=your_password
  DB_NAME=mymanager
  ```

6. **Run the backend server**  
```bash
uvicorn main:app --reload
```

7. **Open frontend**  
- Open `frontend/index.html` in your browser to access the UI.  

---

## Usage

- Admin can manage all tasks and users.  
- Regular users can manage their own tasks.  
- Logs are automatically generated for all actions.  
- JWT tokens are required for API calls from the frontend.  

---

## API Endpoints

**Authentication:**  
- `POST /auth/login` – Login and receive JWT token  

**Tasks:**  
- `GET /tasks` – List all tasks  
- `POST /tasks` – Create a new task  
- `PUT /tasks/{id}` – Update task by ID  
- `DELETE /tasks/{id}` – Delete task by ID  

**Users:**  
- `GET /users` – List all users (Admin only)  
- `POST /users` – Create new user (Admin only)  
- `PUT /users/{id}` – Update user (Admin only)  
- `DELETE /users/{id}` – Delete user (Admin only)  

**Logs:**  
- `GET /logs` – View all logs  

> Swagger documentation available at `http://127.0.0.1:8000/docs`.  

---

## Authentication & Authorization

- Users must log in to receive JWT tokens.  
- Admins have full access.  
- Regular users have limited access based on roles.  

---

## Project Structure

```
TASK_MANAGMENT2.0/
│
├── task_managment_env/       # Local Python virtual environment (should be gitignored)
├── .env                      # Environment variables (DB credentials, etc.)
├── requirment.txt            # Python dependencies
├── package.json              # Node.js dependencies (if any frontend tooling)
├── package-lock.json
│
├── Frontend/                 # Frontend UI
│   ├── dist/
│   │   ├── graphics/
│   │   └── stylesheet/
│   ├── Account.html
│   ├── index.html
│   ├── log.html
│   ├── login.html
│   ├── mainDashboard.html
│   └── Task.html
│   └── node_modules/         # Node dependencies
│
├── src/                      # Backend Python source
│   ├── main.py               # FastAPI entrypoint
│   │
│   ├── api/                  # API route files
│   │   ├── adminGetAlltask.py
│   │   ├── createAccount.py
│   │   ├── deleteAccount.py
│   │   ├── get_all_api.py
│   │   ├── getalllogadm.py
│   │   ├── getLogadmin.py
│   │   ├── getlogUser.py
│   │   ├── login.py
│   │   ├── personal_account.py
│   │   ├── readAccount.py
│   │   ├── report.py
|   |   ├── Welcome.py
│   |   ├── updateLog.py
│   │   ├── see_task_by_mail.py
│   │   ├── seeTask.py
│   │   ├── setLog.py
│   │   ├── taskAssign.py
│   │   ├── taskDeletion.py
│   │   └── taskUpdate.py
│   │
│   ├── Auth/                 # Authentication modules
│   │   ├── Authentication.py
│   │   ├── Authorization.py
│   │   └── Hashing_token.py
│   │
│   ├── Config/
│   │   └── Config.py
│   │
│   ├── CRUD/                 # CRUD operations
│   │   ├── Admin_crud.py
│   │   ├── reportCrud.py
│   │   └── User_crud.py
│   │
│   ├── Database/             # Database models and sessions
│   │   ├── db_model.py
│   │   └── session.py
│   │
│   ├── Dependency/
│   │   └── dependancy.py
│   │
│   ├── Enum_modal/
│   │   └── Enum.py
│   │
│   ├── pydantic_schema/      # Pydantic schemas
│   │   ├── task_pydantic.py
│   │   ├── User_log_pydantic.py
│   │   ├── User_pydantic.py
│   │   ├── User_log_pydantic.cpython-311.pyc
│   │   ├── task_pydantic.cpython-311.pyc
│   │   └── User_pydantic.cpython-311.pyc
│   │
│   |
│   │
│   ├── .env
│   └── Task_managment_venv
│
└── .vscode/ 
```

---

## Contributing

1. Fork the repository  
2. Create a branch (`git checkout -b feature-name`)  
3. Make your changes  
4. Commit (`git commit -m "Description"`)  
5. Push (`git push origin feature-name`)  
6. Create a Pull Request  

---

## License

This project is licensed under the **MIT License**.
