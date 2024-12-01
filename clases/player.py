class Player:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'Player {self.id} {self.username} {self.password} {self.email}'