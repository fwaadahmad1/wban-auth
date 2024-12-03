import json
from datetime import datetime

# Step 1: Simulate patient data
patient_data = {
    "id": "12345",
    "name": "John Doe",
    "heart_rate": 72,
    "blood_pressure": "120/80",
    "allergies": "None",
    "notes": "No pre-existing conditions",
}

# Step 2: Define roles and access policies
roles = {
    "doctor": ["view", "edit"],
    "nurse": ["view"],
    "receptionist": ["view_summary"],  # Can only see a summary
}


# Step 3: Emergency override function
def access_data(role, action, emergency=False):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if emergency:
        log_access(role, action, success=True, emergency=True)
        print("Emergency override! Full data access granted.")
        return json.dumps(patient_data, indent=4)

    if action in roles.get(role, []):
        log_access(role, action, success=True)
        if action == "view":
            return json.dumps(patient_data, indent=4)
        elif action == "view_summary":
            return json.dumps(
                {key: patient_data[key] for key in ["id", "name", "heart_rate"]},
                indent=4,
            )
    else:
        log_access(role, action, success=False)
        return "Access Denied"


# Step 4: Logging function
access_log = []


def log_access(role, action, success, emergency=False):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    access_log.append(
        {
            "time": current_time,
            "role": role,
            "action": action,
            "success": success,
            "emergency": emergency,
        }
    )


# Demonstration
print("Doctor's access to full data:")
print(access_data("doctor", "view"))

print("\nReceptionist's access to summary:")
print(access_data("receptionist", "view_summary"))

print("\nEmergency access by nurse:")
print(access_data("nurse", "view", emergency=True))

print("\nAccess Log:")
print(json.dumps(access_log, indent=4))
