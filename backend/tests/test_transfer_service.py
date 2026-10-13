from decimal import Decimal
from uuid import uuid4

import pytest
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.models.account import Account
from app.models.transfer import Transfer
from app.models.transaction import Transaction
from app.services.transfer_service import create_transfer
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
from sqlalchemy.orm import sessionmaker


def unique_account_number():
    # Generate an 8-digit account number for each test.
    return str(10_000_000 + int(uuid4().int % 90_000_000))


def seed_accounts(
    db,
    source_balance=Decimal("100.00"),
    source_status="Active",
    destination_status="Active",
    source_belongs_to_user=True,
):
    user1 = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    user2 = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )

    db.add_all([user1, user2])
    db.flush()

    source_owner_id = user1.id if source_belongs_to_user else user2.id

    source = Account(
        account_number=unique_account_number(),
        user_id=source_owner_id,
        status=source_status,
        balance=source_balance,
    )

    destination = Account(
        account_number=unique_account_number(),
        user_id=user2.id,
        status=destination_status,
        balance=Decimal("50.00"),
    )

    db.add_all([source, destination])
    db.commit()
    db.refresh(source)
    db.refresh(destination)

    return user1, source, destination


def test_transfer_rejects_insufficient_balance(db_session):
    user, source, destination = seed_accounts(
        db_session,
        source_balance=Decimal("20.00"),
    )

    with pytest.raises(ValueError, match="Insufficient balance"):
        create_transfer(
            db_session,
            user.id,
            source.account_number,
            destination.account_number,
            Decimal("30.00"),
            f"REF-{uuid4().hex}",
        )

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == Decimal("20.00")
    assert destination.balance == Decimal("50.00")


def test_transfer_rejects_inactive_source_account(db_session):
    user, source, destination = seed_accounts(
        db_session,
        source_status="Inactive",
    )

    with pytest.raises(ValueError, match="Source account is not active"):
        create_transfer(
            db_session,
            user.id,
            source.account_number,
            destination.account_number,
            Decimal("10.00"),
            f"REF-{uuid4().hex}",
        )


def test_transfer_rejects_inactive_destination_account(db_session):
    user, source, destination = seed_accounts(
        db_session,
        destination_status="Inactive",
    )

    with pytest.raises(
        ValueError,
        match="Destination account is not active",
    ):
        create_transfer(
            db_session,
            user.id,
            source.account_number,
            destination.account_number,
            Decimal("10.00"),
            f"REF-{uuid4().hex}",
        )


def test_transfer_rejects_source_account_owned_by_another_user(db_session):
    user, source, destination = seed_accounts(
        db_session,
        source_belongs_to_user=False,
    )

    with pytest.raises(
        ValueError,
        match="Source account does not belong to user",
    ):
        create_transfer(
            db_session,
            user.id,
            source.account_number,
            destination.account_number,
            Decimal("10.00"),
            f"REF-{uuid4().hex}",
        )


def test_transfer_rejects_missing_source_account(db_session):
    user, source, destination = seed_accounts(db_session)

    with pytest.raises(ValueError, match="Source account not found"):
        create_transfer(
            db_session,
            user.id,
            unique_account_number(),
            destination.account_number,
            Decimal("10.00"),
            f"REF-{uuid4().hex}",
        )


def test_transfer_rejects_missing_destination_account(db_session):
    user, source, destination = seed_accounts(db_session)

    with pytest.raises(
        ValueError,
        match="Destination account not found",
    ):
        create_transfer(
            db_session,
            user.id,
            source.account_number,
            unique_account_number(),
            Decimal("10.00"),
            f"REF-{uuid4().hex}",
        )


def test_transfer_rejects_duplicate_request_reference(db_session):
    user, source, destination = seed_accounts(db_session)
    reference = f"REF-{uuid4().hex}"

    existing_transfer = Transfer(
        transaction_id=f"OLD-{uuid4().hex}",
        source_account_id=source.id,
        destination_account_id=destination.id,
        amount=Decimal("5.00"),
        request_reference=reference,
        status="Successful",
    )
    db_session.add(existing_transfer)
    db_session.commit()

    with pytest.raises(ValueError, match="Duplicate request reference"):
        create_transfer(
            db_session,
            user.id,
            source.account_number,
            destination.account_number,
            Decimal("10.00"),
            reference,
        )


def test_successful_transfer_updates_balances_and_records_history(db_session):
    user, source, destination = seed_accounts(
        db_session,
        source_balance=Decimal("100.00"),
    )
    amount = Decimal("25.00")
    reference = f"REF-{uuid4().hex}"

    transfer = create_transfer(
        db_session,
        user.id,
        source.account_number,
        destination.account_number,
        amount,
        reference,
    )

    db_session.refresh(source)
    db_session.refresh(destination)

    transaction = (
        db_session.query(Transaction)
        .filter(Transaction.transfer_id == transfer.id)
        .one()
    )

    assert transfer.status == "Successful"
    assert transfer.request_reference == reference
    assert transfer.amount == amount

    assert source.balance == Decimal("75.00")
    assert destination.balance == Decimal("75.00")

    assert transaction.transaction_id == transfer.transaction_id
    assert transaction.amount == amount
    assert transaction.status == "Successful"

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == reference)
        .count()
        == 1
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transfer_id == transfer.id)
        .count()
        == 1
    )


def test_transfer_rolls_back_when_transaction_insert_fails(db_session, monkeypatch):
    user, source, destination = seed_accounts(db_session)

    original_source_balance = source.balance
    original_destination_balance = destination.balance
    reference = f"REF-{uuid4().hex}"

    original_add = db_session.add

    def fail_transaction_insert(instance, *args, **kwargs):
        if isinstance(instance, Transaction):
            raise RuntimeError("Simulated transaction insert failure")

        return original_add(instance, *args, **kwargs)

    monkeypatch.setattr(db_session, "add", fail_transaction_insert)

    with pytest.raises(
        RuntimeError,
        match="Simulated transaction insert failure",
    ):
        create_transfer(
            db_session,
            user.id,
            source.account_number,
            destination.account_number,
            Decimal("10.00"),
            reference,
        )

    monkeypatch.setattr(db_session, "add", original_add)

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == original_source_balance
    assert destination.balance == original_destination_balance

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == reference)
        .count()
        == 0
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transaction_id == f"TXN-{reference}")
        .count()
        == 0
    )


def test_concurrent_transfers_do_not_overdraw_account(db_session):
    user, source, destination = seed_accounts(
        db_session,
        source_balance=Decimal("100.00"),
    )

    source_account_number = source.account_number
    destination_account_number = destination.account_number
    user_id = user.id

    amount = Decimal("80.00")
    references = [
        f"REF-{uuid4().hex}",
        f"REF-{uuid4().hex}",
    ]

    session_factory = sessionmaker(
        bind=db_session.get_bind(),
        expire_on_commit=False,
    )

    barrier = Barrier(2)

    def perform_transfer(reference):
        with session_factory() as session:
            barrier.wait()

            try:
                transfer = create_transfer(
                    session,
                    user_id,
                    source_account_number,
                    destination_account_number,
                    amount,
                    reference,
                )
                return ("success", transfer.id)

            except ValueError as exc:
                if str(exc) == "Insufficient balance":
                    return ("rejected", str(exc))
                raise

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [
            executor.submit(perform_transfer, reference) for reference in references
        ]
        results = [future.result() for future in futures]

    statuses = [result[0] for result in results]

    assert statuses.count("success") == 1
    assert statuses.count("rejected") == 1

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == Decimal("20.00")
    assert destination.balance == Decimal("130.00")

    successful_transfer_ids = [
        result[1] for result in results if result[0] == "success"
    ]

    assert (
        db_session.query(Transfer)
        .filter(Transfer.id.in_(successful_transfer_ids))
        .count()
        == 1
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transfer_id.in_(successful_transfer_ids))
        .count()
        == 1
    )
