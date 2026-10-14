from sqlalchemy.orm import Session, aliased

from app.models.account import Account
from app.models.transaction import Transaction


def get_user_transactions(db: Session, user_id: int):
    source_account = aliased(Account)
    destination_account = aliased(Account)

    return (
        db.query(
            Transaction.transaction_id.label("transaction_id"),
            source_account.account_number.label("source_account_number"),
            destination_account.account_number.label("destination_account_number"),
            Transaction.amount.label("amount"),
            Transaction.status.label("status"),
            Transaction.created_at.label("created_at"),
        )
        .join(
            source_account,
            Transaction.source_account_id == source_account.id,
        )
        .join(
            destination_account,
            Transaction.destination_account_id == destination_account.id,
        )
        .filter(
            (source_account.user_id == user_id)
            | (destination_account.user_id == user_id)
        )
        .order_by(Transaction.created_at.desc(), Transaction.id.desc())
        .all()
    )
