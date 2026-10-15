### 2. Credentials

#### 2.1 Valid Credentials

The following credentials are intended for testing successful authentication. Verify that both users exist in the test database and that their passwords are valid before executing the tests.

| User ID | Email | Password | Expected Result |
|---------|-------|----------|-----------------|
| USR-001 | `john.doe@bluebank.test` | `BlueBank@123` | Authentication successful |
| USR-002 | `jane.smith@bluebank.test` | `BlueBank@123` | Authentication successful |

#### 2.2 Negative Testing Data

The following data is intended for testing unsuccessful authentication and input validation.

| Test Scenario | Email | Password | Expected Result |
|---------------|-------|----------|-----------------|
| Unregistered email | `unknown@bluebank.test` | `BlueBank@123` | Authentication rejected |
| Incorrect password | `john.doe@bluebank.test` | `Wrong@123` | Authentication rejected |
| Empty email | `""` | `BlueBank@123` | Request rejected |
| Empty password | `john.doe@bluebank.test` | `""` | Request rejected |

**Notes:**
- Use these credentials only in the designated test environment.
- Confirm that the valid users and passwords exist in the test database before execution.
- An empty string (`""`) is different from an omitted field. Test these cases separately if both behaviors need to be verified.
- Authentication failures should not disclose whether an email address is registered.