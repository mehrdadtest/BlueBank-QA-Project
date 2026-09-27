# BlueBank QA Project --- Test Analysis

## 1. Requirement Decomposition

Test analysis in this project follows the chain:

**Requirement / Business Rule → Acceptance Criteria → Test Condition →
Test Scenario → Test Case**

### Requirement / Business Rule

What must be true about the product?

### Acceptance Criteria

What conditions determine whether the requirement is accepted?

### Test Condition

What feature, rule, or situation needs to be tested?

### Test Scenario

What meaningful situation or flow should be tested?

### Test Case

Exactly how will the tester execute the test, using defined
Preconditions, Steps, Test Data, and Expected Results?

## 2. Test Conditions

### Authentication & Access

-   TCND-001 Valid Login
-   TCND-002 Wrong Password
-   TCND-003 Unregistered Email
-   TCND-004 Empty Email
-   TCND-005 Empty Password
-   TCND-006 Transfer Access Without Authentication
-   TCND-007 Transfer Access With Expired Session
-   TCND-008 Valid Session Into Transfer

### Source Account

-   TCND-009 Active User Accounts
-   TCND-010 Inactive/Closed/Blocked Accounts
-   TCND-011 Other User Account
-   TCND-012 Valid Source Selection
-   TCND-013 No Active Account
-   TCND-014 Unauthorized Source Account

### Destination Account

-   TCND-015 Valid Destination
-   TCND-016 Nonexistent Destination
-   TCND-017 Closed Destination
-   TCND-018 Blocked Destination
-   TCND-019 Same Source and Destination
-   TCND-020 Empty Destination
-   TCND-021 Invalid Destination Format

### Transfer Amount

-   TCND-022 Below Minimum
-   TCND-023 Minimum
-   TCND-024 Just Above Minimum
-   TCND-025 Normal Valid Amount
-   TCND-026 Valid Decimal
-   TCND-027 Two Decimal Places
-   TCND-028 Near Maximum
-   TCND-029 Maximum
-   TCND-030 Above Maximum
-   TCND-031 Negative
-   TCND-032 Empty
-   TCND-033 Nonnumeric
-   TCND-034 Illegal Characters
-   TCND-035 More Than Two Decimal Places

### Available Balance

-   TCND-036 Amount Below Balance
-   TCND-037 Amount Equal to Balance
-   TCND-038 Amount Above Balance
-   TCND-039 Zero Balance
-   TCND-040 Balance Below Minimum

### Confirmation

-   TCND-041 Confirmation Data
-   TCND-042 Confirm Transfer
-   TCND-043 Cancel
-   TCND-044 Navigate Back
-   TCND-045 Change Amount Before Confirmation

### Successful Transfer

-   TCND-046 Successful Transfer
-   TCND-047 Unique Transaction ID
-   TCND-048 Source Balance Update
-   TCND-049 Destination Balance Update
-   TCND-050 Transaction History Creation
-   TCND-051 Transaction History Accuracy
-   TCND-052 Transfer Status

### Duplicate Submission

-   TCND-053 Double-click Confirm
-   TCND-054 Resend Same Request
-   TCND-055 Retry After Timeout
-   TCND-056 Duplicate History Prevention

## 3. Test Design Techniques

### Equivalence Partitioning

For the transfer amount:

-   Less than 0.01 → Invalid
-   0.01 through 10,000 → Valid
-   Greater than 10,000 → Invalid

### Boundary Value Analysis

Lower boundary:

`0` / `0.01` / `0.02`

Upper boundary:

`9999.99` / `10000` / `10000.01`

### Decision Table

  ---------------------------------------------------------------------------
  Authenticated   Source Valid   Destination    Amount Valid   Expected
                                 Valid                         
  --------------- -------------- -------------- -------------- --------------
  No              \-             \-             \-             Reject

  Yes             No             \-             \-             Reject

  Yes             Yes            No             \-             Reject

  Yes             Yes            Yes            No             Reject

  Yes             Yes            Yes            Yes            Continue to
                                                               Confirmation
  ---------------------------------------------------------------------------

## 4. Analysis Decisions

The original working list contained two scenarios covering `Amount = 0`.
This duplicate coverage was removed from the final baseline so that each
formal test condition has clear and meaningful coverage.

Session expiry, account-number format, and
retry-after-timeout/idempotency behavior are explicit project
assumptions. This prevents expected behavior from being based only on
tester assumptions.
