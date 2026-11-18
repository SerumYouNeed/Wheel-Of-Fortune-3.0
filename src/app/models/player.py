import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.repository.db import Base


class Player(Base):
    __tablename__ = "players"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    score: Mapped[int] = mapped_column(default=0)
    password_hash: Mapped[str] = mapped_column(String(60))