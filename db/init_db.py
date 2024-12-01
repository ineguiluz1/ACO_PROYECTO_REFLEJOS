import psycopg2
from dotenv import load_dotenv
import os
from ACO_PROYECTO_REFLEJOS.db import authManager as auth

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
        cur = conn.cursor()
        return conn, cur
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

# Define a function to create all the tables
def create_tables(conn, cur):
    try:

        create_user_table = """
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL
        );
        """

        create_game_table = """
        CREATE TABLE IF NOT EXISTS games (
            id SERIAL PRIMARY KEY,
            player_id INT NOT NULL,
            game_mode VARCHAR(50) NOT NULL,
            score INT NOT NULL,
            start_date TIMESTAMP NOT NULL,
            end_date TIMESTAMP NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
        );
        """

        # Create the tables
        cur.execute(create_user_table)
        cur.execute(create_game_table)

        # Commit the changes to the database
        conn.commit()

        print("Table 'users' created or already exists.")
        print("Table 'games' created or already exists.")

    except Exception as e:
        print("Error creating the table:", e)


# Define the function to initialize the database
def initialize_db():
    conn, cur = create_connection()
    if conn is None or cur is None:
        return

    try:

        # Create the tables
        create_tables(conn, cur)

        # Register a user
        auth.register("admin", "admin@mail.com", "admin", cur, conn)
        # Commit the changes to the database
        conn.commit()


    except Exception as e:
        print("Error creating the table:", e)

    finally:
        cur.close()  # Ensure cursor is closed before connection
        conn.close()  # Ensure the connection is closed
        print("Connection closed")





