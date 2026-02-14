from datetime import date
from sqlalchemy import String, Float, Date
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    date: Mapped[str] = mapped_column(Date, default=date.today())

def create_transaction(amount, description, category):
    if amount > 0 and description and category:
        new_transaction = Transaction(amount=amount, description=description, category=category)
        return new_transaction