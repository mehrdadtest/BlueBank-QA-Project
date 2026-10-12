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
    try:
        # 1. مبلغ انتقال باید مثبت باشد
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero")

        # 2. حساب مبدأ و مقصد نباید یکسان باشند
        if source_account_number == destination_account_number:
            raise ValueError("Source and destination accounts must be different")

        # 3. جلوگیری از درخواست تکراری
        existing_transfer = (
            db.query(Transfer)
            .filter(Transfer.request_reference == request_reference)
            .first()
        )

        if existing_transfer:
            raise ValueError("Duplicate request reference")

        # 4. پیدا کردن حساب مبدأ
        source_account = (
            db.query(Account)
            .filter(Account.account_number == source_account_number)
            .first()
        )

        if not source_account:
            raise ValueError("Source account not found")

        # 5. بررسی مالکیت حساب مبدأ
        if source_account.user_id != user_id:
            raise ValueError("Source account does not belong to user")

        # 6. حساب مبدأ باید فعال باشد
        if source_account.status != "Active":
            raise ValueError("Source account is not active")

        # 7. موجودی حساب مبدأ باید کافی باشد
        if source_account.balance < amount:
            raise ValueError("Insufficient balance")

        # 8. پیدا کردن حساب مقصد
        destination_account = (
            db.query(Account)
            .filter(Account.account_number == destination_account_number)
            .first()
        )

        if not destination_account:
            raise ValueError("Destination account not found")

        # 9. حساب مقصد باید فعال باشد
        if destination_account.status != "Active":
            raise ValueError("Destination account is not active")

        # 10. ساخت شناسه انتقال
        transaction_id = f"TXN-{request_reference}"

        # 11. ایجاد رکورد انتقال
        transfer = Transfer(
            transaction_id=transaction_id,
            source_account_id=source_account.id,
            destination_account_id=destination_account.id,
            amount=amount,
            request_reference=request_reference,
            status="Successful",
        )

        # 12. به‌روزرسانی موجودی دو حساب
        source_account.balance -= amount
        destination_account.balance += amount

        # 13. ذخیره انتقال و موجودی‌های جدید
        db.add(transfer)
        db.commit()

        # 14. دریافت اطلاعات ذخیره‌شده
        db.refresh(transfer)

        return transfer

    except Exception:
        db.rollback()
        raise
