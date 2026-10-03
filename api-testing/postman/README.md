# BlueBank API Testing

## 1. Purpose

This directory contains the API Testing artifacts for the BlueBank QA Project.

API Testing extends the existing Manual Testing coverage by validating the backend behavior directly, without depending only on the user interface.

The API tests reuse the same:

* Business Rules
* Acceptance Criteria
* Test Scenarios
* Test Data
* Expected business behavior

---

## 2. Scope

The initial API Testing scope covers:

* Authentication
* Account retrieval
* Source account validation
* Destination account validation
* Money Transfer
* Transfer confirmation
* Transfer status
* Transaction History
* Duplicate transfer prevention

---

## 3. Why API Testing Is Added

UI testing verifies the system from the user's perspective.

API testing allows the tester to verify backend behavior directly.

For example:

```text
UI
 ↓
Transfer Form
 ↓
API Request
 ↓
Backend
 ↓
Database
```

A UI test may verify that an invalid transfer is rejected.

An API test can additionally verify:

* HTTP status code
* Response body
* Error message
* Response schema
* Transaction ID
* Balance changes
* Authorization behavior
* Duplicate request handling

---

## 4. Planned API Areas

| Area            | Purpose                           |
| --------------- | --------------------------------- |
| Authentication  | Login and authentication behavior |
| Accounts        | Retrieve and validate accounts    |
| Transfer        | Create money transfers            |
| Transfer Status | Retrieve transfer status          |
| Transactions    | Retrieve transaction history      |

---

## 5. Tools

Primary tool:

**Postman**

Additional tools may be introduced later:

* JavaScript assertions in Postman
* Postman Collection Runner
* Newman
* SQL for database validation

---

## 6. Test Data

API tests reuse the centralized test data located in:

```text
test-data/
```

Important test data includes:

* Valid users
* Invalid credentials
* Active accounts
* Closed accounts
* Blocked accounts
* Valid destinations
* Invalid destinations
* Transfer amounts
* Boundary values
* Request references

---

## 7. API Testing Layers

The API tests will cover several levels of validation.

### HTTP-Level Validation

Examples:

* HTTP method
* Status code
* Headers
* Content type

### Response-Level Validation

Examples:

* Response body
* Required fields
* Data types
* Error messages
* Response structure

### Business-Level Validation

Examples:

* Transfer amount limits
* Account ownership
* Available balance
* Destination eligibility
* Duplicate prevention

### Data-Level Validation

Later, API results will be verified against the database using SQL.

---

## 8. Traceability

API tests will remain traceable to the existing project artifacts.

```text
Business Rule
      ↓
Acceptance Criteria
      ↓
Test Scenario
      ↓
API Test Case
      ↓
API Request
      ↓
Response Validation
      ↓
Database Validation
```

---

## 9. Current Status

The BlueBank API has not yet been implemented or connected to a real environment.

Therefore:

* No real endpoint has been verified.
* No real HTTP response has been recorded.
* No API test has been executed.
* No API defect has been reported.

The endpoint definitions in this directory represent the planned API contract for the portfolio project and must be validated against the actual implementation before execution.
