from db import get_cursor

def get_user_by_email(email: str):
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return cursor.fetchone()

    
def get_user_by_id(user_id: int):
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()

def create_user(name: str, email: str, hashed_password: str):
    with get_cursor() as cursor:
        cursor.execute("INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s) RETURNING id, name, email", (name, email, hashed_password))
        created_user = cursor.fetchone()
        return created_user



def create_todo(user_id: int, title: str, description: str):
    with get_cursor() as cursor:
        cursor.execute("INSERT INTO todos (user_id, title, description) VALUES (%s, %s, %s) RETURNING id, title, description, is_completed", (user_id, title, description,))
        todo_created = cursor.fetchone()
        return todo_created

def get_todos_by_user(user_id: int, limit: int, offset: int):
    with get_cursor() as cursor:
        cursor.execute("SELECT id, title, description, is_completed FROM todos WHERE user_id = %s ORDER BY id LIMIT %s OFFSET %s", (user_id, limit, offset))
        todos = cursor.fetchall()
        return todos

def count_todos_by_user(user_id: int):
    with get_cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM todos WHERE user_id = %s", (user_id,))
        count = cursor.fetchone()[0]
        return count

def get_todo_by_id(todo_id: int):
    with get_cursor() as cursor:
        
        cursor.execute("SELECT id, user_id, title, description, is_completed FROM todos WHERE id = %s", (todo_id,))
        todo = cursor.fetchone()
        return todo


def update_todo(todo_id: int, fields: dict):
    set_clauses = []
    values = []
    
    for column, value in fields.items():
        set_clauses.append(f"{column} = %s")
        values.append(value)
        
    set_clause = ", ".join(set_clauses)
    values.append(todo_id)
    
    with get_cursor() as cursor:
        cursor.execute(f"UPDATE todos SET {set_clause} WHERE id = %s RETURNING id, title, description, is_completed", values)
        updated_todo = cursor.fetchone()   
        return updated_todo


def delete_todo(todo_id: int):
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
        return 
    
