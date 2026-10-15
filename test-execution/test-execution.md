# BlueBank Test Execution

## 1. Purpose

This document records test execution results for the BlueBank QA project.

It distinguishes between:

- Automated backend/API test execution.
- Formal manual test-case execution.
- Retesting of reported defects.
- Regression testing after code changes.

Every execution result must be supported by actual evidence. Test results must not be inferred from requirements, expected results, or the existence of test code alone.

## 2. Execution Status Definitions

| Status | Description |
|---|---|
| Not Executed | The test has not been executed in the relevant execution cycle. |
| Pass | The observed behavior matches the expected result. |
| Fail | The observed behavior differs from the expected result. |
| Blocked | Execution cannot proceed because of an unresolved environment, dependency, or prerequisite issue. |
| Not Applicable | The test does not apply to the agreed execution scope, with a documented reason. |

A failed test is not automatically a confirmed product defect. Investigate the failure to determine whether it is caused by the application, test code, test data, configuration, or environment.

## 3. Current Execution Overview

### 3.1 Automated Backend/API Tests

The latest reported pytest execution completed with **56 passed**.

| Metric | Latest Reported Result |
|---|---:|
| Passed pytest test items | 56 |
| Failed pytest test items | 0 |
| Execution status | Passed |
| Test framework | pytest |
| Execution command | `python -m pytest .\tests -v` |

Run the command from the `backend` directory.

The result above is based on the latest reported execution. The execution date, commit, environment, and complete test output must be recorded to establish a reproducible execution record.

The 56 passing test items are not equivalent to 56 unique business scenarios or 56 formal manual test cases.

### 3.2 Manual Test Cases

The project contains historical documentation describing 61 test scenarios and 61 test cases. These records originated from an earlier, UI-oriented test-design scope.

They must be reviewed and reconciled with the current backend implementation before being treated as the current manual execution baseline.

| Metric | Status |
|---|---|
| Current approved manual test-case baseline | Requires reconciliation |
| Manually executed cases | Not established |
| Manual pass/fail counts | Not established |
| Manual blocked cases | Not established |
| Manual execution evidence | Not established in this summary |

Do not use the automated test result to populate the manual execution counts.

## 4. Execution Record Information

Each execution cycle should have its own record.

| Field | Value |
|---|---|
| Project | BlueBank QA Project |
| Execution Cycle ID | TBD |
| Test Type | Automated Backend/API |
| Test Framework | pytest |
| Application Commit | TBD |
| Environment | TBD |
| Test Database | Dedicated test database |
| Execution Command | `python -m pytest .\tests -v` |
| Execution Date and Time | TBD |
| Tester or Executor | TBD |
| Evidence Location | TBD |

Fill in the fields from the actual execution environment. Do not invent a build version, commit hash, execution timestamp, or environment identifier.

## 5. Automated Test Execution Records

For automated tests, preserve the actual test output and use the test function names from the current test suite.

Example record format:

| Test Function / Item | Test Area | Result | Evidence | Defect ID | Notes |
|---|---|---|---|---|---|
| `test_transfer_rejects_insufficient_balance` | Transfer validation | Record from actual run | TBD | TBD | Verify against execution output |
| `test_transfer_rejects_inactive_source_account` | Source account validation | Record from actual run | TBD | TBD | Verify against execution output |
| `test_transfer_rejects_inactive_destination_account` | Destination validation | Record from actual run | TBD | TBD | Verify against execution output |
| `test_transfer_rejects_source_account_owned_by_another_user` | Authorization | Record from actual run | TBD | TBD | Verify against execution output |
| `test_transfer_rejects_duplicate_request_reference` | Duplicate request handling | Record from actual run | TBD | TBD | Verify against execution output |
| `test_successful_transfer_updates_balances_and_records_history` | Transfer processing | Record from actual run | TBD | TBD | Verify against execution output |
| `test_transfer_rolls_back_when_transaction_insert_fails` | Rollback | Record from actual run | TBD | TBD | Verify against execution output |
| `test_concurrent_transfers_do_not_overdraw_account` | Concurrency | Record from actual run | TBD | TBD | Verify against execution output |

These are examples of known test functions, not a complete list of all tests. Populate results from the actual pytest output. Do not mark individual functions as passed merely because the overall suite previously reported 56 passed.

For a detailed record, retain the test function, run identifier, outcome, failure output where applicable, and link to the corresponding requirement or test case.

## 6. Manual Test Execution Records

Use the following format for approved manual test cases:

| Field | Description |
|---|---|
| Test Case ID | Stable identifier for the formal test case |
| Requirement / AC ID | Related requirement or acceptance criterion |
| Test Scenario ID | Related scenario |
| Test Type | Manual API, database verification, or another applicable type |
| Priority | Agreed test priority |
| Environment | Environment used for execution |
| Preconditions | Conditions established before the test |
| Test Data | Data used during execution |
| Actual Result | Observed system behavior |
| Status | Pass, Fail, Blocked, or Not Applicable |
| Defect ID | Related defect, if one is confirmed |
| Evidence | Request/response, query output, logs, or other relevant evidence |
| Execution Date | Date and time of execution |
| Tester | Person who executed the test |

Manual execution should begin only after the test case has been reviewed and the required environment and test data are available.

UI-specific cases such as clicking a confirmation button, navigating backward in a transfer form, or verifying a confirmation screen must not be executed against the backend-only implementation as if those UI components existed.

Where the intended behavior can be tested at the API level, create or revise an API-level test case with an appropriate request and expected response.

## 7. Execution Rules

### 7.1 Pass

Mark a test as Pass when the actual result satisfies the expected result and the required evidence has been recorded.

### 7.2 Fail

Mark a test as Fail when the actual result does not satisfy the expected result.

Record the observed behavior, relevant request and response or logs, and the steps needed to reproduce the issue.

Create a defect report when investigation confirms a product defect.

### 7.3 Blocked

Mark a test as Blocked when a prerequisite prevents execution.

Examples include:

- The application or required API is unavailable.
- The required test database cannot be accessed.
- Required test data cannot be prepared.
- A required dependency is unavailable.
- An unresolved environment issue prevents a valid result.

Record the blocking reason and the action required to unblock the test.

### 7.4 Not Executed

Keep a test as Not Executed when no execution has taken place in the current cycle.

### 7.5 Not Applicable

Use Not Applicable only when the test is outside the agreed execution scope. Record the reason and obtain the appropriate review or approval.

## 8. Actual Results and Evidence

The Actual Result field must describe the observed behavior, not repeat the Expected Result.

For example:

**Expected Result:** The API rejects a transfer request with an invalid amount.

**Actual Result:** The API returned HTTP 422 and a validation response for the submitted request.

**Status:** Pass, provided that this response matches the approved expected result.

Useful evidence may include:

- pytest output and failure tracebacks.
- API requests and responses.
- Database query results.
- Application logs.
- Transfer or transaction identifiers.
- Relevant timestamps.
- Screenshots or recordings when a UI exists and they are relevant.

Do not include passwords, access tokens, database credentials, or other secrets in evidence committed to the repository.

## 9. Environment and Reproducibility

Record the following for each meaningful execution cycle:

| Field | Value |
|---|---|
| Operating System | TBD |
| Python Version | TBD |
| Application Commit | TBD |
| Dependency Versions | `backend/requirements.txt` or captured environment |
| Database Engine and Version | TBD |
| Test Database | Dedicated test database |
| Test Command | `python -m pytest .\tests -v` |
| Execution Date and Time | TBD |
| Execution Output | TBD |

Before running the test suite, verify that the configured database is the dedicated test database and that the project's database safety checks are active.

## 10. Defect Linkage, Retest, and Regression

The defect workflow is:

```text
Test Execution
      ↓
Fail
      ↓
Failure Investigation
      ↓
Confirmed Defect (if applicable)
      ↓
Fix
      ↓
Retest
      ↓
Regression Testing
      ↓
Recorded Final Result
```

A defect should reference the test case and execution that exposed it. Retesting should verify the specific fix, while regression testing should check related behavior that may have been affected by the change.

Do not create fictional defect records solely to populate the portfolio. If no defect has been confirmed, state that no confirmed defects have been recorded for the relevant cycle.

## 11. Execution Metrics

Calculate metrics separately for each execution cycle and test type.

**Execution Progress**

`Executed Cases / Total Planned Cases × 100`

**Pass Rate**

`Passed Cases / Executed Cases × 100`

**Fail Rate**

`Failed Cases / Executed Cases × 100`

**Blocked Rate**

`Blocked Cases / Executed Cases × 100`

For these metrics, define the denominator consistently and count each planned test case once per cycle. Do not mix automated pytest items with formal manual test cases.

If no cases have been executed, pass, fail, and blocked rates should be reported as not applicable rather than as 0%.

## 12. Exit Criteria

An execution cycle can be closed when its agreed exit criteria have been met, including:

- All planned cases have a recorded outcome or an approved exclusion.
- Required critical tests have been executed.
- Failed tests have been investigated.
- Confirmed defects have been documented.
- Required retesting and regression testing have been completed.
- Unresolved issues and risks have been recorded.
- Execution evidence and the final summary have been reviewed.

Passing all executed tests does not by itself prove complete requirements coverage or production readiness.

## 13. Current Conclusion

The latest reported automated backend/API test run completed with **56 passed pytest test items**.

The historical set of 61 UI-oriented test scenarios and test cases has not yet been reconciled with the current backend scope. Therefore, it must not be used as the denominator for current manual execution metrics.

The next steps are to:

1. Reconcile the historical test cases with the implemented API behavior.
2. Confirm the current formal manual test-case baseline.
3. Record the commit, execution date, environment, and full pytest output for subsequent runs.
4. Map automated test functions to the relevant requirements and test cases.
5. Execute suitable manual API and database checks where they add value.
6. Record confirmed defects, retests, and regression results when applicable.
