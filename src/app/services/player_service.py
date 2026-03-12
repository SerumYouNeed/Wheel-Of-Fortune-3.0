from app.domain.player import Player

class PlayerService:
    """Service responsible for player management, including registration, login, and guest play."""

    def register(self, name: str, password: str):
        # hash password
        # save to DB
        pass

    def login(self, name: str, password: str):
        # verify password
        # return Player
        pass

    def play_as_guest(self, name: str) -> Player:
        player = Player(name, guest=True)
        return player

    def new_player(self, name: str) -> Player:
        return Player(name)