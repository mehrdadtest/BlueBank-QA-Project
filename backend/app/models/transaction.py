from sqlalchemy import (
    CheckConstraint,
    Column,
    Integer,
    String,
    Numeric,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func

from app.database.connection import Base


class Transaction(Base):
    __tablename__ = "transactions"

    __table_args__ = (
        CheckConstraint(
            "status IN ('Successful', 'Failed', 'Cancelled')",
            name="chk_transaction_status",
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(String(50), unique=True, nullable=False)

    transfer_id = Column(
        Integer,
        ForeignKey("transfers.id", name="fk_transaction_transfer"),
        nullable=False,
    )

    source_account_id = Column(
        Integer,
        ForeignKey("accounts.id", name="fk_transaction_source"),
        nullable=False,
    )

    destination_account_id = Column(
        Integer,
        ForeignKey("accounts.id", name="fk_transaction_destination"),
        nullable=False,
    )

    amount = Column(Numeric(12, 2), nullable=False)

    status = Column(String(20), nullable=False)

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
