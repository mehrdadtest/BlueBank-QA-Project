# BlueBank Bug Reports

## 1. Purpose

This directory contains defect reports identified during BlueBank test execution.

Each Bug Report should provide enough information for the development team to:

* Understand the problem
* Reproduce the issue
* Identify the affected functionality
* Assess its severity and priority
* Track the defect through its lifecycle
* Verify the fix during Retesting

---

## 2. Bug Report Naming Convention

Bug Reports use the following format:

```text
BUG-001.md
BUG-002.md
BUG-003.md
```

The ID must be unique within the project.

---

## 3. Bug Lifecycle

A defect follows this general lifecycle:

```text
New
 ↓
Triaged
 ↓
Assigned
 ↓
In Progress
 ↓
Fixed
 ↓
Ready for Retest
 ↓
Retest
 ↓
Closed
```

A defect may also move to other states when appropriate:

```text
Rejected
Duplicate
Won't Fix
Cannot Reproduce
Deferred
Reopened
```

---

## 4. Severity

Severity describes the technical or functional impact of the defect.

| Severity | Description                                                                                                      |
| -------- | ---------------------------------------------------------------------------------------------------------------- |
| Critical | Causes a critical business failure, data corruption, security issue, or prevents a core function from being used |
| High     | Significantly affects an important feature or business flow                                                      |
| Medium   | Affects functionality but a reasonable workaround may exist                                                      |
| Low      | Minor functional, usability, or cosmetic issue                                                                   |

Severity describes **impact**, not how quickly the issue must be fixed.

---

## 5. Priority

Priority describes the order in which the defect should be addressed from a project perspective.

| Priority | Description                                            |
| -------- | ------------------------------------------------------ |
| Critical | Requires immediate attention                           |
| High     | Should be addressed before release when practical      |
| Medium   | Should be addressed during normal development          |
| Low      | Can be addressed when higher-priority work is complete |

Severity and Priority are independent attributes.

For example, a visually minor defect may have higher priority because it affects an important release requirement.

---

## 6. Minimum Bug Report Information

Every defect should contain at least:

* Bug ID
* Title
* Related Test Case
* Related Requirement
* Environment
* Preconditions
* Steps to Reproduce
* Expected Result
* Actual Result
* Severity
* Priority
* Status
* Evidence

---

## 7. Traceability

Every execution-related defect should be linked back to the test that identified it.

Example:

```text
BR-03
  ↓
AC-07
  ↓
TCND-036
  ↓
TS-036
  ↓
TC-036
  ↓
Execution: Fail
  ↓
BUG-001
```

This provides end-to-end traceability from the original business rule to the defect.

---

## 8. Retesting

After a defect is marked as fixed, the related test case must be executed again.

The Retest should verify that:

1. The reported problem has been fixed.
2. The expected behavior now occurs.
3. The fix did not introduce an immediate issue in the affected flow.

A successful Retest does not automatically mean the defect is closed if additional regression testing is required.

---

## 9. Reopened Defects

If the defect still occurs during Retest:

```text
Ready for Retest
       ↓
Retest
       ↓
Fail
       ↓
Reopened
```

The new Actual Result and evidence should be added to the defect history.

---

## 10. Evidence

Evidence should be included when it helps reproduce or understand the defect.

Possible evidence includes:

* Screenshots
* Screen recordings
* API request and response
* Database query results
* Application logs
* Transaction ID
* Timestamp
* Browser console output

Sensitive credentials or real customer information must not be included in screenshots or logs.

---

## 11. Current Status

No actual defects have been identified yet because BlueBank has not entered executable Test Execution.

Current defect count:

**0**

The first Bug Report will be created only after an actual test execution produces a failure.
