from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, field_validator

PlayerName = Annotated[
    str, StringConstraints(strip_whitespace=True, min_length=3, max_length=50)
]


class PlayerCreate(BaseModel):
    name: PlayerName
    password: str = Field(min_length=8)

    @field_validator("password")
    @classmethod
    def password_fits_bcrypt(cls, v: str) -> str:
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password must be at most 72 bytes long")
        return v


class PlayerLogin(BaseModel):
    name: str
    password: str


class PlayerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    score: int

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"