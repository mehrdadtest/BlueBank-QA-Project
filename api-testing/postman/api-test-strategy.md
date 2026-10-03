# BlueBank API Test Strategy

## 1. Objective

The objective of API Testing is to verify that the BlueBank backend correctly implements the business rules and acceptance criteria independently of the UI.

---

## 2. API Test Categories

### Positive Testing

Valid requests should produce the expected successful response.

Examples:

* Valid login
* Valid source account
* Valid destination account
* Valid transfer amount
* Successful transfer

### Negative Testing

Invalid requests should be rejected correctly.

Examples:

* Invalid credentials
* Unauthorized source account
* Invalid destination
* Same source and destination
* Amount above maximum
* Amount above available balance

### Boundary Testing

Important transfer boundaries will be tested.

Examples:

```text
0
0.01
0.02
9999.99
10000
10000.01
```

### Authorization Testing

Protected endpoints should reject requests when:

* No token is provided.
* Token is invalid.
* Token is expired.
* User attempts to access another user's resource.

### Duplicate Request Testing

The API should prevent duplicate transactions when the same logical transfer request is submitted multiple times.

---

## 3. HTTP Status Code Validation

The exact status codes depend on the API contract.

The test design should verify that the implementation consistently distinguishes successful, validation, authentication, authorization, and server-error conditions.

Examples of categories to validate:

| Category                | Example |
| ----------------------- | ------- |
| Successful request      | 2xx     |
| Client validation error | 4xx     |
| Authentication failure  | 4xx     |
| Authorization failure   | 4xx     |
| Server failure          | 5xx     |

The exact expected status code must be documented after the API contract is available.

---

## 4. Response Validation

API responses should be validated for:

* HTTP status
* Response body
* Required fields
* Data types
* Error structure
* Transaction ID
* Transfer status
* Returned account information

---

## 5. Business Rule Validation

The API layer must enforce the important business rules rather than relying only on frontend validation.

Examples:

### Amount

```text
0.01 ≤ amount ≤ 10000
```

### Balance

```text
amount ≤ available balance
```

### Account Ownership

```text
source account belongs to authenticated user
```

### Destination

```text
destination exists
AND
destination is active
```

### Account Relationship

```text
source account ≠ destination account
```

---

## 6. Database Validation

Database validation will be added in the SQL phase.

For a successful transfer, the expected relationship is:

```text
Source Balance
      ↓
decreases by transfer amount

Destination Balance
      ↓
increases by transfer amount

Transaction History
      ↓
new transaction created
```

The API response alone is not always sufficient to prove that persistent data was updated correctly.

---

## 7. API and UI Relationship

The API tests complement, rather than replace, UI tests.

Example:

```text
UI Test
Login → Transfer Form → Confirm
                    ↓
              API Request
                    ↓
              API Validation
                    ↓
              Database Validation
```

This provides multiple levels of confidence in the same business flow.

---

## 8. Current Status

API Test Strategy:

**Defined**

API Execution:

**Not Started**

Reason:

No executable BlueBank API is currently available.
