from fastapi import Depends
from sqlalchemy.orm import Session

from app.repository.db import get_db
from app.repository.player_repository import PlayerRepository
from app.services.player_service import PlayerService


def get_player_service(db: Session = Depends(get_db)) -> PlayerService:
    return PlayerService(PlayerRepository(db))