CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Active',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_user_status
        CHECK (status IN ('Active', 'Inactive'))
);


CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    account_number CHAR(8) NOT NULL UNIQUE,
    user_id INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL,
    balance NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_account_user
        FOREIGN KEY (user_id)
        REFERENCES users(id),

    CONSTRAINT chk_account_status
        CHECK (status IN ('Active', 'Closed', 'Blocked')),

    CONSTRAINT chk_account_balance
        CHECK (balance >= 0),

    CONSTRAINT chk_account_number
        CHECK (account_number ~ '^[0-9]{8}$')
);



CREATE TABLE transfers (
    id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(50) NOT NULL UNIQUE,
    source_account_id INTEGER NOT NULL,
    destination_account_id INTEGER NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    request_reference VARCHAR(100) NOT NULL UNIQUE,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_transfer_source
        FOREIGN KEY (source_account_id)
        REFERENCES accounts(id),

    CONSTRAINT fk_transfer_destination
        FOREIGN KEY (destination_account_id)
        REFERENCES accounts(id),

    CONSTRAINT chk_transfer_amount
        CHECK (amount >= 0.01 AND amount <= 10000),

    CONSTRAINT chk_transfer_status
        CHECK (status IN ('Pending', 'Successful', 'Failed', 'Cancelled')),

    CONSTRAINT chk_different_accounts
        CHECK (source_account_id <> destination_account_id)
);




CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(50) NOT NULL UNIQUE,
    transfer_id INTEGER NOT NULL,
    source_account_id INTEGER NOT NULL,
    destination_account_id INTEGER NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_transaction_transfer
        FOREIGN KEY (transfer_id)
        REFERENCES transfers(id),

    CONSTRAINT fk_transaction_source
        FOREIGN KEY (source_account_id)
        REFERENCES accounts(id),

    CONSTRAINT fk_transaction_destination
        FOREIGN KEY (destination_account_id)
        REFERENCES accounts(id),

    CONSTRAINT chk_transaction_status
        CHECK (status IN ('Successful', 'Failed', 'Cancelled'))
);








