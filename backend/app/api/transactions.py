from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.database.connection import get_db
from app.models.user import User
from app.schemas.transaction import TransactionResponse
from app.services.transaction_service import get_user_transactions

router = APIRouter(
    prefix="/api/v1/transactions",
    tags=["Transactions"],
)


@router.get("", response_model=list[TransactionResponse])
def get_transactions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_user_transactions(
        db=db,
        user_id=current_user.id,
    )
