# BlueBank Test Execution

## 1. Purpose

This document records the execution results of the BlueBank test cases.

The Test Execution phase validates the behavior of the system against the expected results defined in the Test Cases.

At this stage, the BlueBank application has not yet been implemented or connected to an executable test environment. Therefore, no Pass or Fail result is assigned without actual execution evidence.

---

## 2. Execution Status

The following statuses are used during Test Execution:

| Status         | Description                                                                          |
| -------------- | ------------------------------------------------------------------------------------ |
| Not Executed   | Test case has not yet been executed                                                  |
| Pass           | Actual result matches the expected result                                            |
| Fail           | Actual result does not match the expected result                                     |
| Blocked        | Test cannot be executed because of an environment, dependency, or prerequisite issue |
| Not Applicable | Test is not applicable to the current execution scope                                |

---

## 3. Execution Information

| Field            | Value                      |
| ---------------- | -------------------------- |
| Project          | BlueBank QA Project        |
| Test Suite       | BlueBank Manual Test Suite |
| Test Cases       | 61                         |
| Execution Status | Not Started                |
| Environment      | Not Available              |
| Build Version    | Not Available              |
| Tester           | TBD                        |
| Execution Date   | TBD                        |

---

## 4. Test Execution Records

| Test Case | Scenario                                 | Priority | Status       | Actual Result | Bug ID | Notes |
| --------- | ---------------------------------------- | -------- | ------------ | ------------- | ------ | ----- |
| TC-001    | Valid Login                              | High     | Not Executed | -             | -      | -     |
| TC-002    | Login with Wrong Password                | High     | Not Executed | -             | -      | -     |
| TC-003    | Login with Unregistered Email            | High     | Not Executed | -             | -      | -     |
| TC-004    | Login with Blank Email                   | Medium   | Not Executed | -             | -      | -     |
| TC-005    | Login with Blank Password                | Medium   | Not Executed | -             | -      | -     |
| TC-006    | Access Transfer Without Login            | High     | Not Executed | -             | -      | -     |
| TC-007    | Access Transfer with Expired Session     | High     | Not Executed | -             | -      | -     |
| TC-008    | Preserve Valid Session into Transfer     | Medium   | Not Executed | -             | -      | -     |
| TC-009    | Display Active User Accounts             | High     | Not Executed | -             | -      | -     |
| TC-010    | Exclude Inactive/Closed/Blocked Accounts | High     | Not Executed | -             | -      | -     |
| TC-011    | Exclude Another User's Account           | High     | Not Executed | -             | -      | -     |
| TC-012    | Select Valid Source Account              | High     | Not Executed | -             | -      | -     |
| TC-013    | User with No Active Account              | Medium   | Not Executed | -             | -      | -     |
| TC-014    | Unauthorized Source Account              | High     | Not Executed | -             | -      | -     |
| TC-015    | Valid Destination Account                | High     | Not Executed | -             | -      | -     |
| TC-016    | Nonexistent Destination                  | High     | Not Executed | -             | -      | -     |
| TC-017    | Closed Destination                       | High     | Not Executed | -             | -      | -     |
| TC-018    | Blocked Destination                      | High     | Not Executed | -             | -      | -     |
| TC-019    | Same Source and Destination              | High     | Not Executed | -             | -      | -     |
| TC-020    | Empty Destination                        | Medium   | Not Executed | -             | -      | -     |
| TC-021    | Invalid Destination Format               | High     | Not Executed | -             | -      | -     |
| TC-022    | Amount Below Minimum                     | High     | Not Executed | -             | -      | -     |
| TC-023    | Minimum Amount                           | High     | Not Executed | -             | -      | -     |
| TC-024    | Amount Just Above Minimum                | Medium   | Not Executed | -             | -      | -     |
| TC-025    | Normal Valid Amount                      | High     | Not Executed | -             | -      | -     |
| TC-026    | Valid Decimal Amount                     | Medium   | Not Executed | -             | -      | -     |
| TC-027    | Amount with Two Decimal Places           | Medium   | Not Executed | -             | -      | -     |
| TC-028    | Amount Near Maximum                      | High     | Not Executed | -             | -      | -     |
| TC-029    | Maximum Amount                           | High     | Not Executed | -             | -      | -     |
| TC-030    | Amount Above Maximum                     | High     | Not Executed | -             | -      | -     |
| TC-031    | Negative Amount                          | High     | Not Executed | -             | -      | -     |
| TC-032    | Blank Amount                             | Medium   | Not Executed | -             | -      | -     |
| TC-033    | Non-Numeric Amount                       | High     | Not Executed | -             | -      | -     |
| TC-034    | Illegal Characters in Amount             | Medium   | Not Executed | -             | -      | -     |
| TC-035    | More Than Two Decimal Places             | High     | Not Executed | -             | -      | -     |
| TC-036    | Transfer Below Available Balance         | High     | Not Executed | -             | -      | -     |
| TC-037    | Transfer Equal to Available Balance      | High     | Not Executed | -             | -      | -     |
| TC-038    | Transfer Above Available Balance         | High     | Not Executed | -             | -      | -     |
| TC-039    | Zero Balance                             | High     | Not Executed | -             | -      | -     |
| TC-040    | Balance Below Minimum Transfer           | Medium   | Not Executed | -             | -      | -     |
| TC-041    | Verify Confirmation Data                 | High     | Not Executed | -             | -      | -     |
| TC-042    | Confirm Valid Transfer                   | Critical | Not Executed | -             | -      | -     |
| TC-043    | Cancel Before Confirmation               | High     | Not Executed | -             | -      | -     |
| TC-044    | Navigate Back Before Confirmation        | Medium   | Not Executed | -             | -      | -     |
| TC-045    | Change Amount Before Confirmation        | High     | Not Executed | -             | -      | -     |
| TC-046    | Successful Transfer                      | Critical | Not Executed | -             | -      | -     |
| TC-047    | Unique Transaction ID                    | High     | Not Executed | -             | -      | -     |
| TC-048    | Source Balance Update                    | Critical | Not Executed | -             | -      | -     |
| TC-049    | Destination Balance Update               | Critical | Not Executed | -             | -      | -     |
| TC-050    | Transfer Appears in History              | High     | Not Executed | -             | -      | -     |
| TC-051    | Transaction History Accuracy             | High     | Not Executed | -             | -      | -     |
| TC-052    | Transfer Status                          | High     | Not Executed | -             | -      | -     |
| TC-053    | Double-Click Confirm                     | Critical | Not Executed | -             | -      | -     |
| TC-054    | Resend Same Transfer Request             | Critical | Not Executed | -             | -      | -     |
| TC-055    | Retry After Timeout                      | Critical | Not Executed | -             | -      | -     |
| TC-056    | Duplicate History Prevention             | Critical | Not Executed | -             | -      | -     |
| TC-057    | Successful End-to-End Transfer           | Critical | Not Executed | -             | -      | -     |
| TC-058    | Insufficient Balance End-to-End          | Critical | Not Executed | -             | -      | -     |
| TC-059    | Invalid Destination End-to-End           | Critical | Not Executed | -             | -      | -     |
| TC-060    | Full Available Balance End-to-End        | Critical | Not Executed | -             | -      | -     |
| TC-061    | Duplicate Transfer Prevention End-to-End | Critical | Not Executed | -             | -      | -     |

---

## 5. Execution Rules

During actual execution, the following rules will be followed:

### 5.1 Pass

A test case is marked **Pass** when the actual behavior matches the expected result defined in the corresponding Test Case.

### 5.2 Fail

A test case is marked **Fail** when the actual behavior differs from the expected result.

A failed test should normally result in a Bug Report unless the failure is caused by an invalid test environment or test data issue.

### 5.3 Blocked

A test case is marked **Blocked** when execution cannot continue because of an external dependency.

Examples:

* Application is unavailable.
* Required test account does not exist.
* Database is unavailable.
* Required API is unavailable.
* Test environment is not configured.

### 5.4 Not Executed

A test case remains **Not Executed** when execution has not started.

---

## 6. Actual Result Recording

When a test is executed, the `Actual Result` column must contain the observed system behavior rather than a copy of the Expected Result.

For example:

**Expected Result:**

> The transfer is rejected and an appropriate validation message is displayed.

**Actual Result:**

> Transfer was rejected, but no validation message was displayed.

This test would be marked:

**Fail**

and linked to a Bug Report.

---

## 7. Defect Linkage

When a test case fails, its `Bug ID` column should reference the corresponding defect.

Example:

| Test Case | Status | Bug ID  |
| --------- | ------ | ------- |
| TC-030    | Fail   | BUG-001 |

The relationship is therefore:

```text
Test Case
    ↓
Execution
    ↓
Fail
    ↓
Bug Report
    ↓
Fix
    ↓
Retest
    ↓
Regression
```

---

## 8. Execution Evidence

For executable environments, evidence may include:

* Screenshots
* Screen recordings
* API request/response
* Database query results
* Application logs
* Transaction IDs
* Browser console information
* Relevant timestamps

Evidence should be attached or referenced when it helps reproduce or verify the result.

---

## 9. Environment Information

The following information should be recorded for every meaningful execution cycle:

| Field               | Example |
| ------------------- | ------- |
| Environment         | QA      |
| Application Version | v1.0.0  |
| Browser             | Chrome  |
| Browser Version     | TBD     |
| Operating System    | Windows |
| API Version         | TBD     |
| Database            | TBD     |
| Execution Date      | TBD     |
| Tester              | TBD     |

---

## 10. Current State

The current project is still in the **Test Design phase**.

No test case has been executed against an actual BlueBank application.

Therefore:

* Passed: 0
* Failed: 0
* Blocked: 0
* Not Executed: 61

No defect has been created based on execution yet.

---

## 11. Next Step

Once an executable BlueBank environment is available, the 61 test cases will be executed.

The execution process will produce:

1. Actual Results
2. Pass/Fail/Blocked status
3. Defect reports for failed tests
4. Retest candidates
5. Regression candidates
6. Execution summary
