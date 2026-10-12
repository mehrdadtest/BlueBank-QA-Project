from decimal import Decimal

from pydantic import BaseModel, Field, ConfigDict, field_validator


class TransferRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    source_account_number: str = Field(
        min_length=8,
        max_length=20,
        pattern=r"^[0-9]+$",
    )

    destination_account_number: str = Field(
        min_length=8,
        max_length=20,
        pattern=r"^[0-9]+$",
    )

    amount: Decimal = Field(
        gt=0,
        le=10000,
        max_digits=12,
        decimal_places=2,
    )

    request_reference: str = Field(
        min_length=3,
        max_length=100,
    )

    @field_validator("request_reference")
    @classmethod
    def validate_request_reference(cls, value: str) -> str:
        if not value:
            raise ValueError("Request reference cannot be empty")

        return value


class TransferResponse(BaseModel):
    transaction_id: str
    source_account_number: str
    destination_account_number: str
    amount: Decimal
    status: str
    request_reference: str
