from decimal import Decimal

from pydantic import BaseModel, Field

from src.status import EventStatus


class EventSchema(BaseModel):
    id: int
    name: str
    coefficient: Decimal = Field(..., gt=0)
    status: EventStatus

    class Config:
        from_attributes = True
