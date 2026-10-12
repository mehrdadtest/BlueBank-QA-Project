from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.account import Account
from app.models.transfer import Transfer
from app.models.transaction import Transaction


def create_transfer(
    db: Session,
    user_id: int,
    source_account_number: str,
    destination_account_number: str,
    amount: Decimal,
    request_reference: str,
):
    try:
        # 1. Validate the transfer amount
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero")

        # 2. Source and destination must be different
        if source_account_number == destination_account_number:
            raise ValueError("Source and destination accounts must be different")

        # 3. Prevent duplicate requests
        existing_transfer = (
            db.query(Transfer)
            .filter(Transfer.request_reference == request_reference)
            .first()
        )

        if existing_transfer:
            raise ValueError("Duplicate request reference")

        # 4. Find the source account
        source_account = (
            db.query(Account)
            .filter(Account.account_number == source_account_number)
            .first()
        )

        if not source_account:
            raise ValueError("Source account not found")

        # 5. Verify source account ownership
        if source_account.user_id != user_id:
            raise ValueError("Source account does not belong to user")

        # 6. Verify source account status
        if source_account.status != "Active":
            raise ValueError("Source account is not active")

        # 7. Verify sufficient balance
        if source_account.balance < amount:
            raise ValueError("Insufficient balance")

        # 8. Find the destination account
        destination_account = (
            db.query(Account)
            .filter(Account.account_number == destination_account_number)
            .first()
        )

        if not destination_account:
            raise ValueError("Destination account not found")

        # 9. Verify destination account status
        if destination_account.status != "Active":
            raise ValueError("Destination account is not active")

        # 10. Create the transfer record
        transaction_id = f"TXN-{request_reference}"

        transfer = Transfer(
            transaction_id=transaction_id,
            source_account_id=source_account.id,
            destination_account_id=destination_account.id,
            amount=amount,
            request_reference=request_reference,
            status="Successful",
        )

        db.add(transfer)

        # Save the transfer inside the current database transaction.
        # This assigns transfer.id without committing the transaction.
        db.flush()

        # 11. Create the transaction history record
        transaction = Transaction(
            transaction_id=transaction_id,
            transfer_id=transfer.id,
            source_account_id=source_account.id,
            destination_account_id=destination_account.id,
            amount=amount,
            status="Successful",
        )

        db.add(transaction)

        # 12. Update both account balances
        source_account.balance -= amount
        destination_account.balance += amount

        # 13. Commit all changes together
        db.commit()

        # 14. Return the saved transfer
        db.refresh(transfer)

        return transfer

    except Exception:
        db.rollback()
        raise
