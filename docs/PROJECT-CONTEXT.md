# BlueBank QA Project — Project Context

> Master continuation document. This file records the current project state, confirmed implementation details, documentation decisions, and next steps. Use it as the primary reference when continuing work across conversations.

## 1. Project Goal

Build a practical QA portfolio project around the fictional BlueBank banking application.

Primary goals:

1. Review ISTQB CTFL concepts through practical QA activities.
2. Build a GitHub-ready Software Testing portfolio.
3. Develop a Persian software-testing case study based on a realistic banking backend.
4. Practice Manual Testing, API Testing, SQL, and test automation.
5. Extend the project progressively toward Playwright, Python-based automation, and CI/CD.

## 2. Product Overview

**Product:** BlueBank  
**Product Type:** Fictional digital banking application  
**Current Implementation:** FastAPI backend with PostgreSQL database.

The project is educational and intended for QA practice and portfolio development. It is not a production banking system.

## 3. Current Project Status

### Completed or Implemented

- FastAPI backend structure.
- PostgreSQL database connection.
- Database tables for users, accounts, transfers, and transactions.
- Authentication API.
- Account listing and account-detail APIs.
- Money transfer API.
- Transaction history API.
- Request validation through Pydantic schemas.
- Business-rule validation for money transfers.
- Authorization and account-ownership checks.
- Balance updates and transaction-record creation.
- Rollback handling for transfer failures.
- Protection against concurrent transfers causing an overdraft.
- Automated API and backend tests using pytest.

### Current Automated Test Baseline

The latest reported pytest execution completed with:

**56 passed**

Command used from the `backend` directory:

```bash
python -m pytest .\tests -v
```

This result represents 56 passing pytest test items in that execution. It does not automatically mean that 56 unique business scenarios or all documented acceptance criteria have been verified.

The test count is a snapshot of a particular run and must be updated whenever the test suite changes.

### Important Status Distinction

- **Implemented:** The corresponding functionality exists in the application code.
- **Automated-tested:** Automated tests have been written for the behavior.
- **Passed:** The relevant test passed in a recorded execution.
- **Documented:** The requirement or expected behavior is recorded in project documentation.
- **Manually executed:** A formal manual test case has been executed and its result recorded.

These statuses must not be treated as interchangeable.

## 4. Current API Scope

The following endpoints are part of the known backend implementation:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/api/v1/auth/login` | User authentication |
| GET | `/api/v1/accounts` | List accessible bank accounts |
| GET | `/api/v1/accounts/{account_number}` | Retrieve account details |
| POST | `/api/v1/transfers` | Submit a money transfer |
| GET | `/api/v1/transactions` | Retrieve transaction history |

Endpoint behavior, response formats, status codes, and authorization rules must be confirmed against the current implementation before being documented as definitive.

Do not document an endpoint