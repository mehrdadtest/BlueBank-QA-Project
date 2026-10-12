from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user import User
from app.schemas.account import AccountResponse
from app.services.account_service import (
    get_user_accounts,
    get_account_by_number,
)
from app.api.dependencies import get_current_user

router = APIRouter(prefix="/api/v1/accounts", tags=["Accounts"])


@router.get("", response_model=list[AccountResponse])
def get_accounts(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return get_user_accounts(db, current_user.id)


@router.get("/{account_number}", response_model=AccountResponse)
def get_account(
    account_number: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    account = get_account_by_number(db, account_number)

    if not account or account.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Account not found")

    return account
