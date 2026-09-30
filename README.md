# Todo List API

A REST API for managing tasks (todos) with JWT-based user authentication. Based on the [Todo List API project from roadmap.sh](https://roadmap.sh/projects/todo-list-api).

## Technologies

- Python
- FastAPI
- PostgreSQL (via Docker)
- psycopg2
- PyJWT (JWT authentication)
- passlib/bcrypt (password hashing)

## Features

- User registration and login with JWT token generation
- Authenticated CRUD for todos
- Pagination on the todo list
- Owner-based authorization: updating or deleting another user's todo returns `403 Forbidden`

## Project structure

```
.
├── main.py
├── db.py
├── auth.py
├── crud.py
├── schemas.py
├── schema.sql
├── docker-compose.yml
└── routers/
    ├── auth_router.py
    └── todos_router.py
```

## Prerequisites

- Python 3.x
- Docker

## Getting started

1. Start the database:

   ```bash
   docker compose up -d
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the [environment variables](#environment-variables).

5. Apply the schema to the database (PowerShell/Windows command):

   ```powershell
   Get-Content .\schema.sql | docker exec -i todo_api_db psql -U todo_user -d todo_db
   ```

6. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

7. Open the interactive docs at http://127.0.0.1:8000/docs

## Environment variables

| Variable      |
| ------------- |
| `DB_HOST`     |
| `DB_PORT`     |
| `DB_NAME`     |
| `DB_USER`     |
| `DB_PASSWORD` |
| `SECRET_KEY`  |

## Endpoints

| Method | Route         | Description                                  |
| ------ | ------------- | -------------------------------------------- |
| POST   | `/register`   | Registers a new user and returns a token     |
| POST   | `/login`      | Authenticates the user and returns a token   |
| POST   | `/todos`      | Creates a new todo                           |
| GET    | `/todos`      | Lists the user's todos, with pagination      |
| PUT    | `/todos/{id}` | Updates a todo (owner only)                  |
| DELETE | `/todos/{id}` | Deletes a todo (owner only)                  |

The `/todos` routes require the `Authorization: Bearer <token>` header.
