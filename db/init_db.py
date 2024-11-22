import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connection String
conn_string = os.getenv("DB_CONN_STRING")

if conn_string is None:
    print("No connection string found in the environment variables")


# Function to create the connection
def create_connection():
    try:
        conn = psycopg2.connect(conn_string)
        print("Connection established")
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

# Define a function to create all the tables
def create_tables(conn, cur):
    try:
        # Create the table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE NOT NULL
            );
        """)

        # Commit the changes to the database
        conn.commit()

        print("Table 'users' created or already exists.")

    except Exception as e:
        print("Error creating the table:", e)


# Define the function to initialize the database
def initialize_db():
    conn = create_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()

        # Create the tables
        create_tables(conn, cur)

        # Commit the changes to the database
        conn.commit()

    except Exception as e:
        print("Error creating the table:", e)

    finally:
        cur.close()  # Ensure cursor is closed before connection
        conn.close()  # Ensure the connection is closed
        print("Connection closed")





