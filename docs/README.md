# BlueBank QA Project

A practical Software Testing and QA portfolio project built around **BlueBank**, a fictional digital banking platform.

This project combines requirements analysis, test design, backend/API testing, database validation, and automated testing. It demonstrates how QA activities can be connected to an actual application implementation rather than remaining limited to theoretical test documentation.

## Project Goals

- Apply ISTQB CTFL concepts to a practical project.
- Practice requirements analysis, business-rule identification, and acceptance-criteria definition.
- Design test conditions, test scenarios, and formal test cases.
- Test REST APIs and validate authentication, authorization, and business rules.
- Verify database integrity and transaction behavior.
- Develop automated tests using Python and pytest.
- Build a structured, evidence-based QA portfolio for GitHub.
- Extend the project toward SQL testing, Postman, and additional automation.

## Project Overview

BlueBank is a fictional digital banking backend that supports authentication, bank account inquiry, money transfers, and transaction history.

### Technology Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **Validation:** Pydantic
- **Database access:** SQLAlchemy
- **Automated testing:** pytest
- **API documentation:** FastAPI-generated interactive documentation

## Implemented API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/api/v1/auth/login` | Authenticate a user |
| GET | `/api/v1/accounts` | Retrieve accessible bank accounts |
| GET | `/api/v1/accounts/{account_number}` | Retrieve account details |
| POST | `/api/v1/transfers` | Submit a money transfer |
| GET | `/api/v1/transactions` | Retrieve transaction history |

Endpoint availability does not imply that every possible response, edge case, or security scenario has been verified. Refer to the implementation and test evidence for the current level of coverage.

## Current Project Status

### Implemented

- FastAPI backend and PostgreSQL integration.
- Authentication and protected API operations.
- Account listing and account-detail retrieval.
- Money transfer processing and business-rule validation.
- Source and destination balance updates.
- Transfer and transaction record creation.
- Error handling and rollback behavior.
- Automated backend/API tests using pytest.

### Automated Test Baseline

The latest reported test execution completed successfully:

**56 passed**

Run the test suite from the `backend` directory:

```bash
python -m pytest .\tests -v
```

The result represents 56 passing pytest test items in that execution. It should not be interpreted as 56 unique business scenarios, complete requirements coverage, or proof that every documented behavior has been verified.

### QA Documentation

Project documentation covers the project definition, user stories, business rules, acceptance criteria, test analysis, test scenarios, and traceability.

The documentation is being aligned with the implemented backend and its automated tests. Historical counts from earlier test-design documents should not be treated as the current baseline until that reconciliation is complete.

### Planned Work

- Reconcile test scenarios with the current implementation and automated tests.
- Complete formal test cases.
- Strengthen the requirements-to-test traceability matrix.
- Record repeatable test execution evidence.
- Add SQL-based database verification.
- Develop and execute a Postman collection.
- Expand automated test coverage where useful.
- Introduce Playwright if a frontend becomes available, or continue expanding API automation.

## Project Structure

```text
BlueBank-QA-Project/
│
├── README.md
├── PROJECT-CONTEXT.md
│
├── docs/
│   ├── 00-project-definition.md
│   ├── 01-user-stories.md
│   ├── 02-business-rules.md
│   ├── 03-acceptance-criteria.md
│   ├── 04-test-analysis.md
│   ├── 05-test-scenarios.md
│   ├── 06-test-cases.md
│   └── 07-traceability-matrix.md
│
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── ...
│
├── test-cases/
├── test-execution/
├── bug-reports/
├── regression/
├── api-testing/
├── sql/
├── automation/
└── test-data/
```

The tree describes the intended documentation and artifact organization. Verify the actual repository before assuming every listed file or directory already exists.

## How to Run the Automated Tests

1. Set up the Python environment and install the dependencies listed in `backend/requirements.txt`.
2. Configure the required environment variables using the project's environment template.
3. Configure the dedicated test database according to the project configuration.
4. Open a terminal in the `backend` directory.
5. Run:

```bash
python -m pytest .\tests -v
```

**Important:** Use a dedicated test database. Review the project's database safety checks and configuration before running tests. Never publish database passwords, secret keys, access tokens, or other credentials in the repository.

## QA Areas Covered

The project includes testing considerations for:

- Authentication and token validation.
- Authorization and account ownership.
- Request-schema and boundary-value validation.
- Transfer business rules.
- Insufficient funds and inactive accounts.
- Duplicate request references.
- Source and destination balance integrity.
- Transaction history and access control.
- Rollback behavior after failures.
- Concurrent transfers and overdraft prevention.

These are testing areas, not a claim that every possible case has passed. Refer to the actual test suite and recorded results for evidence.

## Traceability Approach

The intended traceability chain is:

**User Story → Business Rule → Acceptance Criterion → Test Condition → Test Scenario → Test Case → Test Execution → Defect (if identified) → Retest → Regression**

This structure helps connect business expectations to test design, execution results, and defect resolution.

## Project Scope and Limitations

- BlueBank is fictional and intended for educational and portfolio purposes.
- The current implementation is backend/API-focused.
- A frontend, login form, transfer confirmation screen, or other UI component should not be assumed to exist.
- Production banking integrations are not part of the project.
- Comprehensive performance testing and security penetration testing are not claimed.
- Project status and test metrics should be updated using actual implementation and execution evidence.

## Repository

[BlueBank QA Project on GitHub](https://github.com/mehrdadtest/BlueBank-QA-Project)

## Disclaimer

BlueBank is a fictional project created for learning, experimentation, and QA portfolio development. It is not intended for real financial transactions or production banking use.
