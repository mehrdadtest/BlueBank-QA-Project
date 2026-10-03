# BlueBank Regression Test Suite

## 1. Purpose

Regression Testing verifies that changes made to the BlueBank application have not introduced unintended problems in previously working functionality.

Regression Testing is especially important when changes affect:

* Authentication
* Account validation
* Transfer validation
* Balance calculation
* Transaction creation
* Transaction History
* Duplicate transfer prevention

Regression Testing does not mean executing every available test case after every change.

Instead, an appropriate set of tests is selected based on the scope and risk of the change.

---

## 2. Regression Testing vs Retesting

Retesting and Regression Testing serve different purposes.

| Retesting                                       | Regression Testing                                    |
| ----------------------------------------------- | ----------------------------------------------------- |
| Verifies that a specific defect has been fixed  | Checks whether changes caused unintended side effects |
| Focuses on the original failed test             | Covers related existing functionality                 |
| Based on a known defect                         | Based on change impact and risk                       |
| Uses the original failure as the starting point | Uses a selected regression suite                      |

Example:

If a defect causes the source balance to be calculated incorrectly, the failed balance test should first be Retested.

After that, related transfer and transaction tests should be included in Regression Testing.

---

## 3. Regression Test Selection Principles

Regression tests are selected based on:

* Changed functionality
* Affected components
* Business risk
* Dependency between features
* Severity of previous defects
* Criticality of the user journey
* Data and database impact
* API impact
* UI impact

The selected suite should be reviewed whenever the application changes significantly.

---

## 4. BlueBank Regression Areas

The BlueBank regression suite is divided into the following areas:

1. Authentication
2. Account Selection
3. Destination Validation
4. Transfer Amount Validation
5. Balance Validation
6. Transfer Confirmation
7. Successful Transfer
8. Transaction History
9. Duplicate Transfer Prevention
10. End-to-End Transfer

---

# 5. Authentication Regression

These tests verify that changes to authentication have not affected access to the transfer functionality.

| Test Case | Scenario                             | Priority |
| --------- | ------------------------------------ | -------- |
| TC-001    | Valid Login                          | High     |
| TC-002    | Wrong Password                       | High     |
| TC-003    | Unregistered Email                   | High     |
| TC-006    | Access Transfer Without Login        | High     |
| TC-007    | Access Transfer with Expired Session | High     |
| TC-008    | Preserve Valid Session into Transfer | Medium   |

---

# 6. Account Regression

These tests verify source-account ownership and eligibility.

| Test Case | Scenario                                 | Priority |
| --------- | ---------------------------------------- | -------- |
| TC-009    | Display Active User Accounts             | High     |
| TC-010    | Exclude Inactive/Closed/Blocked Accounts | High     |
| TC-011    | Exclude Another User's Account           | High     |
| TC-012    | Select Valid Source Account              | High     |
| TC-014    | Unauthorized Source Account              | High     |

---

# 7. Destination Regression

These tests verify that transfer destinations are properly validated.

| Test Case | Scenario                    | Priority |
| --------- | --------------------------- | -------- |
| TC-015    | Valid Destination Account   | High     |
| TC-016    | Nonexistent Destination     | High     |
| TC-017    | Closed Destination          | High     |
| TC-018    | Blocked Destination         | High     |
| TC-019    | Same Source and Destination | High     |
| TC-021    | Invalid Destination Format  | High     |

---

# 8. Amount Validation Regression

Amount validation contains several important boundary and equivalence tests.

| Test Case | Scenario                       | Priority |
| --------- | ------------------------------ | -------- |
| TC-022    | Amount Below Minimum           | High     |
| TC-023    | Minimum Amount                 | High     |
| TC-024    | Amount Just Above Minimum      | Medium   |
| TC-025    | Normal Valid Amount            | High     |
| TC-027    | Amount with Two Decimal Places | Medium   |
| TC-028    | Amount Near Maximum            | High     |
| TC-029    | Maximum Amount                 | High     |
| TC-030    | Amount Above Maximum           | High     |
| TC-031    | Negative Amount                | High     |
| TC-033    | Non-Numeric Amount             | High     |
| TC-035    | More Than Two Decimal Places   | High     |

---

# 9. Balance Regression

These tests verify the relationship between transfer amount and available balance.

| Test Case | Scenario                            | Priority |
| --------- | ----------------------------------- | -------- |
| TC-036    | Transfer Below Available Balance    | High     |
| TC-037    | Transfer Equal to Available Balance | High     |
| TC-038    | Transfer Above Available Balance    | High     |
| TC-039    | Zero Balance                        | High     |
| TC-040    | Balance Below Minimum Transfer      | Medium   |

---

# 10. Confirmation Regression

These tests verify that transfer confirmation remains correct after changes.

| Test Case | Scenario                          | Priority |
| --------- | --------------------------------- | -------- |
| TC-041    | Verify Confirmation Data          | High     |
| TC-042    | Confirm Valid Transfer            | Critical |
| TC-043    | Cancel Before Confirmation        | High     |
| TC-044    | Navigate Back Before Confirmation | Medium   |
| TC-045    | Change Amount Before Confirmation | High     |

---

# 11. Successful Transfer Regression

These tests verify the core transfer operation.

| Test Case | Scenario                     | Priority |
| --------- | ---------------------------- | -------- |
| TC-046    | Successful Transfer          | Critical |
| TC-047    | Unique Transaction ID        | High     |
| TC-048    | Source Balance Update        | Critical |
| TC-049    | Destination Balance Update   | Critical |
| TC-050    | Transfer Appears in History  | High     |
| TC-051    | Transaction History Accuracy | High     |
| TC-052    | Transfer Status              | High     |

---

# 12. Duplicate Transfer Regression

Duplicate prevention is important because changes to the transfer workflow or API can unintentionally create duplicate transactions.

| Test Case | Scenario                     | Priority |
| --------- | ---------------------------- | -------- |
| TC-053    | Double-Click Confirm         | Critical |
| TC-054    | Resend Same Transfer Request | Critical |
| TC-055    | Retry After Timeout          | Critical |
| TC-056    | Duplicate History Prevention | Critical |

---

# 13. End-to-End Regression

The following tests validate complete business journeys.

| Test Case | Scenario                                 | Priority |
| --------- | ---------------------------------------- | -------- |
| TC-057    | Successful End-to-End Transfer           | Critical |
| TC-058    | Insufficient Balance End-to-End          | Critical |
| TC-059    | Invalid Destination End-to-End           | Critical |
| TC-060    | Full Available Balance End-to-End        | Critical |
| TC-061    | Duplicate Transfer Prevention End-to-End | Critical |

---

# 14. Core Regression Suite

For a small and fast regression cycle, the following tests form the **Core Regression Suite**.

| Test Case | Purpose                                   |
| --------- | ----------------------------------------- |
| TC-001    | Verify login                              |
| TC-006    | Verify unauthenticated access restriction |
| TC-009    | Verify source account availability        |
| TC-015    | Verify valid destination                  |
| TC-019    | Verify same-account rejection             |
| TC-023    | Verify minimum amount                     |
| TC-029    | Verify maximum amount                     |
| TC-030    | Verify amount above maximum               |
| TC-036    | Verify transfer below balance             |
| TC-037    | Verify full available balance             |
| TC-038    | Verify insufficient balance               |
| TC-041    | Verify confirmation                       |
| TC-042    | Verify transfer confirmation              |
| TC-046    | Verify successful transfer                |
| TC-048    | Verify source balance update              |
| TC-049    | Verify destination balance update         |
| TC-050    | Verify transaction history                |
| TC-053    | Verify duplicate prevention               |
| TC-057    | Verify successful end-to-end flow         |
| TC-061    | Verify duplicate prevention end-to-end    |

**Core Regression Suite: 20 Test Cases**

---

# 15. Impact-Based Regression

The complete regression suite does not necessarily need to be executed after every change.

### Example 1 — Login Change

If the authentication module changes:

```text
TC-001
TC-002
TC-003
TC-006
TC-007
TC-008
TC-057
```

The purpose is to verify both authentication and its impact on the transfer journey.

### Example 2 — Transfer Amount Validation Change

If the transfer amount validation changes:

```text
TC-022
TC-023
TC-024
TC-025
TC-027
TC-028
TC-029
TC-030
TC-031
TC-033
TC-035
TC-036
TC-037
TC-038
TC-040
TC-057
TC-058
TC-060
```

### Example 3 — Balance Calculation Change

If balance calculation changes:

```text
TC-036
TC-037
TC-038
TC-039
TC-040
TC-046
TC-048
TC-049
TC-057
TC-058
TC-060
TC-061
```

### Example 4 — Transaction Processing Change

If transaction creation or transaction history changes:

```text
TC-046
TC-047
TC-050
TC-051
TC-052
TC-053
TC-054
TC-055
TC-056
TC-057
TC-061
```

---

# 16. Regression Entry Criteria

Regression Testing can begin when:

* The relevant fix or change has been deployed.
* Required Retesting has been completed where applicable.
* The test environment is available.
* Required test data is available.
* The affected areas have been identified.
* The appropriate regression scope has been selected.

---

# 17. Regression Exit Criteria

A Regression cycle can be considered complete when:

* Selected regression tests have been executed.
* Critical regression tests have passed.
* New failures have been investigated.
* New defects have been reported.
* Relevant reopened defects have been handled.
* Remaining risks have been documented.

---

# 18. Regression Traceability

Regression Testing extends the project's overall lifecycle:

```text
Requirement
    ↓
Test Case
    ↓
Initial Execution
    ↓
Failure
    ↓
Bug
    ↓
Fix
    ↓
Retest
    ↓
Regression
```

This demonstrates that testing continues after the initial execution and is not limited to finding defects once.

---

# 19. Current Status

The Regression Suite has been designed but has not yet been executed.

Current status:

* Core Regression Suite: Defined
* Full Regression Suite: Defined
* Impact-Based Regression: Defined
* Regression Execution: Not Started
* Regression Defects: 0
