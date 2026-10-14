# BlueBank QA Project

**A hands-on Software Quality Assurance (QA) learning project for a digital banking system.**

BlueBank is an educational project designed to demonstrate how software testing works in a realistic backend application. It combines requirements analysis, test design, API testing, database validation, automated testing, and test documentation.

The project is built step by step, from understanding business requirements to validating API behavior and preparing for more advanced automation.

> **Learning principle:** Do not just run a test and check whether it passes. Understand what is being tested, why it matters, what result is expected, and what evidence proves the result.

---

## Table of Contents

- [1. Project Overview](#1-project-overview)
- [2. Learning Objectives](#2-learning-objectives)
- [3. Project Status](#3-project-status)
- [4. Technology Stack](#4-technology-stack)
- [5. System Features](#5-system-features)
- [6. Project Structure](#6-project-structure)
- [7. Prerequisites](#7-prerequisites)
- [8. Getting Started](#8-getting-started)
- [9. Running the Backend](#9-running-the-backend)
- [10. Exploring the API](#10-exploring-the-api)
- [11. Running Automated Tests](#11-running-automated-tests)
- [12. Testing with Postman](#12-testing-with-postman)
- [13. Database Testing](#13-database-testing)
- [14. QA Documentation and Test Workflow](#14-qa-documentation-and-test-workflow)
- [15. Test Results and Evidence](#15-test-results-and-evidence)
- [16. Troubleshooting](#16-troubleshooting)
- [17. Learning Roadmap](#17-learning-roadmap)
- [18. How to Contribute](#18-how-to-contribute)
- [19. Important Notes](#19-important-notes)

---

## 1. Project Overview

BlueBank simulates selected operations of a digital banking application. The project provides a practical environment for learning how QA engineers analyze requirements, identify risks, design test scenarios, execute tests, validate APIs, and verify data integrity.

The project focuses on the backend of a banking system, where correctness, security, and data consistency are essential.

For example, a successful money transfer should do more than return an HTTP 200 response. A QA engineer should also consider:

- Was the correct amount deducted from the source account?
- Was the correct amount credited to the destination account?
- Can a user access another user's account?
- What happens when the balance is insufficient?
- Can a transfer be submitted twice with the same request reference?
- Is the transaction recorded correctly in the database and transaction history?

These questions help turn a simple API request into meaningful software testing.

### Project goals

- Learn the Software Testing Life Cycle (STLC).
- Practice requirement analysis and test design.
- Understand functional and negative testing.
- Work with REST APIs and HTTP status codes.
- Validate authentication and authorization.
- Use PostgreSQL for data verification.
- Write and execute automated tests with pytest.
- Organize API tests in Postman.
- Maintain traceability between requirements, scenarios, test cases, and defects.
- Prepare a foundation for Playwright, CI/CD, and advanced test automation.

---

## 2. Learning Objectives

This project is intended for beginners who want to build practical Software QA skills.

By working through the project, you can learn the following concepts:

| Area | What you will learn |
|---|---|
| Requirements analysis | Identify business rules and testable requirements |
| User stories | Understand user needs and acceptance criteria |
| Test analysis | Identify test conditions, risks, and expected behavior |
| Test design | Create scenarios and test cases |
| API testing | Send requests and validate responses |
| Authentication | Work with login and access tokens |
| Authorization | Verify that users can access only permitted resources |
| Database testing | Inspect records and validate data integrity |
| Negative testing | Check invalid inputs, unauthorized access, and business-rule violations |
| Automation | Execute repeatable tests with pytest |
| Postman | Organize requests, collection variables, and test scripts |
| Test documentation | Maintain test results, regression suites, and retest records |
| Version control | Track changes and collaborate using Git and GitHub |

**Recommended approach:** Follow the documented workflow in order. If you are new to QA, start with the project definition and business rules before running the tests.

---

## 3. Project Status

The project has progressed beyond the initial test-analysis stage. The following table distinguishes completed implementation and test activities from future work.

| Component | Current status |
|---|---|
| Project definition and business rules | Documented |
| User stories and acceptance criteria | Documented |
| Test analysis and scenarios | Documented |
| Requirements traceability matrix (RTM) | Available |
| FastAPI backend | Implemented |
| PostgreSQL database | Configured |
| Authentication API | Implemented and tested |
| Accounts API | Implemented and tested |
| Transfers API | Implemented and tested |
| Transactions API | Implemented and tested |
| Backend automated tests | 56 tests passed in the recorded test run |
| Postman collection | Exported and committed to GitHub |
| Regression and retest documentation | Available |
| Playwright automation | Planned |
| CI/CD pipeline | Planned |

The test results above represent recorded execution results, not a guarantee that every possible scenario has been tested.

### Current testing baseline

- Business rules: 19
- Money transfer acceptance criteria: 13
- Authentication acceptance criteria: 5
- Test scenarios: 61
- Backend automated tests: 56 passed in the recorded run

The number of scenarios is not necessarily the same as the number of automated tests. A scenario can require several test cases, and not every scenario is automated.

---

## 4. Technology Stack

The project uses the following technologies.

| Technology | Purpose |
|---|---|
| Python | Backend implementation and test automation |
| FastAPI | REST API development |
| PostgreSQL | Relational database |
| SQLAlchemy | Database interaction |
| Pydantic | Request and data validation |
| pytest | Automated test execution |
| Postman | Manual and scripted API testing |
| Git | Version control |
| GitHub | Source code and project documentation |
| PowerShell | Running commands on Windows |

Playwright and CI/CD are planned learning steps rather than completed capabilities.

---

## 5. System Features

The current backend includes the following API areas.

### 5.1 Authentication

The authentication API validates login credentials and returns an access token for authorized requests.

Example endpoint:

`POST /api/v1/auth/login`

### 5.2 Accounts

The accounts API provides access to account information, subject to authorization rules.

Example endpoints:

- `GET /api/v1/accounts`
- `GET /api/v1/accounts/{account_number}`

Testing considerations include account ownership, account status, valid account numbers, and unauthorized access.

### 5.3 Transfers

The transfers API supports money transfers between accounts.

Example endpoint:

`POST /api/v1/transfers`

Important test conditions include:

- Valid transfers
- Different source and destination accounts
- Sufficient account balance
- Amount validation and maximum limits
- Account status restrictions
- Request-reference uniqueness
- Correct balance updates

### 5.4 Transactions

The transactions API provides transaction history.

Example endpoint:

`GET /api/v1/transactions`

Testing should verify that transaction records are correct and visible only to authorized users.

### 5.5 Health check

The health endpoint provides a simple way to check whether the application is responding.

`GET /health`

Expected response:

```json
{
  "status": "healthy"
}
```

---

## 6. Project Structure

The repository separates backend code, QA documentation, test data, and testing assets.

```text
BlueBank-QA-Project/
│
├── README.md
├── PROJECT-CONTEXT.md
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── apis/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   │
│   ├── tests/
│   ├── conftest.py
│   ├── requirements.txt
│   ├── .env.example
│   └── test_db.py
│
├── api-testing/
│   └── postman/
│       ├── api-test-strategy.md
│       ├── endpoints.md
│       ├── test-scenarios.md
│       └── collections/
│           └── BlueBank-QA-API-Tests.json
│
├── docs/
│   ├── 01-project-definition.md
│   ├── 02-business-rules.md
│   ├── 03-user-story.md
│   ├── 04-acceptance-criteria.md
│   ├── 05-test-analysis.md
│   ├── 06-test-scenarios.md
│   ├── 07-traceability-matrix.md
│   └── README.md
│
├── bug-reports/
├── regression/
├── retest/
├── sql/
├── test-data/
└── test-execution/
```

Some folders contain additional files and subdirectories not shown above.

### Where should you start?

- `docs/`: Understand the requirements and testing approach.
- `backend/app/`: Explore the application implementation.
- `backend/tests/`: Read and run automated tests.
- `api-testing/postman/`: Learn the API testing strategy and use the exported collection.
- `sql/`: Review database creation and seed-data scripts.
- `test-data/`: Find example users, accounts, credentials, and boundary values.
- `test-execution/`: Review execution records and summaries.
- `bug-reports/`: Learn how defects should be documented.
- `regression/`: Review the regression test suite.
- `retest/`: Understand how fixes are verified.

---

## 7. Prerequisites

Before starting, install the following software on your computer.

### Required tools

1. **Python** — use a version compatible with the dependencies in `backend/requirements.txt`.
2. **PostgreSQL** — the database server used by the project.
3. **Git** — for source control.
4. **Postman** — for API testing.
5. **A code editor** — Visual Studio Code is a convenient option.

You should also understand basic command-line operations and JSON. You do not need to be an experienced developer to begin.

### Verify the installations

Open PowerShell and run:

```powershell
python --version
```

```powershell
git --version
```

Check that PostgreSQL is installed and that its database service is running.

If the `python` command is unavailable on your computer, try:

```powershell
py --version
```

---

## 8. Getting Started

This section explains how to prepare the project on Windows.

### Step 1: Clone the repository

If you do not already have the project locally:

```powershell
git clone https://github.com/mehrdadtest/BlueBank-QA-Project.git
```

Move into the project directory:

```powershell
cd BlueBank-QA-Project
```

If you already have the repository, open PowerShell in its root directory instead.

### Step 2: Create a Python virtual environment

From the project root, run:

```powershell
python -m venv venv
```

A virtual environment isolates the project's Python dependencies from other Python projects on your computer.

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because of its execution policy, do not change system-wide security settings automatically. You can run the environment's Python executable directly, as shown later in this guide.

### Step 3: Install backend dependencies

Move into the backend directory:

```powershell
cd backend
```

Install the required packages:

```powershell
..\venv\Scripts\python.exe -m pip install -r requirements.txt
```

This command installs the Python packages listed by the project.

### Step 4: Configure environment variables

The backend includes an `.env.example` file that documents the expected environment configuration.

From the `backend` directory, create a local `.env` file based on the example:

```powershell
Copy-Item .env.example .env
```

Open `.env` in your editor and set the values required by the project.

**Important:**

- Use your own local database credentials.
- Never commit your actual `.env` file or passwords to GitHub.
- Do not replace variable names with guesses; follow the names used in `.env.example` and the application configuration.
- Keep `.env.example` free of real secrets.

### Step 5: Prepare PostgreSQL

Create the databases and configure access according to the project configuration.

The repository includes SQL scripts under the root-level `sql/` directory:

- `01_create_tables.sql`
- `02_seed_data.sql`

Review the scripts before executing them. Use the appropriate database and connection settings, and confirm that the scripts are safe to rerun before running them on an existing database.

The automated test suite uses a separate test database named `bluebank_test`. Keep test data isolated from your development database.

### Step 6: Verify database connectivity

From the `backend` directory, run:

```powershell
..\venv\Scripts\python.exe test_db.py
```

A successful result should indicate that the database connection works.

If the connection fails, check the database service, database name, username, password, port, and environment configuration.

---

## 9. Running the Backend

Make sure you are in the `backend` directory and that the virtual environment dependencies are installed.

Start the FastAPI development server:

```powershell
..\venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

The server should start on the local development address.

Open the interactive API documentation in your browser:

**Swagger UI:** http://127.0.0.1:8000/docs

To check application health, open:

http://127.0.0.1:8000/health

Expected response:

```json
{
  "status": "healthy"
}
```

Keep the terminal running while testing the API.

To stop the server, press `Ctrl+C` in that terminal.

---

## 10. Exploring the API

FastAPI provides interactive API documentation through Swagger UI.

### Recommended learning sequence

1. Open `/docs`.
2. Find the authentication endpoint.
3. Review its request body and required fields.
4. Execute a login request using the project's documented test credentials.
5. Inspect the HTTP status code and JSON response.
6. Use the returned access token for protected endpoints.
7. Explore the accounts, transfers, and transactions APIs.

### Example login request

Endpoint:

`POST /api/v1/auth/login`

Request body:

```json
{
  "email": "john.doe@bluebank.test",
  "password": "12345678"
}
```

This is a sample credential from the local educational test data. It is not a real banking account.

A successful login returns an access token. Use the token as a Bearer token when calling protected endpoints.

### What should you validate?

Do not stop at checking whether the request succeeded. Validate:

- HTTP status code
- Response structure and data types
- Required response fields
- Business rules
- Authentication and authorization behavior
- Database changes, where applicable
- Error messages for invalid requests

For example, a user attempting to access another user's account should not receive that account's private information.

---

## 11. Running Automated Tests

The backend uses pytest to execute automated tests.

### Step 1: Configure the test database

The automated tests must use the dedicated `bluebank_test` database.

The test configuration accepts `TEST_DATABASE_URL`. In PowerShell, set it for the current session:

```powershell
$env:TEST_DATABASE_URL = "postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/bluebank_test"
```

Replace `YOUR_PASSWORD` with your actual local PostgreSQL password. Do not commit the real value or share it publicly.

This environment variable applies only to the current PowerShell session. Set it again in a new session when needed.

Before running tests, verify that the test configuration points to the test database rather than your development database.

### Step 2: Move into the backend directory

From the repository root:

```powershell
cd backend
```

### Step 3: Run the complete test suite

```powershell
..\venv\Scripts\python.exe -m pytest -v
```

The `-v` option displays individual test names and results.

A successful test is reported as `PASSED`. A failing test is reported as `FAILED`.

The recorded project baseline is **56 passed tests**. Your current result may differ if the code, dependencies, database, or tests have changed.

### Run a specific test file

For example:

```powershell
..\venv\Scripts\python.exe -m pytest tests/test_api.py -v
```

Use the actual file paths in `backend/tests/` if the test organization changes.

### How to understand a failed test

When a test fails:

1. Read the failing test name.
2. Read the assertion that failed.
3. Inspect the expected and actual values.
4. Check the API response or database state.
5. Determine whether the problem is in the application, the test, the configuration, or the test data.
6. Record the defect if the observed behavior violates a requirement.

A failing test does not automatically mean the application is defective. The test itself or its environment may also be incorrect.

---

## 12. Testing with Postman

The project includes an exported Postman collection:

`api-testing/postman/collections/BlueBank-QA-API-Tests.json`

### Import the collection

1. Open Postman.
2. Select **Import**.
3. Choose the JSON collection file.
4. Confirm that the collection appears in the sidebar.
5. Ensure the FastAPI server is running at `http://127.0.0.1:8000`.

### Recommended request order

Run the requests in this order when applicable:

1. Health Check
2. Login
3. Get Accounts
4. Get Account Details
5. Create Transfer
6. Get Transactions

The login request stores the access token in a collection variable. Protected requests use the `{{access_token}}` variable.

If a protected request returns an authentication error, run Login again and check that the token variable has been populated.

### Example transfer request

Endpoint:

`POST /api/v1/transfers`

Request body:

```json
{
  "source_account_number": "10001234",
  "destination_account_number": "30007890",
  "amount": 10,
  "request_reference": "POSTMAN-TRANSFER-001"
}
```

This is an example using the project's test data. Before executing it, verify that the accounts and balances match your current database state.

A successful transfer should be checked at several levels:

- The API response indicates the expected outcome.
- The source account balance is updated correctly.
- The destination account balance is updated correctly.
- The transaction is recorded.
- The transaction history is consistent with the transfer.
- The same request is not processed twice when the business rules require duplicate protection.

**Important:** A transfer changes financial test data. Use only the local educational environment and suitable test data. Do not repeatedly run a successful transfer without understanding its effects.

### Useful negative tests

Consider testing:

- Invalid login credentials
- Missing or invalid access token
- Access to another user's account
- Transfer between the same account
- Invalid amount or amount above the permitted limit
- Insufficient balance
- Closed or blocked accounts
- Reuse of a request reference
- Missing required fields

Validate the actual status code and response against the implementation and documented business rules. Do not assume every error must return the same HTTP status code.

---

## 13. Database Testing

API testing verifies behavior through requests and responses. Database testing helps confirm that the application stores and updates data correctly.

The project uses PostgreSQL and includes database scripts under `sql/`.

### Suggested validation workflow

For a money transfer:

1. Read the source and destination balances before the request.
2. Execute the transfer.
3. Read the balances again.
4. Confirm the debit and credit amounts.
5. Verify the transaction record.
6. Compare the API response with the database state.

For a successful transfer of 10.00, assuming there are no fees or other concurrent transactions:

- The source balance should decrease by 10.00.
- The destination balance should increase by 10.00.
- The transaction should reflect the correct amount and accounts.

The expected result must account for any additional rules implemented by the application.

### Why database checks matter

An API may return a success response even when the data is incorrect. Database validation provides additional evidence that the business operation completed as expected.

When testing destructive operations or modifying records manually, always use the test database and understand the consequences before executing SQL.

---

## 14. QA Documentation and Test Workflow

The repository separates the testing process into understandable stages.

### Stage 1: Understand the project

Start with:

- `docs/01-project-definition.md`
- `docs/02-business-rules.md`

Learn what the system is expected to do and identify important business constraints.

### Stage 2: Understand user needs

Read:

- `docs/03-user-story.md`
- `docs/04-acceptance-criteria.md`

User stories describe the user's goal. Acceptance criteria define conditions that must be satisfied for the feature to be accepted.

### Stage 3: Analyze and design tests

Read:

- `docs/05-test-analysis.md`
- `docs/06-test-scenarios.md`
- `docs/07-traceability-matrix.md`

A test scenario describes a situation or behavior to validate. A test case provides the detailed conditions, steps, test data, and expected result needed to execute a test.

The Requirements Traceability Matrix (RTM) helps connect requirements with test scenarios and test cases.

### Stage 4: Execute and record tests

Review:

- `test-execution/`
- `api-testing/postman/`

Record the actual result, execution status, and relevant evidence. Distinguish between tests that have been designed and tests that have actually been executed.

### Stage 5: Report defects

Use the template in:

`bug-reports/templates/bug-report-template.md`

A useful defect report contains a clear title, environment, preconditions, reproducible steps, expected result, actual result, severity or priority where appropriate, and supporting evidence.

### Stage 6: Retest and regression test

Review:

- `retest/`
- `regression/`

Retesting verifies whether a particular defect has been fixed. Regression testing checks whether a change has affected previously working functionality.

These activities are related but not interchangeable.

---

## 15. Test Results and Evidence

The project has a recorded backend test run with 56 passing tests.

The Postman collection has also been exported and committed to the repository. Postman assertions have been executed during the learning workflow.

For reproducibility, record:

- Date and environment of execution
- Application version or Git commit
- Test command or Postman request
- Expected result
- Actual result
- Pass/fail status
- Relevant response or database evidence
- Defect reference, if applicable

A test result is meaningful only when it can be traced to the test that was executed and the environment in which it ran.

Do not report a test as passed merely because it was written or added to a collection.

---

## 16. Troubleshooting

### Problem: Python is not recognized

Check whether Python is installed:

```powershell
py --version
```

If available, use `py` instead of `python` when creating the virtual environment.

### Problem: Dependency installation fails

Confirm that you are in the `backend` directory and that the virtual environment exists.

Run:

```powershell
..\venv\Scripts\python.exe -m pip install -r requirements.txt
```

Read the full error message before changing dependency versions.

### Problem: PostgreSQL connection fails

Check:

- PostgreSQL service status
- Host and port
- Database name
- Username and password
- Environment variable names
- Whether the database exists

Never solve a connection issue by switching the tests to the development database without understanding the risk.

### Problem: Tests complain about `YOUR_PASSWORD`

The test database URL still contains the example placeholder. Set `TEST_DATABASE_URL` to the actual local test-database connection string in the current PowerShell session.

Do not put the real password into source-controlled files.

### Problem: API returns connection or server errors

Confirm that the FastAPI server is running, check the URL and port, and inspect the backend terminal for a traceback.

### Problem: Postman returns an authentication error

Run the Login request again. Verify that the response contains an access token and that the collection variable is being populated.

### Problem: An account cannot be found

Check the account number, the current seed data, and the ownership rules. An account belonging to another user may intentionally be unavailable to the logged-in user.

### Problem: A transfer test produces unexpected balances

Review the account balances before execution, confirm the request reference, and check whether the request was already processed. Avoid repeating successful transfer requests with the same or different references until the data state is understood.

---

## 17. Learning Roadmap

The project is designed to grow gradually from foundational QA skills to automation engineering.

### Phase 1 — QA foundations and backend testing

**Current project stage**

- Understand requirements and business rules.
- Create user stories and acceptance criteria.
- Analyze risks and design test scenarios.
- Use RTM for traceability.
- Execute API tests using Postman.
- Validate database state.
- Run automated backend tests using pytest.
- Document execution, defects, retesting, and regression.

### Phase 2 — Strengthen API testing and automation

Planned learning activities:

- Improve reusable API test assertions.
- Organize positive, negative, boundary, and authorization tests.
- Learn test data management and isolation.
- Improve automated test reporting.
- Explore additional API testing techniques.

### Phase 3 — Playwright

Planned learning activities:

- Understand browser automation.
- Write maintainable automated tests.
- Validate UI behavior and API interactions.
- Learn fixtures, assertions, and test organization.
- Practice debugging failed tests.

### Phase 4 — CI/CD

Planned learning activities:

- Run automated tests in a CI pipeline.
- Learn how pull requests and automated checks work.
- Publish test results as part of the development workflow.
- Understand how automation supports regression testing.

### Phase 5 — Advanced QA

Possible future topics include:

- Performance testing
- Security testing fundamentals
- Contract testing
- Test architecture and maintainability
- AI-assisted testing
- Test strategy and risk-based testing

These phases describe the learning roadmap, not features that are already implemented.

---

## 18. How to Contribute

This is an educational project. Contributions and experiments should preserve the clarity and reproducibility of the testing workflow.

A suggested process:

1. Understand the relevant requirement and business rule.
2. Identify the behavior to validate.
3. Add or update the appropriate test scenario.
4. Implement or update the test case.
5. Execute the relevant tests against the correct environment.
6. Record results and investigate failures.
7. Update documentation when behavior or test coverage changes.
8. Review the changes before committing them.

Use descriptive commit messages and never commit credentials, access tokens, or other secrets.

---

## 19. Important Notes

- BlueBank is an educational project, not a real banking service.
- All example credentials and account numbers are for local testing only.
- Do not use real customer information or production credentials.
- Run transfer and database-modification tests only in an appropriate test environment.
- Keep secrets in local environment configuration, not in Git.
- A passing test suite provides evidence for the tested behavior; it does not prove that the application is free of defects.
- The implementation, test suite, and roadmap may evolve as the project progresses.

---

## Final Note

The purpose of BlueBank is not simply to produce a collection of test scripts. It is to demonstrate a QA workflow in which requirements, test design, execution, evidence, and defect analysis are connected.

**The most important skill is learning to explain why a test exists, what it proves, and what its result means.**
