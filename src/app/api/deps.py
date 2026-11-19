from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.models.player import Player
from app.repository.db import get_db
from app.repository.player_repository import PlayerRepository
from app.services.player_service import PlayerService

bearer = HTTPBearer()


def get_player_service(db: Session = Depends(get_db)) -> PlayerService:
    return PlayerService(PlayerRepository(db))


def get_current_player(
    credentials: HTTPAuthorizationCredentials = Depends(bearer),
    db: Session = Depends(get_db),
) -> Player:
    player_id = decode_access_token(credentials.credentials)
    player = PlayerRepository(db).get_by_id(player_id) if player_id else None
    if player is None:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return player