from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database.connection import Base


class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True)

    transaction_id = Column(String(50), unique=True, nullable=False)

    source_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)

    destination_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)

    amount = Column(Numeric(12, 2), nullable=False)

    request_reference = Column(String(100), unique=True, nullable=False)

    status = Column(String(20), nullable=False, default="Pending")

    created_at = Column(DateTime, nullable=False, server_default=func.now())
