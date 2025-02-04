from decimal import Decimal

from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id: int
    username: str
    balance: Decimal = Field(..., gt=0)

    class Config:
        from_attributes = True
