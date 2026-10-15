# BlueBank QA Project — Acceptance Criteria

## 1. Purpose

This document defines the acceptance criteria for the BlueBank backend capabilities in Phase 1.

The criteria describe observable API behavior and business outcomes. They are intended to support test analysis, test design, automated testing, and requirements traceability.

The current scope includes authentication, bank account inquiry, money transfer, and transaction history. Graphical user-interface behavior is excluded unless implemented separately.

## 2. US-01 — Money Transfer

**API:** `POST /api/v1/transfers`

| ID | Acceptance Criterion |
|---|---|
| AC-TRANSFER-01 | A transfer request that fails request-schema validation is rejected, and the transfer is not processed. |
| AC-TRANSFER-02 | An unauthenticated request to the protected transfer endpoint is rejected. |
| AC-TRANSFER-03 | A transfer from a nonexistent source account is rejected. |
| AC-TRANSFER-04 | A transfer from an inactive source account is rejected. |
| AC-TRANSFER-05 | A user cannot transfer money from a source account owned by another user. |
| AC-TRANSFER-06 | A transfer to a nonexistent destination account is rejected. |
| AC-TRANSFER-07 | A transfer to an inactive destination account is rejected. |
| AC-TRANSFER-08 | A transfer between the same source and destination account is rejected. |
| AC-TRANSFER-09 | The transfer amount must be greater than zero and must not exceed `10,000`. |
| AC-TRANSFER-10 | The transfer amount must contain no more than two decimal places. |
| AC-TRANSFER-11 | A transfer that exceeds the available source-account balance is rejected. |
| AC-TRANSFER-12 | A transfer request must contain a valid `request_reference` within the permitted schema length of 3–100 characters. |
| AC-TRANSFER-13 | A duplicate request reference is rejected without creating a duplicate successful transfer. |
| AC-TRANSFER-14 | A successful transfer decreases the source-account balance by the transfer amount. |
| AC-TRANSFER-15 | A successful internal transfer increases the destination-account balance by the transfer amount. |
| AC-TRANSFER-16 | A successful transfer creates the corresponding transfer and transaction records. |
| AC-TRANSFER-17 | If an exception occurs during transfer processing, partial database changes are rolled back. |
| AC-TRANSFER-18 | Concurrent transfer processing must not allow the source account to be overdrawn. |

### Transfer Amount Examples

These examples describe the intended amount-validation behavior. Other transfer rules, including authentication, account status, ownership, and available balance, must also be satisfied.

| Input | Expected Result |
|---|---|
| `0` | Rejected |
| `-10` | Rejected |
| `0.01` | Accepted by amount validation |
| `0.02` | Accepted by amount validation |
| `100.50` | Accepted by amount validation |
| `100.555` | Rejected |
| `9999.99` | Accepted by amount validation |
| `10000` | Accepted by amount validation |
| `10000.01` | Rejected |

**Note:** The lower-bound rule is defined as an amount greater than zero. The schema does not need a separate minimum value of `0.01` when the amount is restricted to two decimal places. The exact-boundary behavior should still be verified by the relevant tests.

### Transfer Outcome and Data Integrity

A successful transfer must preserve the following invariants:

- The source balance decreases by the transfer amount.
- The destination balance increases by the same amount.
- The corresponding transfer and transaction records are created.
- A failed operation does not leave partially committed database changes.
- Concurrent processing does not cause the source account to be overdrawn.

A graphical confirmation screen, a customer-facing cancel button, and UI-based confirmation are not acceptance criteria for the current backend-only scope.

## 3. US-02 — Login

**API:** `POST /api/v1/auth/login`

| ID | Acceptance Criterion |
|---|---|
| AC-LOGIN-01 | Valid credentials for an eligible registered user result in successful authentication. |
| AC-LOGIN-02 | Incorrect credentials are rejected. |
| AC-LOGIN-03 | Credentials for a nonexistent user are rejected. |
| AC-LOGIN-04 | An inactive user cannot authenticate successfully. |
| AC-LOGIN-05 | The authentication response provides the information required by the implemented authentication flow. |
| AC-LOGIN-06 | Protected API requests with missing or invalid authentication are rejected. |
| AC-LOGIN-07 | Tampered or expired authentication tokens are rejected where applicable to protected endpoints. |

Empty-field validation should be tested according to the actual login request schema and API response. A graphical form preventing submission of empty fields is outside the current backend scope.

## 4. US-03 — Transaction History

**API:** `GET /api/v1/transactions`

| ID | Acceptance Criterion |
|---|---|
| AC-HISTORY-01 | An authenticated user can retrieve transaction history they are authorized to access. |
| AC-HISTORY-02 | Transactions associated with the user's source or destination accounts are returned according to the implemented query rules. |
| AC-HISTORY-03 | A user cannot retrieve transaction history belonging exclusively to unrelated users. |
| AC-HISTORY-04 | Requests without valid authentication are rejected. |
| AC-HISTORY-05 | A successfully completed transfer creates a transaction record retrievable through the transaction-history API. |
| AC-HISTORY-06 | Transaction records returned by the API correspond to the persisted transaction data. |

The exact response fields, sorting order, pagination behavior, and displayed transaction status must be documented only when supported by the current API implementation.

## 5. US-04 — Bank Account Inquiry

**APIs:**

- `GET /api/v1/accounts`
- `GET /api/v1/accounts/{account_number}`

| ID | Acceptance Criterion |
|---|---|
| AC-ACCOUNT-01 | An authenticated user can retrieve their accessible bank accounts. |
| AC-ACCOUNT-02 | A user can retrieve the details of an account they are authorized to access. |
| AC-ACCOUNT-03 | A user cannot retrieve another user's account details without authorization. |
| AC-ACCOUNT-04 | Requests without valid authentication are rejected where authentication is required. |
| AC-ACCOUNT-05 | A request for a nonexistent or inaccessible account is handled according to the implemented API behavior. |

The account-list response and account-detail response must be validated against the actual API schemas and authorization rules.

## 6. Traceability

Acceptance criteria must be traceable to the relevant business rules, test conditions, scenarios, and test cases.

The project uses the following traceability chain:

**User Story → Business Rule → Acceptance Criterion → Test Condition → Test Scenario → Test Case → Test Execution → Defect (if identified) → Retest → Regression**

Not every test execution results in a defect. Defect, retest, and regression records are created when applicable.

## 7. Acceptance Criteria Verification Status

Acceptance criteria describe required behavior; they are not proof that the behavior has passed testing.

Each criterion should be linked to relevant automated or manual test evidence and assigned an appropriate verification status, such as:

- **Verified:** Relevant evidence confirms the criterion.
- **Failed:** Test evidence demonstrates that the criterion is not satisfied.
- **Not Verified:** The criterion has not yet been sufficiently tested.
- **Not Applicable:** The criterion does not apply to the implemented scope, with justification.

A test-suite result such as `56 passed` confirms that the executed pytest test items passed in that run. It does not automatically establish that every acceptance criterion in this document has been verified.

## 8. Scope Notes

- The criteria describe backend API behavior, not an unimplemented graphical interface.
- The amount limit of `10,000`, positive-amount constraint, and two-decimal precision are based on the transfer request schema described for the current project.
- The account-number schema permits 8–20 digits; an eight-digit-only restriction must not be assumed.
- The request-reference schema permits 3–100 characters.
- The exact behavior of boundary cases should be supported by relevant tests before being marked verified.
- All acceptance criteria must remain aligned with the current code, test suite, and traceability matrix.
