# PROJECT-CONTEXT

## Purpose

Master status file for continuing the BlueBank QA project without
depending on chat history.

## Current Phase

Phase 1 --- Manual Test Analysis & Design

## Completed

-   Project Definition
-   Business Rules
-   User Stories
-   Acceptance Criteria
-   Test Analysis
-   Test Scenarios

## Baseline

-   19 Business Rules
-   18 Acceptance Criteria total (13 transfer + 5 authentication)
-   56 Test Conditions
-   61 Test Scenarios

## Important Decisions

-   Login has separate acceptance criteria.
-   Account number format (8 digits) is an explicit project
    assumption/rule.
-   Session expiry and retry-after-timeout are explicit assumptions.
-   Duplicate Amount=0 scenario was removed.
-   BlueBank is fictional.

## Next

Test Case Design → Execution → Bug Reporting → Retest → Regression → API
Testing → SQL → Playwright
