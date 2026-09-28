# BlueBank Test Data

This directory contains centralized and reusable test data for the BlueBank QA project.

The purpose of this directory is to maintain test data in one place so that the same data can be reused consistently across different testing activities, including:

- Manual UI Testing
- API Testing with Postman
- Database / SQL Testing
- Playwright Automation
- Regression Testing

## Test Data Files

| File | Purpose |
|---|---|
| `users.md` | Test users and their basic account information |
| `accounts.md` | Bank accounts, ownership, account status, and balances |
| `credentials.md` | Valid and invalid login credentials |
| `transfers.md` | Reusable transfer data for valid and invalid scenarios |
| `boundary-values.md` | Boundary Value Analysis and Equivalence Partitioning data |

## Data Conventions

- All users, emails, account numbers, and credentials are synthetic.
- No real customer or financial information is used.
- Currency values are represented in USD.
- Monetary values use a maximum of two decimal places.
- Account numbers are 8-digit numeric values.
- Account statuses used in the test data include `Active`, `Closed`, and `Blocked`.
- Test data should be reusable across UI, API, database, and automation testing whenever possible.

## Data Reuse

The same test data should be referenced by test cases instead of creating new values for every test.

For example:

`users.md` → identifies the test user  
`accounts.md` → identifies source and destination accounts  
`credentials.md` → provides login credentials  
`transfers.md` → provides transfer-specific data  
`boundary-values.md` → provides boundary and partition values

This approach helps maintain consistency between test cases and makes later API, SQL, and Playwright testing easier.

## Test Data State

Some tests modify account balances or create transactions.

Before executing a test that depends on a specific initial state:

1. Verify the required test data state.
2. Reset the affected data if necessary.
3. Execute the test.
4. Restore the data when required for subsequent tests.

Test cases that depend on initial balances or account status should not rely on data modified by a previous test unless that dependency is explicitly documented.

## Scope

The data in this directory supports the current BlueBank Phase 1 scope:

- Login
- Account selection
- Money Transfer
- Transfer Confirmation
- Transfer Status
- Transaction History

Additional test data may be added as new features and testing layers are introduced.