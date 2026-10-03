# BlueBank API Endpoints

## 1. Purpose

This document defines the planned API endpoints for the BlueBank QA Project.

These endpoints represent the API contract required to support the current project scope.

They are placeholders until an executable BlueBank API is available.

---

## 2. Authentication

### Login

```text
POST /api/v1/auth/login
```

Purpose:

Authenticate a BlueBank customer and establish an authenticated session or token.

Expected request concept:

```json
{
  "email": "john.doe@bluebank.test",
  "password": "BlueBank@123"
}
```

Expected successful response concept:

```json
{
  "token": "TBD",
  "userId": "USR-001"
}
```

The exact response structure must be confirmed against the implementation.

---

## 3. Accounts

### Get Customer Accounts

```text
GET /api/v1/accounts
```

Purpose:

Retrieve accounts belonging to the authenticated customer.

Relevant requirements:

* AC-01
* AC-02
* BR-05

---

## 4. Account Details

### Get Account Details

```text
GET /api/v1/accounts/{accountNumber}
```

Purpose:

Retrieve account information and balance.

Example:

```text
GET /api/v1/accounts/10001234
```

Relevant requirements include:

* Account ownership
* Account status
* Available balance

---

## 5. Money Transfer

### Create Transfer

```text
POST /api/v1/transfers
```

Purpose:

Create a money transfer between eligible accounts.

Expected request concept:

```json
{
  "sourceAccount": "10001234",
  "destinationAccount": "30007890",
  "amount": 500.00
}
```

Potential request reference:

```text
REQ-BB-000001
```

The exact mechanism for duplicate prevention must be confirmed when the API implementation is available.

---

## 6. Transfer Status

### Get Transfer Status

```text
GET /api/v1/transfers/{transactionId}
```

Purpose:

Retrieve the current status and details of a transfer.

Relevant requirement:

* AC-12

---

## 7. Transaction History

### Get Transaction History

```text
GET /api/v1/transactions
```

Purpose:

Retrieve the authenticated customer's transaction history.

Relevant requirements:

* AC-12
* BR-14

---

## 8. Authentication Model

The planned API requires authentication for protected endpoints.

Example:

```text
Authorization: Bearer <token>
```

The exact authentication mechanism must be verified against the actual implementation.

---

## 9. HTTP Methods

| Method    | Planned Usage                              |
| --------- | ------------------------------------------ |
| GET       | Retrieve resources                         |
| POST      | Create authentication or transfer requests |
| PUT/PATCH | Not currently required                     |
| DELETE    | Not currently required                     |

---

## 10. Important Note

The endpoints above are part of the portfolio project's planned API contract.

They should not be treated as verified production endpoints.

Once the BlueBank API implementation exists, the following must be confirmed:

* Base URL
* Endpoint paths
* HTTP methods
* Authentication mechanism
* Request schema
* Response schema
* Status codes
* Error format
* Idempotency mechanism
