# BlueBank QA Project — User Stories

## US-01 — Money Transfer

**As an authenticated BlueBank customer,**  
I want to transfer money from an account I own to an eligible destination account,  
so that I can send money securely and have the transfer recorded correctly.

### Scope

This user story covers the backend behavior required to process an internal money transfer, including:

- Validating the transfer request.
- Verifying source-account ownership and account status.
- Verifying destination-account existence and status.
- Checking the transfer amount and available balance.
- Preventing duplicate transfer requests.
- Updating source and destination account balances.
- Creating transfer and transaction records.
- Preserving data consistency when a transfer fails.
- Preventing concurrent transfers from overdrawing the source account.

### Backend API Coverage

| API | Purpose |
|---|---|
| `POST /api/v1/transfers` | Submit and process a money transfer. |

### Acceptance Criteria

- **AC-TRANSFER-01:** The system rejects transfer requests that fail request-schema validation.
- **AC-TRANSFER-02:** Only authenticated users can access protected transfer functionality.
- **AC-TRANSFER-03:** The source account must exist, be active, and belong to the authenticated user.
- **AC-TRANSFER-04:** The destination account must exist and be active.
- **AC-TRANSFER-05:** The source and destination accounts must be different.
- **AC-TRANSFER-06:** The transfer amount must be valid and must not exceed the available source-account balance.
- **AC-TRANSFER-07:** A duplicate request reference is rejected without creating a duplicate successful transfer.
- **AC-TRANSFER-08:** A successful transfer decreases the source balance and increases the destination balance by the transfer amount.
- **AC-TRANSFER-09:** A successful transfer creates the corresponding transfer and transaction records.
- **AC-TRANSFER-10:** If transfer processing fails, partial database changes must not remain committed.
- **AC-TRANSFER-11:** Concurrent transfers must not allow the source account to be overdrawn.

## US-02 — Login

**As a BlueBank customer,**  
I want to log in using valid credentials,  
so that I can securely access my accounts and authorized banking functionality.

### Scope

This user story covers authentication through the login API, including credential validation and rejection of invalid authentication attempts.

### Backend API Coverage

| API | Purpose |
|---|---|
| `POST /api/v1/auth/login` | Authenticate a customer using the submitted credentials. |

### Acceptance Criteria

- **AC-LOGIN-01:** Valid credentials for an eligible user result in successful authentication.
- **AC-LOGIN-02:** Invalid credentials are rejected.
- **AC-LOGIN-03:** A nonexistent user cannot authenticate successfully.
- **AC-LOGIN-04:** An inactive user cannot authenticate successfully.
- **AC-LOGIN-05:** Protected API requests require valid authentication.
- **AC-LOGIN-06:** Missing, invalid, tampered, or expired authentication tokens are rejected where applicable to protected APIs.

## US-03 — Transaction History

**As an authenticated BlueBank customer,**  
I want to view the transaction history associated with my accounts,  
so that I can review my financial activity and verify completed transfers.

### Scope

This user story covers retrieving transaction history through the backend API and enforcing the applicable access-control rules.

### Backend API Coverage

| API | Purpose |
|---|---|
| `GET /api/v1/transactions` | Retrieve transaction history accessible to the authenticated user. |

### Acceptance Criteria

- **AC-HISTORY-01:** An authenticated user can retrieve transaction history they are authorized to access.
- **AC-HISTORY-02:** Transactions associated with the user's source or destination accounts are included according to the implemented query rules.
- **AC-HISTORY-03:** A user cannot retrieve transaction history belonging exclusively to unrelated users.
- **AC-HISTORY-04:** Requests without valid authentication are rejected.
- **AC-HISTORY-05:** A successfully completed transfer is recorded and can be retrieved through the transaction-history API.

## US-04 — Bank Account Inquiry

**As an authenticated BlueBank customer,**  
I want to view the list of my bank accounts and retrieve the details of an account I own,  
so that I can review my account information and identify the accounts available for banking operations.

### Scope

This user story covers retrieving account information through the backend APIs and enforcing account ownership and authorization rules.

### Backend API Coverage

| API | Purpose |
|---|---|
| `GET /api/v1/accounts` | Retrieve the authenticated user's accessible accounts. |
| `GET /api/v1/accounts/{account_number}` | Retrieve account details, subject to authorization rules. |

### Acceptance Criteria

- **AC-ACCOUNT-01:** An authenticated user can retrieve their accessible bank accounts.
- **AC-ACCOUNT-02:** A user can retrieve the details of an account they are authorized to access.
- **AC-ACCOUNT-03:** A user cannot retrieve another user's account details without authorization.
- **AC-ACCOUNT-04:** Requests without valid authentication are rejected.

## Relationship Between User Stories

The four user stories represent separate customer-facing capabilities:

1. **Login:** Establishes the customer's authenticated session.
2. **Bank Account Inquiry:** Allows the customer to retrieve authorized account information.
3. **Money Transfer:** Processes transfers subject to business rules, authorization, and data-consistency requirements.
4. **Transaction History:** Allows the customer to review authorized transaction records.

Login is a separate user story because authentication is an independent capability with its own validation and security requirements. Account inquiry and transaction history are also separate because retrieving account information and reviewing financial activity are distinct customer needs.

## Scope Notes

- These user stories describe backend API behavior, not a graphical user interface.
- A transfer form, account-selection screen, confirmation page, and UI navigation are not implied by this document.
- Validation, authorization, duplicate-request protection, rollback, and concurrency controls are supporting rules and implementation behaviors; they do not each require a separate customer-facing user story.
- Acceptance criteria must be verified against the current implementation and automated tests before being reported as fully covered.
- The health-check endpoint is an operational capability and is not included as a customer-facing user story.
