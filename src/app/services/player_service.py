from app.domain.player import Player
from app.repository.player_repository import PlayerRepository
import bcrypt


class PlayerService:
    """Service responsible for player management, including registration, login, and guest play."""

    def __init__(self):
        self.player_repository = PlayerRepository()

    def register(self, name: str, password: str):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        player = Player(name)
        player.password_hash = hashed_password
        self.player_repository.save_player(player)

    def login(self, name: str, password: str):
        bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        pass

    def play_as_guest(self, name: str) -> Player:
        player = Player(name, guest=True)
        return player