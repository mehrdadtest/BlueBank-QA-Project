# BlueBank — Test Scenarios

## 1. Document Information

| Field | Description |
|---|---|
| Project | BlueBank QA Project |
| Document | Test Scenarios |
| Scope | Automated backend testing |
| API Framework | FastAPI |
| Test Framework | pytest |
| Reported Execution Result | 56 passed |
| Scenario Status | To be mapped to the corresponding automated tests |

## 2. Authentication and Authorization

| Scenario ID | Scenario | Expected Result | Test Layer |
|---|---|---|---|
| TS-001 | Login with valid credentials | Authentication succeeds and an access token is returned. | API |
| TS-002 | Login with an incorrect password | Authentication is rejected. | API |
| TS-003 | Login with an unregistered email | Authentication is rejected. | API |
| TS-004 | Login with an inactive user account | Authentication is denied. | API |
| TS-005 | Access a protected endpoint without a token | The request is rejected as unauthorized. | API |
| TS-006 | Access a protected endpoint using an invalid token | The request is rejected. | API |
| TS-007 | Access a protected endpoint using a tampered token | The request is rejected. | API |
| TS-008 | Access a protected endpoint using an expired token | The request is rejected. | API |
| TS-009 | Access a protected endpoint using a token associated with a nonexistent user | The request is rejected. | API |

## 3. Accounts API and Ownership

| Scenario ID | Scenario | Expected Result | Test Layer |
|---|---|---|---|
| TS-010 | Retrieve accounts while authenticated | Only accounts belonging to the authenticated user are returned. | API |
| TS-011 | Retrieve accounts without authentication | Access is denied. | API |
| TS-012 | Retrieve an account by its account number | The requested account is returned when access is authorized. | API |
| TS-013 | Retrieve an account belonging to another user | Unauthorized account access is prevented. | API |
| TS-014 | Retrieve an account that does not exist | The API returns the appropriate error response. | API |

## 4. Transfer Request Validation

| Scenario ID | Scenario | Expected Result | Test Layer |
|---|---|---|---|
| TS-015 | Submit a valid transfer request | The request passes schema validation. | Schema |
| TS-016 | Submit a transfer amount of zero | The request fails validation. | Schema |
| TS-017 | Submit a negative transfer amount | The request fails validation. | Schema |
| TS-018 | Submit a transfer amount above the permitted maximum | The request fails validation. | Schema |
| TS-019 | Submit an invalid account number | The request fails validation. | Schema |
| TS-020 | Submit an empty request reference | The request fails validation. | Schema |
| TS-021 | Submit an amount with more than two decimal places | The request fails validation. | Schema |
| TS-022 | Submit a transfer request without authentication | The API rejects the request. | API |
| TS-023 | Submit a transfer from an account to the same account | The transfer is rejected. | Service/API |

## 5. Transfer Business Rules

| Scenario ID | Scenario | Expected Result | Test Layer |
|---|---|---|---|
| TS-024 | Transfer from a nonexistent source account | The transfer is rejected without committing changes. | Service |
| TS-025 | Transfer to a nonexistent destination account | The transfer is rejected without committing changes. | Service |
| TS-026 | Transfer from an account owned by another user | The transfer is rejected. | Service/API |
| TS-027 | Transfer from an inactive source account | The transfer is rejected. | Service |
| TS-028 | Transfer to an inactive destination account | The transfer is rejected. | Service |
| TS-029 | Transfer an amount greater than the available source balance | The transfer is rejected because of insufficient funds. | Service |
| TS-030 | Submit a request reference that has already been used | The duplicate request is rejected. | Service |
| TS-031 | Complete a valid transfer | The transfer succeeds and the corresponding records are created. | Service/API |
| TS-032 | Verify the source account balance after a successful transfer | The source balance decreases by the transfer amount. | Service |
| TS-033 | Verify the destination account balance after a successful transfer | The destination balance increases by the transfer amount. | Service |
| TS-034 | Verify transfer record creation | A transfer record is persisted for the successful operation. | Service |
| TS-035 | Verify transaction record creation | A corresponding transaction record is persisted. | Service |
| TS-036 | Simulate a failure while inserting the transaction record | The operation rolls back instead of leaving partially committed changes. | Service |
| TS-037 | Execute concurrent transfers against the same source account | Concurrent processing does not allow the account to be overdrawn. | Service |

## 6. Transaction History and Access Control

| Scenario ID | Scenario | Expected Result | Test Layer |
|---|---|---|---|
| TS-038 | Retrieve transaction history while authenticated | The request succeeds and returns the transactions visible to the user. | API |
| TS-039 | Retrieve transaction history without authentication | Access is denied. | API |
| TS-040 | Retrieve history for a user who owns the source account | The relevant transaction is included in the user's history. | API |
| TS-041 | Retrieve history for a user who owns the destination account | The relevant transaction is included in the user's history. | API |
| TS-042 | Retrieve history as an unrelated user | Transactions unrelated to the authenticated user are excluded. | API |
| TS-043 | Verify that a successful transfer appears in transaction history | The corresponding transaction is present. | API/Service |

## 7. Additional Automated Test Coverage

The following areas should be mapped to the exact test functions and parameterized test items in the repository before this document is considered final.

| Coverage ID | Area | Verification Objective |
|---|---|---|
| TS-044 | Authentication input validation | Invalid login input is rejected according to the implemented schema. |
| TS-045 | Transfer amount boundary validation | Boundary values are accepted or rejected according to the actual schema constraints. |
| TS-046 | Account-number validation | Invalid account-number values are rejected. |
| TS-047 | Request-reference validation | Missing or empty request references are rejected. |
| TS-048 | Decimal precision validation | Amounts with unsupported precision are rejected. |
| TS-049 | Source-account ownership | A user cannot transfer money from another user's account. |
| TS-050 | Source-account status | An inactive source account cannot be used for a transfer. |
| TS-051 | Destination-account status | An inactive destination account cannot receive a transfer. |
| TS-052 | Insufficient balance | A transfer cannot complete when the source account lacks sufficient funds. |
| TS-053 | Duplicate request reference | Reusing a request reference does not create another successful transfer. |
| TS-054 | Transaction insertion failure | A transaction persistence failure triggers rollback. |
| TS-055 | Successful transfer consistency | Account balances and transfer-related records remain consistent after success. |
| TS-056 | Concurrent transfer safety | Concurrent transfers preserve the source account's balance constraint. |

## 8. Execution and Traceability

The latest reported automated test execution completed with **56 passed**.

The execution report should record the exact command, execution date, environment, and pytest output when those details are available.

For each scenario, maintain the following traceability information:

- **Scenario ID:** TS-001 through TS-056
- **Automated Test:** Exact pytest test function
- **Parameterized Input:** The specific parameter value, where applicable
- **Test Layer:** API, service, or schema
- **Execution Status:** Passed, Failed, or Not Run
- **Evidence:** Pytest output or report reference

### Important Notes

1. The number of pytest test items is not necessarily equal to the number of unique business scenarios. Parameterized tests can produce multiple test items from a single test function.
2. A scenario may be covered by multiple automated tests, and a single test function may cover more than one assertion.
3. Scenario coverage and execution status must be confirmed against the current source files in `backend/tests`.
4. Do not describe UI interactions, browser navigation, confirmation screens, or browser-timeout retries as executed tests unless separate UI automation exists.
5. Only mark a scenario as **Passed** when its corresponding automated test result supports that status.
