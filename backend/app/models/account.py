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


class Account(Base):
    __tablename__ = "accounts"

    __table_args__ = (
        CheckConstraint(
            "balance >= 0",
            name="chk_account_balance",
        ),
        CheckConstraint(
            "account_number ~ '^[0-9]{8}$'",
            name="chk_account_number",
        ),
        CheckConstraint(
            "status IN ('Active', 'Closed', 'Blocked')",
            name="chk_account_status",
        ),
    )

    id = Column(Integer, primary_key=True)

    account_number = Column(String(8), unique=True, nullable=False)

    user_id = Column(
        Integer,
        ForeignKey("users.id", name="fk_account_user"),
        nullable=False,
    )

    status = Column(String(20), nullable=False)

    balance = Column(Numeric(12, 2), nullable=False, default=0)

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
