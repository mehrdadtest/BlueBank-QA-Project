INSERT INTO users (email, password, status)
VALUES
('john.doe@bluebank.test', 'BlueBank@123', 'Active'),
('jane.smith@bluebank.test', 'BlueBank@123', 'Active'),
('alex.brown@bluebank.test', 'BlueBank@123', 'Active'),
('noactive@bluebank.test', 'BlueBank@123', 'Active');


INSERT INTO accounts
(account_number, user_id, status, balance)
VALUES
('10001234', 1, 'Active', 1500.00),
('10005678', 1, 'Closed', 500.00),
('10009012', 1, 'Blocked', 750.00),
('20004567', 2, 'Active', 3000.00),
('30007890', 3, 'Active', 2000.00),
('30001111', 3, 'Closed', 2000.00),
('30002222', 3, 'Blocked', 2000.00),
('40000000', 4, 'Closed', 0.00);
