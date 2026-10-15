# BlueBank QA Project — Project Definition

## 1. Project Overview

BlueBank is a fictional digital banking platform designed to simulate selected banking operations in a realistic software testing environment.

The project focuses on customer authentication, bank account access, internal money transfers, and transaction history.

The current implementation is a backend application built with FastAPI and PostgreSQL. It provides REST APIs and automated tests to evaluate functional correctness, input validation, authentication, authorization, and data consistency.

The project is developed as a practical QA portfolio case study, demonstrating how software testing activities can be applied to a backend application, from requirements analysis and test design to test execution and automation.

BlueBank is an educational project and is not intended for real financial transactions.

## 2. Project Goals

The project aims to:

- Apply ISTQB CTFL concepts to a practical software testing project.
- Define user stories, business rules, and acceptance criteria.
- Perform test analysis and test design using documented requirements.
- Create and maintain traceable test scenarios and test cases.
- Execute functional and negative tests against REST APIs.
- Validate authentication, authorization, business rules, and data integrity.
- Use SQL and database inspection to support test verification.
- Automate repeatable tests using pytest and API-level testing techniques.
- Investigate failures, document defects when identified, and perform retesting.
- Establish a maintainable regression test suite.
- Demonstrate QA practices through a documented GitHub repository and related educational content.

## 3. Project Roles

| Role | Scope |
|---|---|
| Customer | In scope |
| Administrator | Out of scope |

The current scope focuses on customer-facing banking operations. Administrative workflows and privileged administrative interfaces are not part of Phase 1.

## 4. Product Capabilities

This section describes the intended product capabilities relevant to the project. It does not imply that every capability has a graphical interface or is implemented in the current release.

### 4.1 Authentication

- Customer login.
- Authentication of protected API requests.
- Rejection of invalid credentials and invalid authentication tokens.

A separate logout endpoint or session-management interface is not assumed unless implemented and verified.

### 4.2 Bank Accounts

- Retrieve the authenticated customer's accessible accounts.
- Retrieve the details of an account, subject to authorization.
- Prevent unauthorized access to other customers' account information.

### 4.3 Money Transfer

- Submit an internal transfer request.
- Validate the source and destination accounts.
- Validate the transfer amount.
- Check account ownership, account status, and available balance.
- Prevent duplicate transfer requests using the request reference.
- Update source and destination balances after successful processing.
- Create the corresponding transfer and transaction records.
- Preserve data consistency if processing fails.
- Prevent concurrent transfers from causing an overdraft.

### 4.4 Transaction History

- Retrieve transaction history through the API.
- Apply the implemented access-control rules.
- Verify that successfully processed transfers are represented in transaction records.

A graphical dashboard, transfer form, confirmation page, or transaction-status screen is not part of the verified backend scope unless separately implemented.

## 5. Phase 1 Scope

### 5.1 In Scope

The current Phase 1 backend scope includes:

- Customer login.
- Authentication and authorization of protected endpoints.
- Account listing and account-detail retrieval.
- Internal money transfers.
- Transfer request validation.
- Source-account ownership and account-status checks.
- Destination-account existence and account-status checks.
- Transfer amount and available-balance validation.
- Duplicate request-reference protection.
- Source and destination balance updates.
- Transfer and transaction record creation.
- Transaction-history retrieval and access control.
- Database rollback when transfer processing fails.
- Protection against overdrafts caused by concurrent transfers.
- Automated API, schema, and service-level tests.
- Database-backed verification of relevant behavior.

### 5.2 Out of Scope

The following capabilities are outside the current Phase 1 scope unless explicitly added in a later iteration:

- Customer registration.
- Password recovery and reset.
- Administrative workflows and an admin panel.
- Card management.
- Bill payments.
- Loan management.
- Notifications.
- A native mobile application.
- A customer-facing web UI.
- UI-based transfer confirmation.
- Performance and load testing.
- Dedicated security penetration testing.
- External bank integrations and interbank transfers.

Authentication and authorization checks are part of Phase 1. Excluding dedicated penetration testing does not mean that basic security-related functional checks are excluded.

## 6. Main Business Flow

The current backend flow is:

Customer  
→ Login API  
→ Retrieve accessible accounts  
→ Submit a transfer request  
→ Validate request data  
→ Verify source and destination accounts  
→ Check ownership, account status, and available balance  
→ Check request-reference uniqueness  
→ Process transfer  
→ Update account balances  
→ Create transfer and transaction records  
→ Commit database changes  
→ Retrieve transaction history

If a transfer fails during processing, the system should reject the operation and roll back its database changes as applicable.

This flow represents backend processing. It does not imply that a dashboard, account-selection screen, review page, or confirmation button exists.

## 7. Test Objectives

The QA activities aim to verify the following behaviors:

### Authentication and Authorization

- Successful and unsuccessful login.
- Rejection of missing, invalid, tampered, and expired tokens where applicable.
- Protection of endpoints requiring authentication.
- Prevention of unauthorized account and transaction-history access.

### Account Management

- Successful account listing and account-detail retrieval.
- Rejection of requests for inaccessible accounts.
- Validation of source-account ownership and account status.

### Money Transfer

- Request-schema validation.
- Transfer amount and decimal-precision validation.
- Destination-account existence and status validation.
- Source and destination account consistency.
- Available-balance enforcement.
- Duplicate request-reference rejection.
- Correct source and destination balance updates.
- Correct transfer and transaction record creation.
- Rollback when transfer processing fails.
- Protection against concurrent overdrafts.

### Transaction History

- Retrieval of authorized transaction records.
- Inclusion of transactions according to the implemented query rules.
- Exclusion of records belonging exclusively to unrelated users.
- Consistency between successful transfers and transaction records.

### Test Automation and Regression

- Repeatable execution of automated tests.
- Verification of API responses and relevant database state.
- Regression testing after changes to business logic or validation.
- Traceability between requirements, business rules, scenarios, and automated tests.

## 8. Project Assumptions and Constraints

- BlueBank is a fictional educational product.
- The intended currency is USD.
- The transfer request schema enforces an amount greater than zero and a maximum of `10000`.
- Transfer amounts are limited to two decimal places.
- Account-number validation in the current request schema allows 8–20 digits. An eight-digit-only rule must not be assumed unless the implementation is changed.
- The source account must belong to the authenticated user.
- Source and destination accounts must exist and be active.
- Source and destination accounts must be different.
- A transfer cannot exceed the available source-account balance.
- A duplicate request reference must not create a duplicate successful transfer.
- Successful transfers update both account balances and create the corresponding records.
- Transfer processing must preserve database consistency.
- Concurrent transfer processing must not allow the source account to be overdrawn.
- Protected API access requires valid authentication.
- Transaction-history visibility is governed by the implemented authorization and query rules.
- Business behavior is considered verified only when supported by the implementation and relevant test evidence.

## 9. Technology Stack

The current project uses the following technologies:

| Technology | Purpose |
|---|---|
| Python | Backend implementation and test code |
| FastAPI | REST API development |
| PostgreSQL | Relational database |
| SQLAlchemy | Database interaction and ORM |
| Pydantic | Request validation and data schemas |
| pytest | Automated test execution |
| Git and GitHub | Version control and portfolio publication |

The precise versions and additional dependencies should be documented in `requirements.txt` and the repository's setup instructions.

## 10. Test Evidence and Reporting

Automated test results must be reported using evidence from actual test executions.

A successful pytest run reporting `56 passed` means that 56 pytest test items passed in that execution. It does not automatically prove that 56 independent business scenarios were covered or that every documented requirement was tested.

The project documentation should distinguish between:

- Documented requirements and business rules.
- Designed test scenarios and test cases.
- Implemented automated tests.
- Executed tests and their results.
- Verified requirement coverage.
- Known limitations and unverified assumptions.

Requirements and business rules should be marked as covered only when the relevant tests provide sufficient evidence.

## 11. Project Deliverables

The project repository may include:

- Project definition and scope.
- User stories and acceptance criteria.
- Business rules.
- Test analysis and test scenarios.
- Test cases and traceability matrix.
- Automated API, schema, and service tests.
- Test execution records.
- Defect reports, when defects are identified.
- Setup instructions and API documentation.
- Regression testing documentation.

Each deliverable should reflect the current state of the implementation rather than planned or hypothetical functionality.

## 12. Project Disclaimer

BlueBank is a fictional banking application created for educational, software testing, and portfolio purposes. It is not a production banking system and must not be used to process real financial transactions.
