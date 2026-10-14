import pytest
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.models.account import Account
from app.models.transfer import Transfer
from app.models.transaction import Transaction


def create_user(db, email="qa@example.com"):
    user = User(
        email=email,
        password="test-password",
        status="Active",
    )
    db.add(user)
    db.flush()
    return user


def create_account(
    db,
    user_id,
    account_number="12345678",
    balance=1000,
    status="Active",
):
    account = Account(
        account_number=account_number,
        user_id=user_id,
        balance=balance,
        status=status,
    )
    db.add(account)
    db.flush()
    return account


def create_transfer(
    db,
    source_account_id,
    destination_account_id,
    transaction_id="TRX-TEST-001",
    request_reference="REF-TEST-001",
    amount=100,
    status="Pending",
):
    transfer = Transfer(
        transaction_id=transaction_id,
        source_account_id=source_account_id,
        destination_account_id=destination_account_id,
        request_reference=request_reference,
        amount=amount,
        status=status,
    )
    db.add(transfer)
    db.flush()
    return transfer


def assert_integrity_error(db, operation):
    with pytest.raises(IntegrityError):
        operation()

    # Clear the failed transaction before the session is reused.
    db.rollback()


def test_database_rejects_duplicate_user_email(db_session):
    create_user(db_session, "duplicate@example.com")

    assert_integrity_error(
        db_session,
        lambda: create_user(db_session, "duplicate@example.com"),
    )


def test_database_rejects_negative_account_balance(db_session):
    user = create_user(db_session)

    assert_integrity_error(
        db_session,
        lambda: create_account(
            db_session,
            user.id,
            account_number="12345678",
            balance=-1,
        ),
    )


def test_database_rejects_invalid_account_number(db_session):
    user = create_user(db_session)

    assert_integrity_error(
        db_session,
        lambda: create_account(
            db_session,
            user.id,
            account_number="ABC12345",
        ),
    )


def test_database_rejects_duplicate_account_number(db_session):
    user = create_user(db_session)
    create_account(db_session, user.id, "12345678")

    assert_integrity_error(
        db_session,
        lambda: create_account(
            db_session,
            user.id,
            account_number="12345678",
        ),
    )


def test_database_rejects_account_with_missing_user(db_session):
    assert_integrity_error(
        db_session,
        lambda: create_account(
            db_session,
            user_id=999999,
        ),
    )


def test_database_rejects_transfer_with_invalid_amount(db_session):
    user = create_user(db_session)
    source = create_account(db_session, user.id, "12345678")
    destination = create_account(db_session, user.id, "87654321")

    assert_integrity_error(
        db_session,
        lambda: create_transfer(
            db_session,
            source.id,
            destination.id,
            amount=0,
        ),
    )


def test_database_rejects_transfer_between_same_account(db_session):
    user = create_user(db_session)
    account = create_account(db_session, user.id)

    assert_integrity_error(
        db_session,
        lambda: create_transfer(
            db_session,
            account.id,
            account.id,
        ),
    )


def test_database_rejects_transfer_with_invalid_status(db_session):
    user = create_user(db_session)
    source = create_account(db_session, user.id, "12345678")
    destination = create_account(db_session, user.id, "87654321")

    assert_integrity_error(
        db_session,
        lambda: create_transfer(
            db_session,
            source.id,
            destination.id,
            status="Unknown",
        ),
    )


def test_database_rejects_transaction_with_invalid_status(db_session):
    user = create_user(db_session)
    source = create_account(db_session, user.id, "12345678")
    destination = create_account(db_session, user.id, "87654321")

    transfer = create_transfer(
        db_session,
        source.id,
        destination.id,
    )

    transaction = Transaction(
        transaction_id="HIST-TEST-001",
        transfer_id=transfer.id,
        source_account_id=source.id,
        destination_account_id=destination.id,
        amount=100,
        status="Pending",
    )
    db_session.add(transaction)

    assert_integrity_error(
        db_session,
        db_session.flush,
    )
