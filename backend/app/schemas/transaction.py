from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class TransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    transaction_id: str
    source_account_number: str
    destination_account_number: str
    amount: Decimal
    status: str
    created_at: datetime
