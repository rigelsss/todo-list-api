from db import get_connection

def get_user_by_email(email: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
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
    