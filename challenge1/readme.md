### Experiment: **Context-Aware Access Control in Emergency Scenarios**

#### Goal:
- Implement a fine-grained access control system.
- Allow emergency overrides to demonstrate flexibility in patient data access during critical situations.

---

### Implementation Plan:
1. **Simulate Patient Data**:
   - Generate mock patient health data.
2. **Define Access Policies**:
   - Assign access roles with specific privileges.
3. **Context-Aware Override**:
   - Allow data access overrides in emergencies with logging for accountability.
4. **Access Log**:
   - Record all access attempts for monitoring.

---

### Output Example

```plaintext
Doctor's access to full data:
{
    "id": "12345",
    "name": "John Doe",
    "heart_rate": 72,
    "blood_pressure": "120/80",
    "allergies": "None",
    "notes": "No pre-existing conditions"
}

Receptionist's access to summary:
{
    "id": "12345",
    "name": "John Doe",
    "heart_rate": 72
}

Emergency access by nurse:
Emergency override! Full data access granted.
{
    "id": "12345",
    "name": "John Doe",
    "heart_rate": 72,
    "blood_pressure": "120/80",
    "allergies": "None",
    "notes": "No pre-existing conditions"
}

Access Log:
[
    {
        "time": "2024-12-03 14:45:30",
        "role": "doctor",
        "action": "view",
        "success": true,
        "emergency": false
    },
    {
        "time": "2024-12-03 14:45:32",
        "role": "receptionist",
        "action": "view_summary",
        "success": true,
        "emergency": false
    },
    {
        "time": "2024-12-03 14:45:34",
        "role": "nurse",
        "action": "view",
        "success": true,
        "emergency": true
    }
]
```

---

### Explanation for Presentation:
1. **Context-Aware Access**:
   - Role-based privileges control access to patient data.
   - Summary or full data view based on role permissions.
2. **Emergency Overrides**:
   - Immediate access granted during emergencies, reflecting real-world healthcare needs.
3. **Accountability**:
   - All access attempts are logged for security and compliance tracking.