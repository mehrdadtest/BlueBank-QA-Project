### 6. Boundary Values

#### Transfer Amount

| Category           |    Value | Expected |
| ------------------ | -------: | -------- |
| Below minimum      |     0.00 | Invalid  |
| Minimum            |     0.01 | Valid    |
| Just above minimum |     0.02 | Valid    |
| Normal             |   500.00 | Valid    |
| Near maximum       |  9999.99 | Valid    |
| Maximum            | 10000.00 | Valid    |
| Above maximum      | 10000.01 | Invalid  |

#### Decimal Precision

|   Value | Expected |
| ------: | -------- |
|     100 | Valid    |
|  100.50 | Valid    |
|  100.55 | Valid    |
| 100.555 | Invalid  |

#### Balance

| Available Balance | Transfer Amount | Expected |
| ----------------: | --------------: | -------- |
|           1000.00 |          999.99 | Valid    |
|           1000.00 |         1000.00 | Valid    |
|           1000.00 |         1000.01 | Invalid  |
|              0.00 |            0.01 | Invalid  |