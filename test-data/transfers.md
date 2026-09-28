### 5. Transfer Data

داده‌های انتقال را نیز مرکزی می‌کنیم:

| Transfer ID | Source   | Destination |   Amount | Purpose                 |
| ----------- | -------- | ----------- | -------: | ----------------------- |
| TR-001      | 10001234 | 30007890    |   500.00 | Normal transfer         |
| TR-002      | 10001234 | 30007890    |   500.50 | Decimal amount          |
| TR-003      | 10001234 | 30007890    |     0.01 | Minimum boundary        |
| TR-004      | 10001234 | 30007890    |     0.02 | Just above minimum      |
| TR-005      | 10001234 | 30007890    |  9999.99 | Just below maximum      |
| TR-006      | 10001234 | 30007890    | 10000.00 | Maximum boundary        |
| TR-007      | 10001234 | 30007890    | 10000.01 | Above maximum           |
| TR-008      | 10001234 | 30007890    |  1000.00 | Equal to balance        |
| TR-009      | 10001234 | 30007890    |  1000.01 | Above balance           |
| TR-010      | 10001234 | 99999999    |   500.00 | Invalid destination     |
| TR-011      | 10001234 | 10001234    |   500.00 | Same source/destination |