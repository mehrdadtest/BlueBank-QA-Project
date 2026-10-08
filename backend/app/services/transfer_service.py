from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.account import Account
from app.models.transfer import Transfer


def create_transfer(
    db: Session,
    user_id: int,
    source_account_number: str,
    destination_account_number: str,
    amount: Decimal,
    request_reference: str,
):
    # 1. Source و Destination نباید یکسان باشند
    if source_account_number == destination_account_number:
        raise ValueError("Source and destination accounts must be different")

    # 2. پیدا کردن حساب مبدأ
    source_account = (
        db.query(Account)
        .filter(Account.account_number == source_account_number)
        .first()
    )

    if not source_account:
        raise ValueError("Source account not found")

    # 3. حساب مبدأ باید متعلق به کاربر باشد
    if source_account.user_id != user_id:
        raise ValueError("Source account does not belong to user")

    # 4. حساب مبدأ باید Active باشد
    if source_account.status != "Active":
        raise ValueError("Source account is not active")

    # 5. موجودی باید کافی باشد
    if source_account.balance < amount:
        raise ValueError("Insufficient balance")

    # 6. پیدا کردن حساب مقصد
    destination_account = (
        db.query(Account)
        .filter(Account.account_number == destination_account_number)
        .first()
    )

    if not destination_account:
        raise ValueError("Destination account not found")

    # 7. حساب مقصد باید Active باشد
    if destination_account.status != "Active":
        raise ValueError("Destination account is not active")

    # 8. جلوگیری از Request تکراری
    existing_transfer = (
        db.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .first()
    )

    if existing_transfer:
        raise ValueError("Duplicate request reference")

    # 9. ایجاد Transaction ID
    transaction_id = f"TXN-{request_reference}"

    # 10. ایجاد Transfer
    transfer = Transfer(
        transaction_id=transaction_id,
        source_account_id=source_account.id,
        destination_account_id=destination_account.id,
        amount=amount,
        request_reference=request_reference,
        status="Successful",
    )

    # 11. کم کردن موجودی مبدأ
    source_account.balance -= amount

    # 12. اضافه کردن مبلغ به مقصد
    destination_account.balance += amount

    # 13. ذخیره Transfer
    db.add(transfer)

    # 14. ثبت تغییرات در Database
    db.commit()

    # 15. دریافت اطلاعات نهایی
    db.refresh(transfer)

    return transfer
