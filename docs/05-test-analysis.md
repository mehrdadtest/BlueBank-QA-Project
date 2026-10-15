# Test Analysis

## 1. Purpose

This document describes the test analysis for the current BlueBank backend implementation. The analysis is based on the implemented FastAPI endpoints, request validation, service-layer business rules, database operations, and automated tests.

The scope is limited to the existing backend. UI behavior, browser sessions, confirmation dialogs, and other unimplemented frontend functionality are outside the current test scope.

## 2. Test Scope

The current automated test coverage includes:

- Health endpoint availability.
- JWT authentication and authorization.
- Account listing and account ownership.
- Transfer request validation.
- Transfer business rules.
- Balance updates after a successful transfer.
- Transfer and transaction record creation.
- Duplicate request-reference rejection.
- Transaction history visibility for relevant account owners.
- Database rollback and concurrent transfer behavior at the service layer.

## 3. Requirements and Business Rules

| ID | Requirement / Business Rule | Expected Behavior |
|---|---|---|
| BR-01 | Health Check | `GET /health` returns HTTP 200 and `{"status": "healthy"}`. |
| BR-02 | Authentication Required | Protected endpoints reject requests without a valid authentication token. |
| BR-03 | JWT Validation | Invalid, tampered, or expired tokens are rejected. |
| BR-04 | User Validation | A token associated with a nonexistent or inactive user is rejected. |
| BR-05 | Account List Authorization | A user can retrieve only their own accounts. |
| BR-06 | Individual Account Authorization | A user cannot retrieve another user's account; the API returns HTTP 404. |
| BR-07 | Positive Transfer Amount | Transfer requests with zero or negative amounts are rejected during request validation. |
| BR-08 | Transfer Amount Limit | An amount above the implemented maximum of 10,000 is rejected during request validation. |
| BR-09 | Amount Precision | Transfer amounts with more than two decimal places are rejected. |
| BR-10 | Valid Account Number Format | Account numbers that do not satisfy the request schema are rejected. |
| BR-11 | Required Request Reference | An empty `request_reference` is rejected. |
| BR-12 | Different Accounts | Source and destination accounts must be different. |
| BR-13 | Source Account Existence | The source account must exist. |
| BR-14 | Destination Account Existence | The destination account must exist. |
| BR-15 | Source Account Ownership | The authenticated user must own the source account. |
| BR-16 | Active Accounts | Both source and destination accounts must be active. |
| BR-17 | Sufficient Balance | The source account must have sufficient funds for the transfer. |
| BR-18 | Duplicate Request Prevention | A previously used `request_reference` is rejected. |
| BR-19 | Successful Transfer | A valid transfer updates the source and destination balances. |
| BR-20 | Transfer Records | A successful transfer creates a `Transfer` record and a corresponding `Transaction` record. |
| BR-21 | Transaction History Authorization | Transaction history includes transactions relevant to the user's accounts and excludes unrelated transactions. |
| BR-22 | Failure Atomicity | A failed transfer must not leave partial balance changes or incomplete transfer records. |
| BR-23 | Concurrent Balance Protection | Concurrent transfers must not allow the source account to be overdrawn. |

## 4. Test Conditions

### 4.1 Health Check

- Verify the health endpoint returns HTTP 200.
- Verify the response body matches the expected status object.

### 4.2 Authentication and Authorization

- Submit a protected request without a token.
- Submit a request with an invalid token.
- Submit a request with a tampered JWT signature.
- Submit a request with an expired token.
- Submit a request using a token for a nonexistent user.
- Submit a request using a token for an inactive user.

### 4.3 Account Access

- Retrieve the authenticated user's account list.
- Verify that another user's accounts are excluded.
- Retrieve an account owned by the authenticated user.
- Attempt to retrieve an account owned by another user.
- Attempt to list accounts without a token or with an invalid token.

### 4.4 Transfer Request Validation

- Submit zero and negative amounts.
- Submit an amount above the maximum.
- Submit an amount with more than two decimal places.
- Submit an invalid account number.
- Submit an empty request reference.
- Submit the same source and destination account number.

### 4.5 Transfer Business Rules

- Transfer funds from a valid active source account to a valid active destination account.
- Attempt a transfer from another user's source account.
- Attempt a transfer from a nonexistent source account.
- Attempt a transfer to a nonexistent destination account.
- Attempt a transfer from an inactive source account.
- Attempt a transfer to an inactive destination account.
- Attempt a transfer with insufficient funds.
- Submit a duplicate request reference.

### 4.6 Transfer Results and Persistence

- Verify the HTTP response for a successful transfer.
- Verify the source balance decreases by the transfer amount.
- Verify the destination balance increases by the transfer amount.
- Verify the transfer status is `Successful`.
- Verify the corresponding `Transfer` and `Transaction` records exist.
- Verify rejected transfers do not change balances or create records.
- Verify rollback behavior when a transaction-record insertion fails.
- Verify concurrent transfers cannot overdraw the source account.

### 4.7 Transaction History

- Verify the source account owner can see a relevant transaction.
- Verify the destination account owner can see a relevant transaction.
- Verify an unrelated user cannot see that transaction.

## 5. Test Design Techniques

### Equivalence Partitioning (EP)

Input partitions currently supported by the test suite include:

- Valid and invalid transfer amounts.
- Valid and invalid account-number formats.
- Nonempty and empty request references.
- Valid and invalid authentication tokens.
- Existing and nonexistent accounts.
- Active and inactive accounts.
- Authorized and unauthorized source accounts.

### Boundary Value Analysis (BVA)

The existing tests explicitly cover these amount boundaries:

| Input | Expected Result |
|---|---|
| `0` | HTTP 422 |
| Negative amount | HTTP 422 |
| `10000` | The schema's upper boundary; verify using the dedicated validation tests |
| `10001` | HTTP 422 |
| More than two decimal places | HTTP 422 |

The exact minimum positive amount and acceptance of every boundary value must be documented only to the extent confirmed by the request schema and its tests.

### Decision-Based Testing

Transfer acceptance depends on multiple conditions, including source ownership, account existence, account status, available balance, distinct account numbers, and request-reference uniqueness. The automated suite tests these conditions individually and tests a successful transfer.

## 6. Out of Scope

The following items are not included in the current verified automated coverage described by this document:

- UI navigation and confirmation dialogs.
- Cancel, Back, and Change Amount button behavior.
- Browser session expiry.
- Frontend display and formatting.
- Retry behavior after network timeouts.
- Double-click behavior in a user interface.
- Performance, load, accessibility, and security penetration testing.
- Postman execution results, unless a separate executed collection report is available.

## 7. Analysis Summary

The current test analysis focuses on backend API behavior, authorization, transfer business rules, persistence, and transaction history. A requirement is not considered tested merely because it appears in this document; its coverage must be traceable to an automated test or other recorded execution evidence.
