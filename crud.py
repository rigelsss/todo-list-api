from db import get_connection

def get_user_by_email(email: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def get_user_by_id(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def create_user(name: str, email: str, hashed_password: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s) RETURNING id, name, email", (name, email, hashed_password))
    user = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return user

def create_todo(user_id: int, title: str, description: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todos (user_id, title, description) VALUES (%s, %s, %s) RETURNING id, title, description, is_completed", (user_id, title, description,))
    todo_created = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return todo_created

def get_todos_by_user(user_id: int, limit: int, offset: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, description, is_completed FROM todos WHERE user_id = %s ORDER BY id LIMIT %s OFFSET %s", (user_id, limit, offset))
    todos = cursor.fetchall()
    cursor.close()
    connection.close()
    return todos

def count_todos_by_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM todos WHERE user_id = %s", (user_id,))
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count