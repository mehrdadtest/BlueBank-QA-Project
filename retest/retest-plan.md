# BlueBank Retest Plan

## 1. Purpose

Retesting is performed to verify that a reported defect has been fixed correctly.

In the BlueBank project, a failed Test Case becomes a candidate for Retesting when:

1. The defect has been investigated.
2. The development team has implemented a fix.
3. The defect has been marked as ready for retest.
4. The required test environment and test data are available.

Retesting focuses specifically on the previously failed behavior.

---

## 2. Retesting vs Regression Testing

Retesting and Regression Testing have different purposes.

| Retesting                                       | Regression Testing                               |
| ----------------------------------------------- | ------------------------------------------------ |
| Verifies that a specific defect has been fixed  | Checks whether changes caused problems elsewhere |
| Usually focuses on the failed Test Case         | Covers related or affected areas                 |
| Requires a known defect                         | Can be performed after any significant change    |
| Uses the original failure as the starting point | Uses a selected regression test suite            |

Example:

If `TC-030` fails because the application incorrectly accepts `$10,000.01`, Retesting should execute `TC-030` again after the fix.

Regression testing may additionally include other amount-validation and transfer tests.

---

## 3. Retest Entry Criteria

A defect can enter Retesting when:

* A fix has been delivered.
* The relevant application build is available.
* The original Test Case is available.
* Required test data is available.
* The defect has sufficient reproduction information.
* The environment is stable enough for testing.

---

## 4. Retest Process

```text id="rj8g6v"
Bug Report
    ↓
Fix Implemented
    ↓
Ready for Retest
    ↓
Execute Original Test Case
    ↓
Compare Actual Result with Expected Result
    ↓
┌───────────────┬────────────────┐
│ Pass          │ Fail           │
│ ↓             │ ↓              │
│ Close/Verify  │ Reopen Bug     │
└───────────────┴────────────────┘
```

---

## 5. Retest Result

The following statuses are used:

| Result       | Description                                                                     |
| ------------ | ------------------------------------------------------------------------------- |
| Pass         | The original defect is no longer reproducible and expected behavior is observed |
| Fail         | The defect still occurs                                                         |
| Blocked      | Retest cannot be completed because of an environment or dependency issue        |
| Not Executed | Retest has not yet been performed                                               |

---

## 6. Retest Record

| Bug ID | Original Test Case | Build | Retest Result | Date | Tester | Notes                    |
| ------ | ------------------ | ----- | ------------- | ---- | ------ | ------------------------ |
| TBD    | TBD                | TBD   | Not Executed  | TBD  | TBD    | No defects available yet |

---

## 7. Retest Example

The following is an example of the process and is **not an actual BlueBank defect**.

Suppose execution identifies a failure in:

`TC-030 — Amount Above Maximum`

Expected:

> A transfer amount of `$10,000.01` is rejected.

Actual:

> The application allows the transfer.

The test fails and a Bug Report is created.

After the fix is delivered, the same Test Case is executed again.

### If the Retest passes

```text id="n8t8g6"
TC-030
   ↓
Fail
   ↓
BUG-XXX
   ↓
Fix
   ↓
Retest TC-030
   ↓
Pass
```

The defect can then move toward closure, subject to the project's defect workflow.

### If the Retest fails

```text id="rjv9aq"
TC-030
   ↓
Fail
   ↓
BUG-XXX
   ↓
Fix
   ↓
Retest TC-030
   ↓
Fail
   ↓
Reopen BUG-XXX
```

---

## 8. Evidence

Retest evidence should be collected when appropriate.

Examples:

* Screenshot of the corrected behavior
* API response
* Database result
* Transaction ID
* Application log
* Relevant timestamp

The evidence should demonstrate that the original failure has been addressed.

---

## 9. Traceability

Retesting extends the project's traceability chain:

```text id="8s3pqa"
Business Rule
      ↓
Acceptance Criteria
      ↓
Test Condition
      ↓
Test Scenario
      ↓
Test Case
      ↓
Execution
      ↓
Failure
      ↓
Bug
      ↓
Fix
      ↓
Retest
```

---

## 10. Current Project Status

No Retest has been performed yet.

Reason:

* Test Execution has not started.
* No real Test Case has failed.
* No actual Bug Report has been created.
* No fix is available for verification.

Current Retest status:

**Not Started**
