from decimal import Decimal
from pydantic import BaseModel, ConfigDict

from pydantic import BaseModel


class AccountResponse(BaseModel):
    account_number: str
    status: str
    balance: Decimal

    model_config = ConfigDict(from_attributes=True)
