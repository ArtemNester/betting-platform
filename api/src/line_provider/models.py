import decimal

from src.infrastructure.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric

class Events(Base):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    coefficient: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    bets = relationship('Bet', back_populates='event')