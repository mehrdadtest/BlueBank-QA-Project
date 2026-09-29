# BlueBank Traceability Matrix

## 1. Purpose

This document defines the traceability relationships between BlueBank business rules, acceptance criteria, test conditions, test scenarios, and test cases.

The purpose of the Traceability Matrix is to ensure that:

* Business rules are covered by testable requirements.
* Acceptance criteria are covered by test conditions.
* Test conditions are represented by appropriate test scenarios.
* Test scenarios are covered by test cases.
* Test cases can later be traced to test execution results and defects.

The main traceability chain in this project is:

**Business Rule → Acceptance Criteria → Test Condition → Test Scenario → Test Case**

After test execution, the chain will be extended to:

**Test Case → Execution Result → Bug → Retest → Regression**

---

## 2. Traceability Legend

| ID Type | Description         |
| ------- | ------------------- |
| BR      | Business Rule       |
| AC      | Acceptance Criteria |
| TCND    | Test Condition      |
| TS      | Test Scenario       |
| TC      | Test Case           |

---

## 3. Business Rule to Acceptance Criteria

| Business Rule | Business Rule Description                                            | Acceptance Criteria |
| ------------- | -------------------------------------------------------------------- | ------------------- |
| BR-01         | Minimum transfer amount is $0.01                                     | AC-06               |
| BR-02         | Maximum transfer amount is $10,000                                   | AC-06               |
| BR-03         | Transfer amount must not exceed Available Balance                    | AC-07               |
| BR-04         | Transfer equal to Available Balance is allowed                       | AC-08               |
| BR-05         | Source account must belong to the authenticated user                 | AC-01, AC-02        |
| BR-06         | Destination account must exist                                       | AC-03, AC-04        |
| BR-07         | Destination account must be Active                                   | AC-04               |
| BR-08         | Source and destination accounts must be different                    | AC-05               |
| BR-09         | Amount supports up to two decimal places                             | AC-06               |
| BR-10         | Amount must be numeric                                               | AC-06               |
| BR-11         | Negative amounts are invalid                                         | AC-06               |
| BR-12         | Empty amount is invalid                                              | AC-06               |
| BR-13         | Duplicate transfer submission must not create duplicate transactions | AC-13               |
| BR-14         | Successful transfers appear in Transaction History                   | AC-12               |
| BR-15         | Unauthenticated users cannot access transfer functionality           | AC-AUTH-05          |
| BR-16         | Account numbers are 8 digits                                         | AC-03, AC-04        |
| BR-17         | Successful transfer creates a unique Transaction ID                  | AC-10               |
| BR-18         | Successful internal transfer increases destination balance           | AC-11               |
| BR-19         | Successful transfer decreases source balance                         | AC-11               |

---

## 4. Acceptance Criteria to Test Conditions

### Authentication and Access

| Acceptance Criteria | Test Conditions              |
| ------------------- | ---------------------------- |
| AC-AUTH-01          | TCND-001                     |
| AC-AUTH-02          | TCND-002                     |
| AC-AUTH-03          | TCND-003                     |
| AC-AUTH-04          | TCND-004, TCND-005           |
| AC-AUTH-05          | TCND-006, TCND-007, TCND-008 |

### Money Transfer

| Acceptance Criteria | Test Conditions                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| AC-01               | TCND-009, TCND-010, TCND-011, TCND-013                                                                                                     |
| AC-02               | TCND-012                                                                                                                                   |
| AC-03               | TCND-015                                                                                                                                   |
| AC-04               | TCND-016, TCND-017, TCND-018, TCND-020, TCND-021                                                                                           |
| AC-05               | TCND-019                                                                                                                                   |
| AC-06               | TCND-022, TCND-023, TCND-024, TCND-025, TCND-026, TCND-027, TCND-028, TCND-029, TCND-030, TCND-031, TCND-032, TCND-033, TCND-034, TCND-035 |
| AC-07               | TCND-036, TCND-038, TCND-039, TCND-040                                                                                                     |
| AC-08               | TCND-037                                                                                                                                   |
| AC-09               | TCND-041, TCND-043, TCND-044, TCND-045                                                                                                     |
| AC-10               | TCND-042, TCND-046, TCND-047                                                                                                               |
| AC-11               | TCND-048, TCND-049                                                                                                                         |
| AC-12               | TCND-050, TCND-051, TCND-052                                                                                                               |
| AC-13               | TCND-053, TCND-054, TCND-055, TCND-056                                                                                                     |

---

## 5. Test Condition to Test Scenario

| Test Condition | Test Scenario |
| -------------- | ------------- |
| TCND-001       | TS-001        |
| TCND-002       | TS-002        |
| TCND-003       | TS-003        |
| TCND-004       | TS-004        |
| TCND-005       | TS-005        |
| TCND-006       | TS-006        |
| TCND-007       | TS-007        |
| TCND-008       | TS-008        |
| TCND-009       | TS-009        |
| TCND-010       | TS-010        |
| TCND-011       | TS-011        |
| TCND-012       | TS-012        |
| TCND-013       | TS-013        |
| TCND-014       | TS-014        |
| TCND-015       | TS-015        |
| TCND-016       | TS-016        |
| TCND-017       | TS-017        |
| TCND-018       | TS-018        |
| TCND-019       | TS-019        |
| TCND-020       | TS-020        |
| TCND-021       | TS-021        |
| TCND-022       | TS-022        |
| TCND-023       | TS-023        |
| TCND-024       | TS-024        |
| TCND-025       | TS-025        |
| TCND-026       | TS-026        |
| TCND-027       | TS-027        |
| TCND-028       | TS-028        |
| TCND-029       | TS-029        |
| TCND-030       | TS-030        |
| TCND-031       | TS-031        |
| TCND-032       | TS-032        |
| TCND-033       | TS-033        |
| TCND-034       | TS-034        |
| TCND-035       | TS-035        |
| TCND-036       | TS-036        |
| TCND-037       | TS-037        |
| TCND-038       | TS-038        |
| TCND-039       | TS-039        |
| TCND-040       | TS-040        |
| TCND-041       | TS-041        |
| TCND-042       | TS-042        |
| TCND-043       | TS-043        |
| TCND-044       | TS-044        |
| TCND-045       | TS-045        |
| TCND-046       | TS-046        |
| TCND-047       | TS-047        |
| TCND-048       | TS-048        |
| TCND-049       | TS-049        |
| TCND-050       | TS-050        |
| TCND-051       | TS-051        |
| TCND-052       | TS-052        |
| TCND-053       | TS-053        |
| TCND-054       | TS-054        |
| TCND-055       | TS-055        |
| TCND-056       | TS-056        |

---

## 6. Test Scenario to Test Case

| Test Scenario | Test Case | Priority |
| ------------- | --------- | -------- |
| TS-001        | TC-001    | High     |
| TS-002        | TC-002    | High     |
| TS-003        | TC-003    | High     |
| TS-004        | TC-004    | Medium   |
| TS-005        | TC-005    | Medium   |
| TS-006        | TC-006    | High     |
| TS-007        | TC-007    | High     |
| TS-008        | TC-008    | Medium   |
| TS-009        | TC-009    | High     |
| TS-010        | TC-010    | High     |
| TS-011        | TC-011    | High     |
| TS-012        | TC-012    | High     |
| TS-013        | TC-013    | Medium   |
| TS-014        | TC-014    | High     |
| TS-015        | TC-015    | High     |
| TS-016        | TC-016    | High     |
| TS-017        | TC-017    | High     |
| TS-018        | TC-018    | High     |
| TS-019        | TC-019    | High     |
| TS-020        | TC-020    | Medium   |
| TS-021        | TC-021    | High     |
| TS-022        | TC-022    | High     |
| TS-023        | TC-023    | High     |
| TS-024        | TC-024    | Medium   |
| TS-025        | TC-025    | High     |
| TS-026        | TC-026    | Medium   |
| TS-027        | TC-027    | Medium   |
| TS-028        | TC-028    | High     |
| TS-029        | TC-029    | High     |
| TS-030        | TC-030    | High     |
| TS-031        | TC-031    | High     |
| TS-032        | TC-032    | Medium   |
| TS-033        | TC-033    | High     |
| TS-034        | TC-034    | Medium   |
| TS-035        | TC-035    | High     |
| TS-036        | TC-036    | High     |
| TS-037        | TC-037    | High     |
| TS-038        | TC-038    | High     |
| TS-039        | TC-039    | High     |
| TS-040        | TC-040    | Medium   |
| TS-041        | TC-041    | High     |
| TS-042        | TC-042    | Critical |
| TS-043        | TC-043    | High     |
| TS-044        | TC-044    | Medium   |
| TS-045        | TC-045    | High     |
| TS-046        | TC-046    | Critical |
| TS-047        | TC-047    | High     |
| TS-048        | TC-048    | Critical |
| TS-049        | TC-049    | Critical |
| TS-050        | TC-050    | High     |
| TS-051        | TC-051    | High     |
| TS-052        | TC-052    | High     |
| TS-053        | TC-053    | Critical |
| TS-054        | TC-054    | Critical |
| TS-055        | TC-055    | Critical |
| TS-056        | TC-056    | Critical |

---

## 7. End-to-End Test Coverage

The final five scenarios validate important business flows across multiple conditions.

| Scenario | Test Case | Main Coverage                     |
| -------- | --------- | --------------------------------- |
| TS-057   | TC-057    | Successful end-to-end transfer    |
| TS-058   | TC-058    | Insufficient balance end-to-end   |
| TS-059   | TC-059    | Invalid destination end-to-end    |
| TS-060   | TC-060    | Full available balance end-to-end |
| TS-061   | TC-061    | Duplicate transfer prevention     |

These scenarios intentionally cross multiple requirements and test conditions.

### TC-057 — Successful End-to-End Transfer

Covers:

* AC-AUTH-01
* AC-01
* AC-02
* AC-03
* AC-06
* AC-09
* AC-10
* AC-11
* AC-12

### TC-058 — Insufficient Balance

Covers:

* AC-AUTH-01
* AC-01
* AC-02
* AC-03
* AC-07

### TC-059 — Invalid Destination

Covers:

* AC-AUTH-01
* AC-01
* AC-02
* AC-04

### TC-060 — Full Available Balance

Covers:

* AC-08
* AC-10
* AC-11
* AC-12

### TC-061 — Duplicate Transfer Prevention

Covers:

* AC-10
* AC-11
* AC-12
* AC-13

---

## 8. Test Design Technique Coverage

The project also uses specific Test Design Techniques to ensure meaningful coverage with a manageable number of test cases.

| Technique                           | Covered Test Cases                             | Main Purpose                                   |
| ----------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| Equivalence Partitioning            | TC-022, TC-025, TC-031, TC-033, TC-035         | Valid and invalid input classes                |
| Boundary Value Analysis             | TC-022, TC-023, TC-024, TC-028, TC-029, TC-030 | Lower and upper boundaries                     |
| Decision Table                      | TC-036, TC-037, TC-038, TC-039, TC-040         | Combination of transfer and balance conditions |
| Experience-based / Negative Testing | TC-053, TC-054, TC-055, TC-056                 | Duplicate submission and retry behavior        |

---

## 9. Coverage Summary

At the design stage, the project contains:

| Artifact            | Count |
| ------------------- | ----: |
| Business Rules      |    19 |
| Acceptance Criteria |    18 |
| Test Conditions     |    56 |
| Test Scenarios      |    61 |
| Test Cases          |    61 |

The current Test Cases have not yet been executed.

Therefore:

* **Execution Status:** Not Executed
* **Automation Status:** Not Automated
* **Defects:** Not yet identified
* **Retesting:** Not started
* **Regression Testing:** Not started

These values will be updated after the Execution phase.

---

## 10. Traceability Gaps and Assumptions

During traceability review, several items require clarification before or during execution.

### Source Account Status

AC-01 states that active accounts belonging to the authenticated customer should be available as source accounts.

However, the current Business Rules do not contain an explicit rule stating:

> The source account must be Active.

This behavior is currently derived from AC-01.

Before finalizing the requirements baseline, this can either be:

* added as an explicit Business Rule, or
* documented as an assumption of AC-01.

### User With No Active Account

TC-013 verifies the behavior of a customer who has no active account.

This behavior is derived from AC-01 and should be confirmed as an explicit expected behavior if the project specification is later formalized.

### Duplicate Transfer Prevention

TC-053 through TC-056 verify duplicate submission and retry behavior.

The current project assumes that repeated submission of the same logical transfer must not create duplicate transactions.

During API testing, this assumption can be further defined through an idempotency or request-reference mechanism.

---

## 11. Future Traceability

After Test Execution, this matrix will be extended with execution and defect information.

The final traceability chain will be:

**Business Rule → Acceptance Criteria → Test Condition → Test Scenario → Test Case → Test Execution → Bug → Retest → Regression**

This allows the project to demonstrate not only that tests were designed, but also how requirements were validated and how defects were managed throughout the testing lifecycle.
