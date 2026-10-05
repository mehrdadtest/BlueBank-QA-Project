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
