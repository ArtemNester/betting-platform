import decimal

from src.infrastructure.database import Base
from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    balance: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2))

    bets = relationship('Bet', back_populates='user')
