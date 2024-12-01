import psycopg2
import clases.game
import clases.player
from clases import player


def save_game(conn, cur, game):
    """
    Saves a game to the database
    
    Parameters:
        - Database connection object
        - Database cursor object
        - Game object
    """

    query = """
    INSERT INTO games (player_id, game_mode, score, start_date, end_date)
    VALUES (%s, %s, %s, %s, %s);
    """

    try:
        cur.execute(query, (game.id, game.mode, game.score, game.start_date, game.end_date))
        conn.commit()
    except Exception as e:
        print("Error saving game: ", e)

def query_best_games(conn, cur, game_mode):

    """
    Queries the database for all games whose mode is game_mode and returns the 3 best games

    Parameters:
        - Database connection object
        - Database cursor object
        - game mode to filter by

    """
    query = """
    SELECT *
    FROM games
    WHERE game_mode = %s
    ORDER BY score DESC
    LIMIT 3;
    """

    try:
        cur.execute(query, (game_mode,))
        top_games = cur.fetchall()
        return top_games
    except Exception as e:
        print("Error querying best games: ", e)


def query_best_players_game_mode(conn, cur, game_mode):

    """
    Queries the database for all games whose mode is game_mode and returns the 3 best players
    for that game mode

    Parameters:
    - Database connection object
    - Database cursor object
    - game mode to filter by
    """


    query = """
    SELECT p.id AS player_id, p.username, MAX(g.score) AS highest_score
    FROM players p
    JOIN games g ON p.id = g.player_id
    WHERE g.game_mode = %s
    GROUP BY p.id, p.username
    ORDER BY highest_score DESC
    LIMIT 3;
    """
    try:
        cur.execute(query, (game_mode,))
        best_players = cur.fetchall()
        return best_players
    except Exception as e:
        print("Error querying best games: ", e)


