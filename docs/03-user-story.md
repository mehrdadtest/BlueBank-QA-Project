# BlueBank QA Project --- User Stories

## US-01 --- Money Transfer

> As an authenticated BlueBank customer, I want to transfer money from
> one of my accounts to an eligible destination account, so that I can
> send money securely.

## US-02 --- Login

> As a BlueBank customer, I want to log in with valid credentials so
> that I can securely access my accounts and transfer functionality.

## Why Login Has a Separate User Story

Login is part of the Phase 1 scope, but the Money Transfer user story
should not implicitly contain all authentication requirements.
Therefore, Login is documented as a separate user story.

## Business Flow

1.  Customer logs in.
2.  Customer opens Transfer.
3.  Customer selects a source account.
4.  Customer enters a destination account.
5.  Customer enters the transfer amount.
6.  The system displays the transfer confirmation.
7.  Customer confirms the transfer.
8.  The system creates the transfer.
9.  Account balances are updated.
10. The transaction appears in Transaction History.
