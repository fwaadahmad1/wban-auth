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

### Output Example

```plaintext
Encrypted Data: b'gAAAAABnTr28ulnrIUgEva3DGD-GFRCCCYdJE_OO5dRJUgdCuT58XRnAnwIbIG4HIScemu_sb12o28dqmIk_Vv-K9xOzYOcAy4VkiWPtAqtyCSUiVLsWTCVQ83Vesuf3SS8hoX7P59o1L6Ik-xIfzzWlUt4Hri0xkIP030XS9i3k-GkxX5i8sDhqQk-KoJEtk7cBU8TjU8fL'

Role: doctor
Decrypted Data: {'id': '12345', 'name': 'John Doe', 'heart_rate': 78, 'blood_pressure': '101/62'}

Role: nurse
Decrypted Data: {'id': '12345', 'name': 'John Doe', 'heart_rate': 78, 'blood_pressure': '101/62'}

Role: receptionist
Decrypted Data: Access Denied
```

---

### Explanation:
1. **Secure Storage**: Patient data is encrypted using AES, ensuring confidentiality.
2. **Role-Based Access Control**: Only authorized roles can view the decrypted data.
3. **Relevance**: Demonstrates key principles from the paper—security, privacy, and controlled access in WBANs.