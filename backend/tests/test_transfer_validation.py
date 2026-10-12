import pytest
from pydantic import ValidationError

from app.schemas.transfer import TransferRequest

BASE_DATA = {
    "source_account_number": "10001234",
    "destination_account_number": "20004567",
    "amount": 10,
    "request_reference": "VALID-001",
}


def test_valid_transfer_request():
    request = TransferRequest(**BASE_DATA)

    assert request.amount == 10
    assert request.source_account_number == "10001234"


@pytest.mark.parametrize(
    "amount",
    [0, -1, 10001],
    ids=["zero", "negative", "above_limit"],
)
def test_invalid_amount(amount):
    data = {**BASE_DATA, "amount": amount}

    with pytest.raises(ValidationError):
        TransferRequest(**data)


def test_account_number_with_letters_is_rejected():
    data = {
        **BASE_DATA,
        "source_account_number": "ABC12345",
    }

    with pytest.raises(ValidationError):
        TransferRequest(**data)


def test_empty_request_reference_is_rejected():
    data = {**BASE_DATA, "request_reference": ""}

    with pytest.raises(ValidationError):
        TransferRequest(**data)


def test_amount_with_more_than_two_decimal_places_is_rejected():
    data = {
        **BASE_DATA,
        "amount": "10.123",
    }

    with pytest.raises(ValidationError):
        TransferRequest(**data)
