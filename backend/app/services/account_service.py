from sqlalchemy.orm import Session

from app.models.account import Account


def get_user_accounts(db: Session, user_id: int):
    return (
        db.query(Account)
        .filter(Account.user_id == user_id, Account.status == "Active")
        .order_by(Account.account_number)
        .all()
    )


def get_account_by_number(db: Session, account_number: str):
    return db.query(Account).filter(Account.account_number == account_number).first()
