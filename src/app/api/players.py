from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_current_player, get_player_service
from app.core.security import create_access_token
from app.models.player import Player
from app.schemas.player import PlayerCreate, PlayerLogin, PlayerOut, TokenOut
from app.services.player_service import PlayerAlreadyExists, PlayerService

router = APIRouter(tags=["players"])


@router.post("/players", response_model=PlayerOut, status_code=status.HTTP_201_CREATED)
def register(data: PlayerCreate, service: PlayerService = Depends(get_player_service)):
    try:
        return service.register(data.name, data.password)
    except PlayerAlreadyExists:
        raise HTTPException(status.HTTP_409_CONFLICT, "Player with this name already exists")


@router.post("/auth/login", response_model=TokenOut)
def login(data: PlayerLogin, service: PlayerService = Depends(get_player_service)):
    player = service.login(data.name, data.password)
    if player is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid name or password")
    return TokenOut(access_token=create_access_token(player.id))


@router.get("/players/me", response_model=PlayerOut)
def me(current: Player = Depends(get_current_player)):
    return current