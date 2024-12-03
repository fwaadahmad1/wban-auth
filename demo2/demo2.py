import hashlib
from cryptography.fernet import Fernet

# Step 1: Simulate distributed WBAN nodes
nodes = {}

# Generate symmetric encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Data to be stored on nodes
patient_data = {
    "node1": {"id": "12345", "heart_rate": 72},
    "node2": {"id": "12345", "blood_pressure": "120/80"},
    "node3": {"id": "12345", "temperature": 36.7},
}

# Step 2: Store encrypted data with hash for integrity
for node, data in patient_data.items():
    encrypted_data = cipher.encrypt(str(data).encode())
    data_hash = hashlib.sha256(encrypted_data).hexdigest()
    nodes[node] = {"encrypted_data": encrypted_data, "hash": data_hash}

# Step 3: Simulate tampering
# Tamper with node2 data
tampered_data = cipher.encrypt(
    str({"id": "12345", "blood_pressure": "150/90"}).encode()
)
nodes["node2"]["encrypted_data"] = tampered_data  # Tampered without updating the hash


# Step 4: Verify data integrity
def verify_integrity(nodes):
    for node, contents in nodes.items():
        encrypted_data = contents["encrypted_data"]
        stored_hash = contents["hash"]
        calculated_hash = hashlib.sha256(encrypted_data).hexdigest()

        if calculated_hash != stored_hash:
            print(f"Data tampered on {node}!")
        else:
            print(f"{node} data integrity verified.")


# Run verification
verify_integrity(nodes)
