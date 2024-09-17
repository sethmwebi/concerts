import os

from dotenv import load_dotenv
from psycopg2 import pool

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

try:
    connection_pool = pool.SimpleConnectionPool(
        1,
        20,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )

    if connection_pool:
        print("Connection pool created successfully")
except Exception as e:
    print(f"Error creating connection pool: {e}")


def get_connection():
    """
    Retrieves a connection from the connection pool.
    Raises an error if no connection is available.
    """
    try:
        connection = connection_pool.getconn()
        if connection:
            print("Successfully retrieved a connection from the pool")
            return connection
        else:
            raise Exception("Failed to retrieve connection from pool")
    except Exception as e:
        print(f"Error getting connection: {e}")
        raise e


def close_connection(connection):
    """
    Returns a connection to the pool.
    """
    try:
        connection_pool.putconn(connection)
        print("Connection returned to the pool")
    except Exception as e:
        print(f"Error returning connection: {e}")
