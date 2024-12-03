### Experiment: **Simulating Secure Data Transmission in a WBAN**

#### Goal:
- Encrypt patient data using a symmetric key encryption technique.
- Control access based on predefined roles using a basic Role-Based Access Control (RBAC) model.

#### Implementation Plan:
1. **Simulate WBAN Data**:
   - Generate mock patient health data (e.g., heart rate, blood pressure).
2. **Encrypt Data**:
   - Use the `cryptography` library for symmetric encryption (e.g., AES).
3. **Implement RBAC**:
   - Define roles (e.g., doctor, nurse) and grant access rights.
4. **Access Simulation**:
   - Decrypt the data only if the user's role matches the access policy.

---

### Explanation:
1. **Secure Storage**: Patient data is encrypted using AES, ensuring confidentiality.
2. **Role-Based Access Control**: Only authorized roles can view the decrypted data.
3. **Relevance**: Demonstrates key principles from the paper—security, privacy, and controlled access in WBANs.