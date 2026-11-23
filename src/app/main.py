from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import players
from app.models import player  # noqa: F401  (rejestruje model w Base.metadata)
from app.repository.db import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(title="Wheel of Fortune", lifespan=lifespan)
app.include_router(players.router)

