import psycopg2
import dotenv
import os

# dotenv.load_dotenv()
# conn_string = os.getenv("DB_CONN_STRING")
conn_string = "postgresql://neondb_owner:v1n2ktZwMjxL@ep-restless-truth-a2tidnlv.eu-central-1.aws.neon.tech/neondb?sslmode=require"
class DB:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(conn_string)
            self.cursor = self.conn.cursor()
            self.create_tables()
            self.conn.commit()
        except Exception as e:
            print(e)


    def create_tables(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS players(
                    id SERIAL PRIMARY KEY,
                    email VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    username VARCHAR(255) NOT NULL);
            """)

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS games(
            id SERIAL PRIMARY KEY,
            player1_id INTEGER NOT NULL,
            game_mode VARCHAR(255) NOT NULL,
            score1 INTEGER NOT NULL,
            start_time TIMESTAMP NOT NULL,
            end_time TIMESTAMP NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE);""")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def register_player(self, email, password, username):
        try:
            self.cursor.execute("""
                INSERT INTO players (email, contrasena, username) VALUES (%s, %s, %s);
            """, (email, password, username))
            self.conn.commit()
        except Exception as e:
            print(e)

    def login_player(self, email, password):
        try:
            self.cursor.execute("""
                SELECT * FROM players WHERE email = %s AND contrasena = %s;
            """, (email, password))
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
            return None


    def save_game(self, player_id, game_mode, score):
        try:
            self.cursor.execute("""
                INSERT INTO games (player_id, game_mode, score) VALUES (%s, %s, %s);
            """, (player_id, game_mode, score))
            self.conn.commit()
        except Exception as e:
            print(e)

    def get_best_games_by_gamemode(self, game_mode):
        try:
            self.cursor.execute("""
                SELECT * FROM games WHERE game_mode = %s ORDER BY score DESC LIMIT 5;
            """, (game_mode,))
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":
    db = DB()
    db.save_game(1, "led", 826)
