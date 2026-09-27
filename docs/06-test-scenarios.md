# BlueBank QA Project --- Test Scenarios

## Authentication & Access

  ID       Scenario
  -------- --------------------------------------
  TS-001   Login with valid credentials
  TS-002   Login with wrong password
  TS-003   Login with unregistered email
  TS-004   Login with blank email
  TS-005   Login with blank password
  TS-006   Access Transfer without login
  TS-007   Access Transfer with expired session
  TS-008   Preserve valid session into Transfer

## Source Account

  ID       Scenario
  -------- -----------------------------------------------
  TS-009   Display active accounts belonging to the user
  TS-010   Exclude inactive/closed/blocked accounts
  TS-011   Exclude another user's account
  TS-012   Select a valid source account
  TS-013   User with no active account
  TS-014   Attempt unauthorized source account

## Destination Account

  ID       Scenario
  -------- ----------------------------------
  TS-015   Enter valid destination account
  TS-016   Enter nonexistent destination
  TS-017   Enter closed destination
  TS-018   Enter blocked destination
  TS-019   Use same source and destination
  TS-020   Leave destination empty
  TS-021   Enter invalid destination format

## Transfer Amount

  ID       Scenario
  -------- ----------------------------------------------
  TS-022   Amount below minimum: 0
  TS-023   Minimum amount: 0.01
  TS-024   Just above minimum: 0.02
  TS-025   Normal valid amount: 500
  TS-026   Valid decimal amount: 500.50
  TS-027   Valid amount with two decimal places: 999.99
  TS-028   Near maximum: 9999.99
  TS-029   Maximum amount: 10000
  TS-030   Above maximum: 10000.01
  TS-031   Negative amount
  TS-032   Blank amount
  TS-033   Nonnumeric amount
  TS-034   Illegal characters in amount
  TS-035   More than two decimal places

## Available Balance

  ID       Scenario
  -------- ------------------------------------------
  TS-036   Transfer less than available balance
  TS-037   Transfer equal to available balance
  TS-038   Transfer greater than available balance
  TS-039   Source balance is zero
  TS-040   Source balance is below minimum transfer

## Confirmation

  ID       Scenario
  -------- -----------------------------------
  TS-041   Verify confirmation data
  TS-042   Confirm valid transfer
  TS-043   Cancel before confirmation
  TS-044   Navigate back before confirmation
  TS-045   Change amount before confirmation

## Successful Transfer

  ID       Scenario
  -------- --------------------------------------------
  TS-046   Successful transfer
  TS-047   Unique Transaction ID generated
  TS-048   Source balance decreases correctly
  TS-049   Destination balance increases correctly
  TS-050   Transfer appears in Transaction History
  TS-051   Transaction History details match transfer
  TS-052   Transfer status is correct

## Duplicate Transfer

  ID       Scenario
  -------- -----------------------------------------------
  TS-053   Double-click Confirm
  TS-054   Resend the same transfer request
  TS-055   Retry after timeout
  TS-056   Verify only one transaction exists in history

## End-to-End

  ID       Scenario
  -------- ------------------------------------------
  TS-057   Successful end-to-end transfer
  TS-058   Insufficient balance end-to-end
  TS-059   Invalid destination end-to-end
  TS-060   Full available balance end-to-end
  TS-061   Duplicate transfer prevention end-to-end

## Baseline Count

**61 Test Scenarios**

The previous working list contained 62 scenarios. The duplicate
zero-amount scenario was removed during documentation cleanup, resulting
in a 61-scenario baseline.
