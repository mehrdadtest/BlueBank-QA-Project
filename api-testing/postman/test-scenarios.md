# BlueBank API Test Scenarios

## Authentication

| ID         | Scenario                      | Expected Outcome        |
| ---------- | ----------------------------- | ----------------------- |
| API-TS-001 | Login with valid credentials  | Authentication succeeds |
| API-TS-002 | Login with wrong password     | Authentication rejected |
| API-TS-003 | Login with unregistered email | Authentication rejected |
| API-TS-004 | Login with empty email        | Request rejected        |
| API-TS-005 | Login with empty password     | Request rejected        |

## Authorization

| ID         | Scenario                                     | Expected Outcome |
| ---------- | -------------------------------------------- | ---------------- |
| API-TS-006 | Access protected endpoint without token      | Request rejected |
| API-TS-007 | Access protected endpoint with invalid token | Request rejected |
| API-TS-008 | Access protected endpoint with expired token | Request rejected |
| API-TS-009 | Access another user's account                | Request rejected |

## Accounts

| ID         | Scenario                               | Expected Outcome               |
| ---------- | -------------------------------------- | ------------------------------ |
| API-TS-010 | Retrieve authenticated user's accounts | Own eligible accounts returned |
| API-TS-011 | Attempt to use closed source account   | Request rejected               |
| API-TS-012 | Attempt to use blocked source account  | Request rejected               |
| API-TS-013 | Attempt unauthorized source account    | Request rejected               |

## Destination Validation

| ID         | Scenario                    | Expected Outcome |
| ---------- | --------------------------- | ---------------- |
| API-TS-014 | Valid destination           | Accepted         |
| API-TS-015 | Nonexistent destination     | Rejected         |
| API-TS-016 | Closed destination          | Rejected         |
| API-TS-017 | Blocked destination         | Rejected         |
| API-TS-018 | Same source and destination | Rejected         |
| API-TS-019 | Invalid destination format  | Rejected         |

## Amount Validation

| ID         | Scenario               | Expected Outcome |
| ---------- | ---------------------- | ---------------- |
| API-TS-020 | Amount = 0             | Rejected         |
| API-TS-021 | Amount = 0.01          | Accepted         |
| API-TS-022 | Amount = 0.02          | Accepted         |
| API-TS-023 | Normal amount = 500    | Accepted         |
| API-TS-024 | Amount = 9999.99       | Accepted         |
| API-TS-025 | Amount = 10000         | Accepted         |
| API-TS-026 | Amount = 10000.01      | Rejected         |
| API-TS-027 | Negative amount        | Rejected         |
| API-TS-028 | Non-numeric amount     | Rejected         |
| API-TS-029 | More than two decimals | Rejected         |

## Balance Validation

| ID         | Scenario                | Expected Outcome  |
| ---------- | ----------------------- | ----------------- |
| API-TS-030 | Amount below balance    | Accepted          |
| API-TS-031 | Amount equal to balance | Accepted          |
| API-TS-032 | Amount above balance    | Rejected          |
| API-TS-033 | Zero balance            | Transfer rejected |

## Transfer

| ID         | Scenario                          | Expected Outcome            |
| ---------- | --------------------------------- | --------------------------- |
| API-TS-034 | Create valid transfer             | Transfer created            |
| API-TS-035 | Verify unique Transaction ID      | Unique ID returned          |
| API-TS-036 | Verify source balance update      | Balance decreases correctly |
| API-TS-037 | Verify destination balance update | Balance increases correctly |
| API-TS-038 | Verify transaction history        | Transaction recorded        |
| API-TS-039 | Retrieve transfer status          | Correct status returned     |

## Duplicate Prevention

| ID         | Scenario                      | Expected Outcome                           |
| ---------- | ----------------------------- | ------------------------------------------ |
| API-TS-040 | Submit same request twice     | No duplicate transaction                   |
| API-TS-041 | Resend same request reference | No duplicate transaction                   |
| API-TS-042 | Retry after timeout           | No duplicate if original request succeeded |

## End-to-End API Flow

| ID         | Scenario                                        | Expected Outcome                          |
| ---------- | ----------------------------------------------- | ----------------------------------------- |
| API-TS-043 | Login → Get Accounts → Transfer → Verify Status | Complete flow succeeds                    |
| API-TS-044 | Login → Transfer with insufficient balance      | Transfer rejected                         |
| API-TS-045 | Login → Transfer to invalid destination         | Transfer rejected                         |
| API-TS-046 | Login → Full balance transfer                   | Transfer succeeds and source reaches zero |
| API-TS-047 | Login → Duplicate transfer attempt              | Only one transaction created              |

---

## Scenario Count

Current API Test Design contains:

**47 API Test Scenarios**

These scenarios will later be converted into executable Postman requests and assertions.

---

## Current Status

* API Scenarios: Defined
* Postman Collection: Planned
* API Execution: Not Started
* API Defects: 0
