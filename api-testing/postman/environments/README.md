# Postman Environments

## 1. Purpose

Postman Environments store configuration values that change between environments.

The BlueBank API tests should not contain hard-coded environment-specific values such as:

* Base URL
* Authentication token
* User ID
* Account ID
* Transaction ID

Instead, these values should be managed through environment variables.

---

## 2. Planned Environments

| Environment | Purpose                        | Status  |
| ----------- | ------------------------------ | ------- |
| Local       | Local BlueBank API development | Planned |
| QA          | QA test environment            | Planned |

---

## 3. Environment Variables

The initial environment is expected to contain variables such as:

| Variable             | Purpose                      | Example                 |
| -------------------- | ---------------------------- | ----------------------- |
| `baseUrl`            | API base URL                 | `http://localhost:8080` |
| `authToken`          | Current authentication token | Generated at runtime    |
| `userId`             | Current test user            | `USR-001`               |
| `sourceAccount`      | Source account               | `10001234`              |
| `destinationAccount` | Destination account          | `30007890`              |
| `transactionId`      | Current transaction ID       | Generated at runtime    |
| `requestReference`   | Transfer request reference   | `REQ-BB-000001`         |

The actual values should be configured in Postman and should not be committed when they contain secrets or environment-specific credentials.

---

## 4. Variable Scope

Variables should be used according to their purpose.

### Environment Variables

Use for:

* Base URL
* Environment-specific configuration
* Runtime authentication values

### Collection Variables

Use for values shared across the collection when appropriate.

### Local Variables

Use for temporary values needed during a request or script.

---

## 5. Sensitive Data

Real passwords, API keys, tokens, or other secrets must not be committed to GitHub.

The repository should contain only safe example values or placeholders.

For the BlueBank portfolio project, synthetic test credentials are used.

---

## 6. Example Request

Instead of:

```text id="uk4f8p"
http://localhost:8080/api/v1/accounts
```

the collection should use:

```text id="4rfl9s"
{{baseUrl}}/api/v1/accounts
```

This allows the same collection to run against different environments.

---

## 7. Current Status

Environment structure:

**Defined**

Actual environment configuration:

**Not Started**

Reason:

The executable BlueBank API is not yet available.
