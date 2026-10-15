# BlueBank QA Project — Business Rules

This document defines the business rules and validation constraints implemented or expected in the BlueBank backend. Numeric validation limits are based on the current transfer request schema.

## 1. Transfer Amount Rules

| ID | Business Rule | Expected Behavior |
|---|---|---|
| BR-01 | The transfer amount must be greater than zero. | Zero and negative amounts are rejected. |
| BR-02 | The transfer amount must not exceed `10,000`. | Amounts greater than `10,000` are rejected. |
| BR-03 | The transfer amount must not exceed the available source-account balance. | Transfers exceeding the available balance are rejected. |
| BR-04 | The transfer amount may equal the available source-account balance. | The transfer is allowed if all other validations pass. |
| BR-05 | The transfer amount must not have more than two decimal places. | Amounts with more than two decimal places are rejected. |
| BR-06 | The transfer amount must be a valid decimal value. | Invalid numeric values are rejected during request validation. |

### Amount Boundary Values

| Input | Expected Result | Reason |
|---|---|---|
| `0` | Invalid | Amount must be greater than zero. |
| `-10` | Invalid | Negative amount. |
| `0.01` | Valid at schema level | Greater than zero and within the maximum. |
| `0.02` | Valid at schema level | Within the permitted range. |
| `100.50` | Valid at schema level | Within the permitted range and precision. |
| `100.555` | Invalid | More than two decimal places. |
| `9999.99` | Valid at schema level | Below the maximum. |
| `10000` | Valid at schema level | Equal to the maximum. |
| `10000.01` | Invalid | Exceeds the maximum. |

**Note:** Schema-level validity does not guarantee a successful transfer. Account ownership, account status, available balance, authentication, and duplicate-reference checks must also pass.

## 2. Account Number Rules

| ID | Business Rule | Expected Behavior |
|---|---|---|
| BR-07 | Source and destination account numbers must contain between 8 and 20 digits. | Values outside this length or format are rejected. |
| BR-08 | The source account must exist. | Transfers from nonexistent source accounts are rejected. |
| BR-09 | The source account must belong to the authenticated user. | Users cannot transfer money from accounts owned by other users. |
| BR-10 | The source account must be active. | Transfers from inactive source accounts are rejected. |
| BR-11 | The destination account must exist. | Transfers to nonexistent destination accounts are rejected. |
| BR-12 | The destination account must be active. | Transfers to inactive destination accounts are rejected. |
| BR-13 | Source and destination accounts must be different. | A transfer between the same account is rejected. |

## 3. Request Reference Rules

| ID | Business Rule | Expected Behavior |
|---|---|---|
| BR-14 | A transfer request must include a valid `request_reference`. | Requests with missing or invalid references are rejected. |
| BR-15 | The request reference must contain between 3 and 100 characters. | Values outside the permitted length are rejected. |
| BR-16 | A duplicate request reference must not create a duplicate successful transfer. | The duplicate request is rejected. |

## 4. Authentication and Authorization Rules

| ID | Business Rule | Expected Behavior |
|---|---|---|
| BR-17 | Transfer functionality requires authentication. | Unauthenticated requests are rejected. |
| BR-18 | Protected account APIs require valid authentication. | Requests without valid credentials or tokens are rejected. |
| BR-19 | Account access must respect ownership rules. | A user cannot retrieve another user's account information without authorization. |
| BR-20 | Transaction-history access must respect authorization rules. | Users cannot retrieve transaction history belonging exclusively to unrelated users. |

## 5. Transfer Processing and Data Consistency

| ID | Business Rule | Expected Behavior |
|---|---|---|
| BR-21 | A successful transfer decreases the source balance by the transfer amount. | The source balance is updated correctly. |
| BR-22 | A successful internal transfer increases the destination balance by the transfer amount. | The destination balance is updated correctly. |
| BR-23 | A successful transfer creates the corresponding transfer and transaction records. | Transfer data is persisted for subsequent retrieval. |
| BR-24 | A failed transfer must not leave partial database changes committed. | Database changes are rolled back when processing fails. |
| BR-25 | Concurrent transfers must not cause the source account to be overdrawn. | Concurrent processing preserves balance constraints. |
| BR-26 | Successful transactions must be retrievable through the transaction-history API. | The transaction appears in the authorized user's history according to the implemented query rules. |

## 6. Login Rules

| ID | Business Rule | Expected Behavior |
|---|---|---|
| BR-27 | Login requires valid credentials. | Invalid credentials are rejected. |
| BR-28 | A nonexistent user cannot authenticate successfully. | Login fails. |
| BR-29 | An inactive user cannot authenticate successfully. | Login fails. |
| BR-30 | Protected API requests require a valid authentication token. | Missing, invalid, tampered, or expired tokens are rejected where applicable. |

## 7. Scope and Traceability Notes

- Amount constraints are based on the transfer request schema: `amount > 0` and `amount <= 10000`.
- Account-number format is 8–20 digits, according to the current request-schema validation.
- Decimal precision is limited to two places.
- `request_reference` length is limited to 3–100 characters.
- Business rules concerning ownership, account status, available balance, duplicate references, transaction history, rollback, and concurrent transfers must be linked to the corresponding automated tests.
- Rules must not be marked as passed solely because the overall test suite reports a successful run. Each rule should be supported by its relevant test evidence.
