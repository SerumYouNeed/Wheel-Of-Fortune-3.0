from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.player import Player


class PlayerRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, player: Player) -> Player:
        self.db.add(player)
        self.db.commit()
        self.db.refresh(player)
        return player

    def get_by_name(self, name: str) -> Player | None:
        return self.db.scalar(select(Player).where(Player.name == name))