# BlueBank QA Project --- Business Rules

  -----------------------------------------------------------------------
  ID                                  Business Rule
  ----------------------------------- -----------------------------------
  BR-01                               The minimum transfer amount is
                                      \$0.01.

  BR-02                               The maximum transfer amount is
                                      \$10,000.

  BR-03                               The transfer amount must not exceed
                                      Available Balance.

  BR-04                               A transfer equal to Available
                                      Balance is allowed.

  BR-05                               The source account must belong to
                                      the authenticated user.

  BR-06                               The destination account must exist.

  BR-07                               The destination account must be
                                      Active.

  BR-08                               The source and destination accounts
                                      must be different.

  BR-09                               The transfer amount supports a
                                      maximum of two decimal places.

  BR-10                               The transfer amount must be
                                      numeric.

  BR-11                               Negative amounts are invalid.

  BR-12                               An empty amount is invalid.

  BR-13                               Duplicate submission of the same
                                      transfer must not create a
                                      duplicate transaction.

  BR-14                               Successful transfers must appear in
                                      Transaction History.

  BR-15                               Unauthenticated users must not
                                      access transfer functionality.

  BR-16                               Account numbers use the assumed
                                      8-digit format.

  BR-17                               A successful transfer must generate
                                      a unique Transaction ID.

  BR-18                               A successful internal transfer
                                      increases the destination balance
                                      by the transfer amount.

  BR-19                               A successful transfer decreases the
                                      source balance by the transfer
                                      amount.
  -----------------------------------------------------------------------

## Amount Examples

  Input      Expected Result
  ---------- -----------------
  0          Invalid
  -10        Invalid
  0.01       Valid
  0.02       Valid
  100.50     Valid
  100.555    Invalid
  10000      Valid
  10000.01   Invalid

## Boundary Values

### Lower Boundary

-   `0` → Invalid
-   `0.01` → Valid
-   `0.02` → Valid

### Upper Boundary

-   `9999.99` → Valid
-   `10000` → Valid
-   `10000.01` → Invalid
