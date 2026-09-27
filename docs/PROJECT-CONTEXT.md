# BlueBank QA Project --- Project Context

> Master continuation document. This file preserves the current project
> state so future work does not depend on chat history.

## Project Goal

Build a practical QA portfolio project around the fictional BlueBank
banking application.

Primary goals:

1.  Review ISTQB CTFL concepts through practical work.
2.  Build a GitHub-ready QA portfolio.
3.  Create material for a Persian software-testing case study.
4.  Continue later with API Testing, SQL, Playwright, and automation.

## Current Phase

**Phase 1 --- Manual Test Analysis & Design**

Status: Completed.

The next step is **Test Case Design**.

## Product

BlueBank --- fictional digital banking platform.

## Phase 1 Scope

### In Scope

-   Login
-   Money Transfer
-   Transfer Confirmation
-   Transfer Status
-   Transaction History

### Out of Scope

-   Registration
-   Password Recovery
-   Admin Panel
-   Card Management
-   Bill Payment
-   Loan Management
-   Notifications
-   Mobile Application
-   Performance Testing
-   Security Penetration Testing

## Completed Artifacts

-   `01-project-definition.md`
-   `02-business-rules.md`
-   `03-user-story.md`
-   `04-acceptance-criteria.md`
-   `05-test-analysis.md`
-   `06-test-scenarios.md`
-   `07-traceability-matrix.md`

## Current Baseline

-   Business Rules: 19
-   Acceptance Criteria: 18 total
    -   13 Money Transfer
    -   5 Authentication
-   Test Conditions: 56
-   Test Scenarios: 61
-   Formal Test Cases: Not created
-   Test Execution: Not started
-   Bug Reports: Not created
-   Retest: Not started
-   Regression: Not started
-   API Testing: Not started
-   SQL: Not started
-   Playwright: Not started

## Important Decisions

1.  Login has separate acceptance criteria because Login is part of
    Phase 1 scope.
2.  Account number format (8 digits) is an explicit project
    assumption/business rule.
3.  Session expiry behavior is explicitly defined.
4.  Retry-after-timeout/idempotency behavior is explicitly defined.
5.  The duplicate zero-amount scenario was removed.
6.  BlueBank is fictional and exists only for educational and portfolio
    purposes.

## Next Steps

1.  Create formal Test Cases.
2.  Review Test Cases.
3.  Execute Test Cases.
4.  Create realistic Bug Reports.
5.  Retest fixed defects.
6.  Build Regression Set.
7.  Complete traceability.
8.  Start API Testing with Postman.
9.  Add SQL testing.
10. Add Playwright automation.
