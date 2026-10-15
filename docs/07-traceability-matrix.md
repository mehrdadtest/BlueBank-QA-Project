# Traceability Matrix

## 1. Purpose

This document maps the current BlueBank backend requirements to automated test scenarios and their corresponding test functions.

The matrix is based on the implemented code and test files. It does not treat a planned scenario as implemented or executed without supporting evidence.

## 2. Traceability Structure

The traceability chain used in this project is:

**Business Rule → Test Scenario → Automated Test Function → Execution Result**

A requirement may be covered by more than one test. Likewise, a single test may provide evidence for multiple related requirements.

## 3. Requirement-to-Test Traceability

| Requirement ID | Requirement | Scenario IDs | Automated Test Evidence |
|---|---|---|---|
| BR-01 | Health endpoint responds correctly | TS-001 | `test_health_check` |
| BR-02 | Protected endpoints require authentication | TS-009, TS-015 | `test_transfer_rejects_request_without_token`, `test_accounts_list_rejects_request_without_token` |
| BR-03 | Invalid JWTs are rejected | TS-010–TS-012, TS-016 | `test_transfer_rejects_invalid_token`, `test_transfer_api_rejects_tampered_token`, `test_transfer_api_rejects_expired_token`, `test_accounts_list_rejects_invalid_token` |
| BR-04 | Nonexistent or inactive users are rejected | TS-013–TS-014 | `test_transfer_api_rejects_token_for_nonexistent_user`, `test_transfer_api_rejects_inactive_user` |
| BR-05 | Account lists are restricted to the current user | TS-017 | `test_accounts_list_returns_only_current_users_accounts` |
| BR-06 | Users cannot access another user's account | TS-018–TS-019 | `test_user_can_access_own_account`, `test_user_cannot_access_another_users_account` |
| BR-07 | Zero and negative amounts are rejected | TS-002–TS-003, TS-046–TS-047 | `test_transfer_rejects_zero_amount`, `test_transfer_rejects_negative_amount`, `test_invalid_transfer_amount` |
| BR-08 | Amounts above the maximum are rejected | TS-004, TS-048 | `test_transfer_rejects_amount_above_limit`, `test_invalid_transfer_amount` |
| BR-09 | Excessive decimal precision is rejected | TS-008, TS-051 | `test_transfer_rejects_amount_with_too_many_decimals`, `test_amount_with_too_many_decimal_places` |
| BR-10 | Invalid account-number formats are rejected | TS-006, TS-049 | `test_transfer_rejects_invalid_account_number`, `test_invalid_account_number` |
| BR-11 | An empty request reference is rejected | TS-007, TS-050 | `test_transfer_rejects_empty_request_reference`, `test_empty_request_reference` |
| BR-12 | Source and destination accounts must differ | TS-005 | `test_transfer_rejects_same_source_and_destination` |
| BR-13 | The source account must exist | TS-031, TS-039 | `test_transfer_api_rejects_nonexistent_source_account`, `test_transfer_rejects_missing_source_account` |
| BR-14 | The destination account must exist | TS-030, TS-040 | `test_transfer_api_rejects_nonexistent_destination_account`, `test_transfer_rejects_missing_destination_account` |
| BR-15 | The authenticated user must own the source account | TS-025, TS-038 | `test_transfer_api_rejects_another_users_source_account`, `test_transfer_rejects_source_account_owned_by_another_user` |
| BR-16 | Source and destination accounts must be active | TS-028–TS-029, TS-036–TS-037 | `test_transfer_api_rejects_inactive_source_account`, `test_transfer_api_rejects_inactive_destination_account`, corresponding service-layer tests |
| BR-17 | Insufficient funds prevent a transfer | TS-027, TS-035 | `test_transfer_api_rejects_insufficient_balance`, `test_transfer_rejects_insufficient_balance` |
| BR-18 | Duplicate request references are rejected | TS-026, TS-041 | `test_transfer_api_rejects_duplicate_request_reference`, `test_transfer_rejects_duplicate_request_reference` |
| BR-19 | Successful transfers update both balances | TS-020–TS-022, TS-042 | `test_transfer_api_successfully_transfers_money`, `test_successful_transfer_updates_balances_and_records_history` |
| BR-20 | Successful transfers create transfer and transaction records | TS-023–TS-024, TS-042 | `test_transfer_api_successfully_transfers_money`, `test_successful_transfer_updates_balances_and_records_history` |
| BR-21 | Transaction history respects account ownership | TS-032–TS-034 | `test_transactions_list_includes_transaction_for_source_owner`, `test_transactions_list_includes_transaction_for_destination_owner`, `test_transactions_list_excludes_transaction_for_unrelated_user` |
| BR-22 | Failed transfers do not leave partial changes | TS-025–TS-031, TS-043 | Rejected-transfer API tests and `test_transfer_rolls_back_when_transaction_insert_fails` |
| BR-23 | Concurrent transfers cannot overdraw the source account | TS-044 | `test_concurrent_transfers_do_not_overdraw_account` |

## 4. Coverage Notes

- The matrix identifies test functions that provide evidence for each requirement.
- A function with parameterized inputs may represent multiple pytest test cases.
- API tests and service-layer tests are listed separately where their test boundaries differ.
- Request-schema tests verify input validation; they do not by themselves establish that the complete transfer workflow behaves correctly.
- A test's presence in the code does not establish that its latest execution passed. Execution status must be confirmed from pytest output.
- UI behavior, performance testing, and other unimplemented areas are not included as verified coverage.

## 5. Execution Evidence

The latest execution result reported for the project was **56 passed**. The exact per-test results should be taken from the corresponding pytest report.

The reported total is a test execution count, not a count of business rules, scenarios, or Postman requests.

## 6. Maintenance

When implementation or test coverage changes:

1. Update the relevant business rule.
2. Add, modify, or remove the corresponding test scenario.
3. Update the mapping to the actual test function.
4. Record the new execution result.
5. Remove any mapping that no longer has implementation or test evidence.
