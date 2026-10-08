from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.transfer import TransferRequest, TransferResponse
from app.services.transfer_service import create_transfer

router = APIRouter(prefix="/api/v1/transfers", tags=["Transfers"])


@router.post("", response_model=TransferResponse)
def transfer_money(
    request: TransferRequest, user_id: int, db: Session = Depends(get_db)
):
    try:
        transfer = create_transfer(
            db=db,
            user_id=user_id,
            source_account_number=request.source_account_number,
            destination_account_number=request.destination_account_number,
            amount=request.amount,
            request_reference=request.request_reference,
        )

        return TransferResponse(
            transaction_id=transfer.transaction_id,
            source_account_number=request.source_account_number,
            destination_account_number=request.destination_account_number,
            amount=transfer.amount,
            status=transfer.status,
            request_reference=transfer.request_reference,
        )

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
