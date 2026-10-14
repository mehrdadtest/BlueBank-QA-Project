from fastapi.testclient import TestClient
from types import SimpleNamespace
from app.api.dependencies import get_current_user
from app.main import app

from uuid import uuid4

from app.models.user import User
from app.models.account import Account
from decimal import Decimal
from app.models.transfer import Transfer
from app.models.transaction import Transaction
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import settings
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import settings

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_transfer_rejects_zero_amount():
    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=1)

    try:
        response = client.post(
            "/api/v1/transfers",
            json={
                "source_account_number": "12345678",
                "destination_account_number": "87654321",
                "amount": "0",
                "request_reference": "TEST-ZERO-AMOUNT",
            },
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 422


def test_transfer_rejects_negative_amount():
    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=1)

    try:
        payload = {
            "source_account_number": "10001234",
            "destination_account_number": "20004567",
            "amount": -10,
            "request_reference": "PYTEST-NEGATIVE-001",
        }

        response = client.post(
            "/api/v1/transfers",
            json=payload,
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 422


def test_transfer_rejects_amount_above_limit():
    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=1)

    try:
        payload = {
            "source_account_number": "10001234",
            "destination_account_number": "20004567",
            "amount": 10001,
            "request_reference": "PYTEST-ABOVE-LIMIT-001",
        }

        response = client.post(
            "/api/v1/transfers",
            json=payload,
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 422


def test_transfer_rejects_same_source_and_destination():
    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=1)

    try:
        payload = {
            "source_account_number": "10001234",
            "destination_account_number": "10001234",
            "amount": 10,
            "request_reference": "PYTEST-SAME-ACCOUNT-001",
        }

        response = client.post(
            "/api/v1/transfers",
            json=payload,
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Source and destination accounts must be different"
    )


def test_transfer_rejects_invalid_account_number():
    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=1)

    try:
        payload = {
            "source_account_number": "ABC12345",
            "destination_account_number": "20004567",
            "amount": 10,
            "request_reference": "PYTEST-INVALID-ACCOUNT-001",
        }

        response = client.post(
            "/api/v1/transfers",
            json=payload,
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 422


def test_transfer_rejects_empty_request_reference():
    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=1)

    try:
        payload = {
            "source_account_number": "10001234",
            "destination_account_number": "20004567",
            "amount": 10,
            "request_reference": "",
        }

        response = client.post(
            "/api/v1/transfers",
            json=payload,
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 422


def test_transfer_rejects_amount_with_too_many_decimals():
    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=1)

    try:
        payload = {
            "source_account_number": "10001234",
            "destination_account_number": "20004567",
            "amount": "10.123",
            "request_reference": "PYTEST-DECIMALS-001",
        }

        response = client.post(
            "/api/v1/transfers",
            json=payload,
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 422


def test_transfer_rejects_request_without_token():
    payload = {
        "source_account_number": "10001234",
        "destination_account_number": "20004567",
        "amount": 10,
        "request_reference": "AUTH-NO-TOKEN-001",
    }

    response = client.post("/api/v1/transfers", json=payload)

    assert response.status_code in (401, 403)


def test_transfer_rejects_invalid_token():
    payload = {
        "source_account_number": "10001234",
        "destination_account_number": "20004567",
        "amount": 10,
        "request_reference": "AUTH-BAD-TOKEN-001",
    }

    response = client.post(
        "/api/v1/transfers",
        json=payload,
        headers={"Authorization": "Bearer invalid-token"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid authentication token"


def test_accounts_list_returns_only_current_users_accounts(db_session):
    user1 = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    user2 = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )

    db_session.add_all([user1, user2])
    db_session.flush()

    account1 = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user1.id,
        status="Active",
        balance=100,
    )
    account2 = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user2.id,
        status="Active",
        balance=200,
    )

    db_session.add_all([account1, account2])
    db_session.commit()

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=user1.id)

    try:
        response = client.get("/api/v1/accounts")
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 200

    returned_account_numbers = {item["account_number"] for item in response.json()}

    assert account1.account_number in returned_account_numbers
    assert account2.account_number not in returned_account_numbers


def test_user_can_access_own_account(db_session):
    user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add(user)
    db_session.flush()

    account = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=100,
    )
    db_session.add(account)
    db_session.commit()

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=user.id)

    try:
        response = client.get(f"/api/v1/accounts/{account.account_number}")
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 200
    assert response.json()["account_number"] == account.account_number


def test_user_cannot_access_another_users_account(db_session):
    owner = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    another_user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )

    db_session.add_all([owner, another_user])
    db_session.flush()

    account = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=owner.id,
        status="Active",
        balance=500,
    )
    db_session.add(account)
    db_session.commit()

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(
        id=another_user.id
    )

    try:
        response = client.get(f"/api/v1/accounts/{account.account_number}")
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 404
    assert response.json()["detail"] == "Account not found"


def test_transfer_api_successfully_transfers_money(db_session):
    user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add(user)
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("100.00"),
    )
    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("50.00"),
    )
    db_session.add_all([source, destination])
    db_session.commit()

    source_number = source.account_number
    destination_number = destination.account_number
    request_reference = f"API-TRANSFER-{uuid4().hex}"

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=user.id)

    try:
        response = client.post(
            "/api/v1/transfers",
            json={
                "source_account_number": source_number,
                "destination_account_number": destination_number,
                "amount": "10.00",
                "request_reference": request_reference,
            },
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 200

    result = response.json()
    assert result["source_account_number"] == source_number
    assert result["destination_account_number"] == destination_number
    assert Decimal(str(result["amount"])) == Decimal("10.00")
    assert result["status"] == "Successful"
    assert result["request_reference"] == request_reference

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == Decimal("90.00")
    assert destination.balance == Decimal("60.00")

    transfer = (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .first()
    )
    assert transfer is not None
    assert transfer.status == "Successful"
    assert transfer.amount == Decimal("10.00")

    transaction = (
        db_session.query(Transaction)
        .filter(Transaction.transaction_id == f"TXN-{request_reference}")
        .first()
    )
    assert transaction is not None
    assert transaction.status == "Successful"
    assert transaction.amount == Decimal("10.00")


def test_transfer_api_rejects_another_users_source_account(db_session):
    owner = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    another_user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add_all([owner, another_user])
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=owner.id,
        status="Active",
        balance=Decimal("100.00"),
    )
    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=another_user.id,
        status="Active",
        balance=Decimal("50.00"),
    )
    db_session.add_all([source, destination])
    db_session.commit()

    source_number = source.account_number
    destination_number = destination.account_number
    request_reference = f"API-UNAUTHORIZED-{uuid4().hex}"

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(
        id=another_user.id
    )

    try:
        response = client.post(
            "/api/v1/transfers",
            json={
                "source_account_number": source_number,
                "destination_account_number": destination_number,
                "amount": "10.00",
                "request_reference": request_reference,
            },
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 400
    assert response.json()["detail"] == ("Source account does not belong to user")

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == Decimal("100.00")
    assert destination.balance == Decimal("50.00")

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .first()
        is None
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transaction_id == f"TXN-{request_reference}")
        .first()
        is None
    )


def test_transfer_api_rejects_duplicate_request_reference(db_session):
    user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add(user)
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("100.00"),
    )
    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("50.00"),
    )
    db_session.add_all([source, destination])
    db_session.commit()

    source_number = source.account_number
    destination_number = destination.account_number
    request_reference = f"API-DUPLICATE-{uuid4().hex}"

    payload = {
        "source_account_number": source_number,
        "destination_account_number": destination_number,
        "amount": "10.00",
        "request_reference": request_reference,
    }

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=user.id)

    try:
        first_response = client.post(
            "/api/v1/transfers",
            json=payload,
        )
        second_response = client.post(
            "/api/v1/transfers",
            json=payload,
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert first_response.status_code == 200

    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Duplicate request reference"

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == Decimal("90.00")
    assert destination.balance == Decimal("60.00")

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .count()
        == 1
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transaction_id == f"TXN-{request_reference}")
        .count()
        == 1
    )


def test_transfer_api_rejects_insufficient_balance(db_session):
    user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add(user)
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("5.00"),
    )
    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("50.00"),
    )
    db_session.add_all([source, destination])
    db_session.commit()

    source_number = source.account_number
    destination_number = destination.account_number
    request_reference = f"API-INSUFFICIENT-{uuid4().hex}"

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=user.id)

    try:
        response = client.post(
            "/api/v1/transfers",
            json={
                "source_account_number": source_number,
                "destination_account_number": destination_number,
                "amount": "10.00",
                "request_reference": request_reference,
            },
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient balance"

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == Decimal("5.00")
    assert destination.balance == Decimal("50.00")

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .count()
        == 0
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transaction_id == f"TXN-{request_reference}")
        .count()
        == 0
    )


def test_transfer_api_rejects_inactive_source_account(db_session):
    user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add(user)
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Closed",
        balance=Decimal("100.00"),
    )
    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("50.00"),
    )
    db_session.add_all([source, destination])
    db_session.commit()

    source_number = source.account_number
    destination_number = destination.account_number
    request_reference = f"API-INACTIVE-SOURCE-{uuid4().hex}"

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=user.id)

    try:
        response = client.post(
            "/api/v1/transfers",
            json={
                "source_account_number": source_number,
                "destination_account_number": destination_number,
                "amount": "10.00",
                "request_reference": request_reference,
            },
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 400
    assert response.json()["detail"] == "Source account is not active"

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == Decimal("100.00")
    assert destination.balance == Decimal("50.00")

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .count()
        == 0
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transaction_id == f"TXN-{request_reference}")
        .count()
        == 0
    )


def test_transfer_api_rejects_inactive_destination_account(db_session):
    user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add(user)
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("100.00"),
    )
    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Closed",
        balance=Decimal("50.00"),
    )
    db_session.add_all([source, destination])
    db_session.commit()

    source_number = source.account_number
    destination_number = destination.account_number
    request_reference = f"API-INACTIVE-DEST-{uuid4().hex}"

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=user.id)

    try:
        response = client.post(
            "/api/v1/transfers",
            json={
                "source_account_number": source_number,
                "destination_account_number": destination_number,
                "amount": "10.00",
                "request_reference": request_reference,
            },
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 400
    assert response.json()["detail"] == "Destination account is not active"

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == Decimal("100.00")
    assert destination.balance == Decimal("50.00")

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .count()
        == 0
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transaction_id == f"TXN-{request_reference}")
        .count()
        == 0
    )


def test_transfer_api_rejects_nonexistent_destination_account(db_session):
    user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add(user)
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("100.00"),
    )
    db_session.add(source)
    db_session.commit()

    source_number = source.account_number
    destination_number = "99999999"
    request_reference = f"API-DEST-NOT-FOUND-{uuid4().hex}"

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=user.id)

    try:
        response = client.post(
            "/api/v1/transfers",
            json={
                "source_account_number": source_number,
                "destination_account_number": destination_number,
                "amount": "10.00",
                "request_reference": request_reference,
            },
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 400
    assert response.json()["detail"] == "Destination account not found"

    db_session.refresh(source)
    assert source.balance == Decimal("100.00")

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .count()
        == 0
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transaction_id == f"TXN-{request_reference}")
        .count()
        == 0
    )


def test_transfer_api_rejects_nonexistent_source_account(db_session):
    user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add(user)
    db_session.flush()

    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("50.00"),
    )
    db_session.add(destination)
    db_session.commit()

    source_number = "99999998"
    destination_number = destination.account_number
    request_reference = f"API-SOURCE-NOT-FOUND-{uuid4().hex}"

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(id=user.id)

    try:
        response = client.post(
            "/api/v1/transfers",
            json={
                "source_account_number": source_number,
                "destination_account_number": destination_number,
                "amount": "10.00",
                "request_reference": request_reference,
            },
        )
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 400
    assert response.json()["detail"] == "Source account not found"

    db_session.refresh(destination)
    assert destination.balance == Decimal("50.00")

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .count()
        == 0
    )

    assert (
        db_session.query(Transaction)
        .filter(Transaction.transaction_id == f"TXN-{request_reference}")
        .count()
        == 0
    )


def test_transfer_api_rejects_inactive_user(db_session):
    user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Closed",
    )
    db_session.add(user)
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("100.00"),
    )

    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=user.id,
        status="Active",
        balance=Decimal("50.00"),
    )

    db_session.add_all([source, destination])
    db_session.commit()

    source_number = source.account_number
    destination_number = destination.account_number
    user_id = user.id
    request_reference = f"INACTIVE-{uuid4().hex[:12]}"

    token = jwt.encode(
        {
            "sub": str(user_id),
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
        },
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )

    response = client.post(
        "/api/v1/transfers",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "source_account_number": source_number,
            "destination_account_number": destination_number,
            "amount": "10.00",
            "request_reference": request_reference,
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "User account is inactive"

    db_session.refresh(source)
    db_session.refresh(destination)

    assert source.balance == Decimal("100.00")
    assert destination.balance == Decimal("50.00")

    assert (
        db_session.query(Transfer)
        .filter(Transfer.request_reference == request_reference)
        .count()
        == 0
    )


def test_transfer_api_rejects_tampered_token():
    token = jwt.encode(
        {
            "sub": "1",
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
        },
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )

    token_parts = token.split(".")
    signature = token_parts[2]

    token_parts[2] = ("B" if signature[0] == "A" else "A") + signature[1:]

    tampered_token = ".".join(token_parts)

    response = client.post(
        "/api/v1/transfers",
        headers={"Authorization": f"Bearer {tampered_token}"},
        json={
            "source_account_number": "12345678",
            "destination_account_number": "87654321",
            "amount": "10.00",
            "request_reference": "TAMPERED-TOKEN-001",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid authentication token"


def test_transfer_api_rejects_expired_token():
    token = jwt.encode(
        {
            "sub": "1",
            "exp": datetime.now(timezone.utc) - timedelta(minutes=5),
        },
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )

    response = client.post(
        "/api/v1/transfers",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "source_account_number": "12345678",
            "destination_account_number": "87654321",
            "amount": "10.00",
            "request_reference": "EXPIRED-TOKEN-001",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid authentication token"


def test_transfer_api_rejects_token_for_nonexistent_user(db_session):
    nonexistent_user_id = 999999999

    token = jwt.encode(
        {
            "sub": str(nonexistent_user_id),
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
        },
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )

    response = client.post(
        "/api/v1/transfers",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "source_account_number": "12345678",
            "destination_account_number": "87654321",
            "amount": "10.00",
            "request_reference": f"NOUSER-{uuid4().hex[:12]}",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "User not found"


def test_accounts_list_rejects_request_without_token():
    response = client.get("/api/v1/accounts")

    assert response.status_code in (401, 403)


def test_accounts_list_rejects_invalid_token():
    response = client.get(
        "/api/v1/accounts",
        headers={"Authorization": "Bearer invalid-token"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid authentication token"


def test_transactions_list_includes_transaction_for_source_owner(db_session):
    source_owner = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    destination_owner = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add_all([source_owner, destination_owner])
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=source_owner.id,
        status="Active",
        balance=Decimal("100.00"),
    )
    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=destination_owner.id,
        status="Active",
        balance=Decimal("50.00"),
    )
    db_session.add_all([source, destination])
    db_session.flush()

    transaction_id = f"TXN-{uuid4().hex}"

    transfer = Transfer(
        transaction_id=transaction_id,
        source_account_id=source.id,
        destination_account_id=destination.id,
        amount=Decimal("10.00"),
        request_reference=f"REF-{uuid4().hex}",
        status="Successful",
    )
    db_session.add(transfer)
    db_session.flush()

    transaction = Transaction(
        transaction_id=transaction_id,
        transfer_id=transfer.id,
        source_account_id=source.id,
        destination_account_id=destination.id,
        amount=Decimal("10.00"),
        status="Successful",
    )
    db_session.add(transaction)
    db_session.commit()

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(
        id=source_owner.id
    )
    try:
        response = client.get("/api/v1/transactions")
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 200
    assert transaction_id in [item["transaction_id"] for item in response.json()]


def test_transactions_list_includes_transaction_for_destination_owner(db_session):
    source_owner = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    destination_owner = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add_all([source_owner, destination_owner])
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=source_owner.id,
        status="Active",
        balance=Decimal("100.00"),
    )
    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=destination_owner.id,
        status="Active",
        balance=Decimal("50.00"),
    )
    db_session.add_all([source, destination])
    db_session.flush()

    transaction_id = f"TXN-{uuid4().hex}"

    transfer = Transfer(
        transaction_id=transaction_id,
        source_account_id=source.id,
        destination_account_id=destination.id,
        amount=Decimal("10.00"),
        request_reference=f"REF-{uuid4().hex}",
        status="Successful",
    )
    db_session.add(transfer)
    db_session.flush()

    transaction = Transaction(
        transaction_id=transaction_id,
        transfer_id=transfer.id,
        source_account_id=source.id,
        destination_account_id=destination.id,
        amount=Decimal("10.00"),
        status="Successful",
    )
    db_session.add(transaction)
    db_session.commit()

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(
        id=destination_owner.id
    )
    try:
        response = client.get("/api/v1/transactions")
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 200
    assert transaction_id in [item["transaction_id"] for item in response.json()]


def test_transactions_list_excludes_transaction_for_unrelated_user(db_session):
    source_owner = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    destination_owner = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    unrelated_user = User(
        email=f"{uuid4().hex}@test.local",
        password="test-password",
        status="Active",
    )
    db_session.add_all([source_owner, destination_owner, unrelated_user])
    db_session.flush()

    source = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=source_owner.id,
        status="Active",
        balance=Decimal("100.00"),
    )
    destination = Account(
        account_number=str(10_000_000 + uuid4().int % 90_000_000),
        user_id=destination_owner.id,
        status="Active",
        balance=Decimal("50.00"),
    )
    db_session.add_all([source, destination])
    db_session.flush()

    transaction_id = f"TXN-{uuid4().hex}"

    transfer = Transfer(
        transaction_id=transaction_id,
        source_account_id=source.id,
        destination_account_id=destination.id,
        amount=Decimal("10.00"),
        request_reference=f"REF-{uuid4().hex}",
        status="Successful",
    )
    db_session.add(transfer)
    db_session.flush()

    transaction = Transaction(
        transaction_id=transaction_id,
        transfer_id=transfer.id,
        source_account_id=source.id,
        destination_account_id=destination.id,
        amount=Decimal("10.00"),
        status="Successful",
    )
    db_session.add(transaction)
    db_session.commit()

    app.dependency_overrides[get_current_user] = lambda: SimpleNamespace(
        id=unrelated_user.id
    )
    try:
        response = client.get("/api/v1/transactions")
    finally:
        app.dependency_overrides.pop(get_current_user, None)

    assert response.status_code == 200
    assert transaction_id not in [item["transaction_id"] for item in response.json()]
