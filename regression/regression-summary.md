# BlueBank Regression Summary

## 1. Overview

This document records the results of Regression Testing performed after application changes, defect fixes, or other changes that may affect existing functionality.

---

## 2. Regression Suite

| Suite                   | Test Cases | Status       |
| ----------------------- | ---------: | ------------ |
| Core Regression         |         20 | Not Executed |
| Full Regression         |         61 | Not Executed |
| Impact-Based Regression |   Variable | Not Executed |

---

## 3. Current Execution Results

| Metric                          | Count |
| ------------------------------- | ----: |
| Total Regression Tests Executed |     0 |
| Passed                          |     0 |
| Failed                          |     0 |
| Blocked                         |     0 |
| Not Executed                    |    61 |
| New Defects                     |     0 |
| Reopened Defects                |     0 |

---

## 4. Regression Execution Record

| Cycle   | Change / Fix | Suite | Executed | Passed | Failed | Blocked | Status      |
| ------- | ------------ | ----- | -------: | -----: | -----: | ------: | ----------- |
| REG-001 | TBD          | TBD   |        0 |      0 |      0 |       0 | Not Started |

---

## 5. Regression Defects

Any defect discovered during Regression Testing should be linked to:

* The Regression Test Case
* The original change or fix
* The affected requirement
* The related Bug Report, if applicable

Example relationship:

```text
BUG-001 Fix
     ↓
Regression
     ↓
TC-048
     ↓
Fail
     ↓
BUG-002
```

This allows defects introduced by a fix to be distinguished from the original defect.

---

## 6. Regression Metrics

Once execution begins, the following metrics will be calculated.

### Regression Pass Rate

```text id="p0azmt"
Passed Regression Tests
──────────────────────── × 100
Executed Regression Tests
```

### Regression Failure Rate

```text id="5qj1nb"
Failed Regression Tests
──────────────────────── × 100
Executed Regression Tests
```

---

## 7. Current Conclusion

The BlueBank project now has a defined Regression Testing strategy.

However, no Regression result is currently reported because:

* The application has not yet entered actual execution.
* No real defect has been fixed.
* No real change has been deployed.
* No Regression cycle has been performed.

The next phase of the project can therefore move from the testing lifecycle into **API Testing**, where the same requirements and test data will be validated at the API level.
