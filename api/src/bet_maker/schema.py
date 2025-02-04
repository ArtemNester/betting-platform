from decimal import Decimal

from pydantic import BaseModel, Field

from src.status import EventStatus


class BetSchema(BaseModel):
    id: int
    user_id: int
    event_id: int
    amount: Decimal = Field(..., gt=0)
    status: EventStatus

    class Config:
        from_attributes = True


class BetCreateSchema(BaseModel):
    user_id: int
    event_id: int
    amount: Decimal = Field(..., gt=0)
