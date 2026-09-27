# BlueBank QA Project --- Acceptance Criteria

## Money Transfer

  -----------------------------------------------------------------------
  ID                                  Acceptance Criteria
  ----------------------------------- -----------------------------------
  AC-01                               An authenticated customer sees
                                      their active accounts as eligible
                                      source accounts.

  AC-02                               The customer can select a valid
                                      source account.

  AC-03                               A valid destination account is
                                      accepted.

  AC-04                               An invalid, nonexistent, closed, or
                                      blocked destination account is
                                      rejected and the transfer is
                                      prevented.

  AC-05                               A source account and destination
                                      account that are identical are
                                      rejected.

  AC-06                               The transfer amount must be
                                      numeric, at least 0.01, at most
                                      10,000, and contain no more than
                                      two decimal places.

  AC-07                               An amount greater than Available
                                      Balance is rejected.

  AC-08                               An amount equal to Available
                                      Balance is allowed and leaves the
                                      source balance at zero.

  AC-09                               Before final submission, the
                                      confirmation screen displays Source
                                      Account, Destination Account, and
                                      Amount, and allows the customer to
                                      confirm or cancel.

  AC-10                               A valid confirmed transfer succeeds
                                      and generates a unique Transaction
                                      ID.

  AC-11                               For a successful internal transfer,
                                      the source balance decreases and
                                      the destination balance increases
                                      by the transfer amount.

  AC-12                               A successful transfer appears in
                                      Transaction History with
                                      Transaction ID, Date/Time, Source
                                      Account, Destination Account,
                                      Amount, and Status.

  AC-13                               Resubmitting the same transfer does
                                      not create a duplicate transaction.
  -----------------------------------------------------------------------

## Authentication

  -----------------------------------------------------------------------
  ID                                  Acceptance Criteria
  ----------------------------------- -----------------------------------
  AC-AUTH-01                          Valid registered credentials allow
                                      the customer to log in
                                      successfully.

  AC-AUTH-02                          An incorrect password prevents
                                      login.

  AC-AUTH-03                          An unregistered email prevents
                                      login.

  AC-AUTH-04                          Empty Email or Password fields
                                      cannot be submitted.

  AC-AUTH-05                          An unauthenticated user or a user
                                      with an expired session cannot
                                      access Transfer functionality.
  -----------------------------------------------------------------------

## Traceability

The following traceability chain will be completed in later project
phases:

**Business Rule → Acceptance Criteria → Test Condition → Test Scenario →
Test Case → Execution → Bug → Retest → Regression**
