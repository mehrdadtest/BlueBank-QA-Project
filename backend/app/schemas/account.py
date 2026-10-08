from decimal import Decimal

from pydantic import BaseModel


class AccountResponse(BaseModel):
    account_number: str
    status: str
    balance: Decimal

    class Config:
        from_attributes = True
