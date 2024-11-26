class Game:
    def __init__(self, player_id, game_mode, score, start_date, end_date):
        self.player_id = player_id
        self.game_mode = game_mode
        self.score = score
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"{self.player_id} {self.game_mode} {self.score} {self.start_date} {self.end_date}"