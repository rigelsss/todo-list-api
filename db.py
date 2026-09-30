from dotenv import load_dotenv
import os
import psycopg2
from contextlib import contextmanager

load_dotenv()

def get_connection():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return connection

@contextmanager
def get_cursor():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    except:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()