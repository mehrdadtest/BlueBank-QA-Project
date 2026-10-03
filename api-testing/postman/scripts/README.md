# Postman Scripts

## 1. Purpose

Postman scripts are used to prepare requests and validate responses automatically.

BlueBank will use two main types of scripts:

* Pre-request Scripts
* Test Scripts

---

## 2. Pre-request Scripts

Pre-request scripts run before the request is sent.

Potential uses include:

* Generate dynamic request references
* Prepare test data
* Set timestamps
* Generate temporary values
* Prepare authentication-related variables

Example concept:

```text id="m8t9qk"
requestReference = REQ-BB-<unique-value>
```

---

## 3. Test Scripts

Test Scripts run after the API response is received.

They can validate:

* HTTP status
* Response body
* Required fields
* Business rules
* Response data
* Transaction ID
* Transfer status

---

## 4. Authentication Token Chaining

After a successful login, the authentication token can be stored for later requests.

Conceptual flow:

```text id="zjjj0x"
Login
  ↓
Extract token
  ↓
Store authToken
  ↓
Use {{authToken}}
  ↓
Protected API requests
```

The exact implementation depends on the authentication mechanism used by the BlueBank API.

---

## 5. Transaction ID Chaining

After creating a successful transfer:

```text id="6l7c5b"
Create Transfer
       ↓
Extract transactionId
       ↓
Store {{transactionId}}
       ↓
Get Transfer Status
```

This allows subsequent requests to operate on the transaction created by the previous request.

---

## 6. Business Assertions

API tests should validate business behavior rather than checking only the HTTP status.

For example, a successful transfer test should eventually verify:

```text id="9t7g1r"
HTTP response successful
        AND
Transaction ID exists
        AND
Transfer status is correct
        AND
Source balance changed correctly
        AND
Destination balance changed correctly
```

---

## 7. Error Assertions

Negative tests should verify that invalid requests are rejected correctly.

Example:

```text id="zkgm2s"
Amount = 10000.01
        ↓
Request rejected
        ↓
Expected validation error
```

The exact HTTP status and error schema must be based on the actual API contract.

---

## 8. Current Status

Script design:

**Defined**

Executable scripts:

**Not Started**

Reason:

The executable BlueBank API is not yet available.
