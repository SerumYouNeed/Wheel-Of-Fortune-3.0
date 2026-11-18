import bcrypt

from app.models.player import Player
from app.repository.player_repository import PlayerRepository


class PlayerAlreadyExists(Exception):
    pass


class PlayerService:
    def __init__(self, repository: PlayerRepository):
        self.repository = repository

    def register(self, name: str, password: str) -> Player:
        name = name.strip().upper()
        if self.repository.get_by_name(name):
            raise PlayerAlreadyExists(name)
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        return self.repository.add(Player(name=name, password_hash=hashed))

    def login(self, name: str, password: str) -> Player | None:
        player = self.repository.get_by_name(name.strip().upper())
        if player is None:
            return None
        if bcrypt.checkpw(password.encode("utf-8"), player.password_hash.encode("utf-8")):
            return player
        return None