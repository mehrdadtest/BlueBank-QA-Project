from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.account import AccountResponse
from app.services.account_service import get_user_accounts, get_account_by_number

router = APIRouter(prefix="/api/v1/accounts", tags=["Accounts"])


@router.get("/user/{user_id}", response_model=list[AccountResponse])
def get_accounts(user_id: int, db: Session = Depends(get_db)):
    return get_user_accounts(db, user_id)


@router.get("/{account_number}", response_model=AccountResponse)
def get_account(account_number: str, db: Session = Depends(get_db)):
    account = get_account_by_number(db, account_number)

    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    return account
