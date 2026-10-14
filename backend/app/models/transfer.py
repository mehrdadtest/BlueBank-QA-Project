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


class Transfer(Base):
    __tablename__ = "transfers"

    __table_args__ = (
        CheckConstraint(
            "amount >= 0.01 AND amount <= 10000",
            name="chk_transfer_amount",
        ),
        CheckConstraint(
            "source_account_id <> destination_account_id",
            name="chk_different_accounts",
        ),
        CheckConstraint(
            "status IN ('Pending', 'Successful', 'Failed', 'Cancelled')",
            name="chk_transfer_status",
        ),
    )

    id = Column(Integer, primary_key=True)

    transaction_id = Column(String(50), unique=True, nullable=False)

    source_account_id = Column(
        Integer,
        ForeignKey("accounts.id", name="fk_transfer_source"),
        nullable=False,
    )

    destination_account_id = Column(
        Integer,
        ForeignKey("accounts.id", name="fk_transfer_destination"),
        nullable=False,
    )

    amount = Column(Numeric(12, 2), nullable=False)

    request_reference = Column(String(100), unique=True, nullable=False)

    status = Column(String(20), nullable=False, default="Pending")

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
