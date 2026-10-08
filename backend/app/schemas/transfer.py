from decimal import Decimal

from pydantic import BaseModel, Field


class TransferRequest(BaseModel):
    source_account_number: str
    destination_account_number: str

    amount: Decimal = Field(gt=0, le=10000)

    request_reference: str


class TransferResponse(BaseModel):
    transaction_id: str
    source_account_number: str
    destination_account_number: str
    amount: Decimal
    status: str
    request_reference: str
