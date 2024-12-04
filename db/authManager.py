import psycopg2
from dotenv import load_dotenv
import os

def login(email, password, cur)->bool:
    try:
        # Execute the query
        cur.execute("""
            SELECT * FROM users
            WHERE email = %s AND password = %s;
        """, (email, password))

        user = cur.fetchone()

        if user is not None:
            return True
        else:
            return False

    except Exception as e:
        print("Error executing the query:", e)
        return False

def register(username, email, password, cur, conn):
    try:
        # Execute the query
        cur.execute("""
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s);
        """, (username, email, password))

        # Commit the changes to the database
        conn.commit()

        print("User registered successfully")

    except Exception as e:
        print("Error executing the query:", e)
        return False