import decimal

from src.infrastructure.database import Base
from sqlalchemy import ForeignKey, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.status import EventStatus


class Bets(Base):
    __tablename__ = 'bets'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey('events.id'), nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[EventStatus] = mapped_column(Enum(EventStatus), nullable=False)

    user = relationship('User', back_populates='bets')
    event = relationship('Event', back_populates='bets')

    def __repr__(self):
        return f'<Bet(id={self.id}), status={self.status}>'
