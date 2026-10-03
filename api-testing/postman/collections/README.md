# BlueBank Postman Collection

## 1. Purpose

The Postman Collection contains executable API requests for the BlueBank API.

The collection will eventually cover:

* Authentication
* Accounts
* Transfer
* Transfer Status
* Transaction History
* Negative Testing
* Authorization Testing
* Duplicate Transfer Prevention

---

## 2. Planned Collection Structure

```text id="3jzqxm"
BlueBank API
│
├── 01 - Authentication
│   ├── Login - Valid
│   ├── Login - Wrong Password
│   ├── Login - Unregistered Email
│   └── Login - Empty Credentials
│
├── 02 - Accounts
│   ├── Get My Accounts
│   ├── Get Account Details
│   └── Unauthorized Account Access
│
├── 03 - Transfer Validation
│   ├── Valid Destination
│   ├── Invalid Destination
│   ├── Same Account
│   ├── Amount Below Minimum
│   ├── Minimum Amount
│   ├── Maximum Amount
│   ├── Amount Above Maximum
│   ├── Negative Amount
│   ├── Invalid Decimal Precision
│   └── Insufficient Balance
│
├── 04 - Transfer
│   ├── Create Transfer
│   ├── Verify Transaction ID
│   ├── Verify Source Balance
│   └── Verify Destination Balance
│
├── 05 - Transfer Status
│   └── Get Transfer Status
│
├── 06 - Transactions
│   └── Get Transaction History
│
└── 07 - Duplicate Prevention
    ├── Duplicate Request
    ├── Resend Request
    └── Retry After Timeout
```

---

## 3. Request Naming Convention

Requests should use clear names describing the behavior being tested.

Preferred:

```text
Create Transfer - Valid Amount
```

Avoid:

```text
POST Transfer 1
```

The request name should help the tester understand the test purpose without opening the request.

---

## 4. Request Structure

Each request should contain:

* HTTP Method
* URL
* Headers
* Authentication
* Request Body
* Pre-request Script when required
* Test Script
* Related Test Scenario

---

## 5. Assertions

Postman test scripts should validate more than HTTP status.

Depending on the endpoint, assertions may verify:

* Status code
* Response time
* Response schema
* Required fields
* Field values
* Transaction ID
* Transfer status
* Error response
* Business rules

---

## 6. Variable Chaining

Some requests depend on values returned by previous requests.

Example:

```text id="z1f4jj"
Login
  ↓
authToken
  ↓
Create Transfer
  ↓
transactionId
  ↓
Get Transfer Status
  ↓
Transaction History
```

Postman scripts can store these values in environment or collection variables.

---

## 7. Collection Execution

The collection should eventually support:

* Individual request execution
* Folder execution
* Collection Runner
* Data-driven execution
* Newman execution

Automation of the API collection will be considered after the manual API tests are stable.

---

## 8. Current Status

Collection design:

**Defined**

Executable requests:

**Not Started**

Reason:

The BlueBank API implementation is not yet available.
