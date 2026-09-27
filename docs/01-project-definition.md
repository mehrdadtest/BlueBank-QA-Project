# BlueBank QA Project --- Project Definition

## 1. Project Overview

BlueBank is a fictional digital banking platform that allows customers
to log in, view account information, transfer money, and view
transaction history.

The purpose of this project is to simulate a real-world software testing
project and create a practical QA portfolio suitable for GitHub.

## 2. Project Goals

-   Practice ISTQB CTFL concepts through hands-on work
-   Practice test analysis and test design
-   Create formal test cases and execute them
-   Report defects and perform retesting
-   Build a regression test set
-   Establish a foundation for API Testing, SQL, and Test Automation
-   Produce a case study suitable for GitHub and a software-testing blog

## 3. Roles

  Role       Scope
  ---------- --------------
  Customer   In Scope
  Admin      Out of Scope

## 4. Main Features

### Authentication

-   Login
-   Logout

### Dashboard

-   Account Summary

### Accounts

-   Account Details

### Money Transfer

-   Create Transfer
-   Transfer Confirmation
-   Transfer Status

### Transactions

-   Transaction History

## 5. Phase 1 Scope

### In Scope

-   Login
-   Money Transfer
-   Transfer Confirmation
-   Transfer Status
-   Transaction History

### Out of Scope

-   Registration
-   Password Recovery
-   Admin Panel
-   Card Management
-   Bill Payment
-   Loan Management
-   Notifications
-   Mobile Application
-   Performance Testing
-   Security Penetration Testing

## 6. Main Business Flow

Customer → Login → Dashboard → Select Source Account → Enter Destination
Account → Enter Amount → Review Transfer → Confirm Transfer → Transfer
Created → Transaction History Updated

## 7. Test Objectives

-   Verify successful and unsuccessful login
-   Verify access to protected functionality
-   Verify source account validation
-   Verify destination account validation
-   Verify transfer amount validation
-   Verify available balance rules
-   Verify transfer confirmation
-   Verify successful transfer processing
-   Verify balance updates
-   Verify transaction history
-   Verify duplicate transfer prevention

## 8. Project Assumptions

-   The currency used in this fictional project is USD.
-   Account numbers are assumed to contain 8 digits.
-   Transfer amounts support a maximum of two decimal places.
-   Internal BlueBank transfers increase the destination account
    balance.
-   A successful transfer generates a unique Transaction ID.
-   An expired session cannot access protected functionality.
-   Resubmitting the same transfer must not create a duplicate
    transaction.

> BlueBank is a fictional product created for educational and portfolio
> purposes.
