from cryptography.fernet import Fernet
import random


# Simulate WBAN Data
def generate_mock_data():
    data = {
        "id": "12345",
        "name": "John Doe",
        "heart_rate": random.randint(60, 100),
        "blood_pressure": f"{random.randint(90, 120)}/{random.randint(60, 80)}",
    }
    return data


# Encrypt Data
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(str(data).encode())
    return encrypted_data


# Decrypt Data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return eval(decrypted_data)


# Implement RBAC
roles = {"doctor": ["read"], "nurse": ["read"], "receptionist": []}


def has_access(role, action):
    return action in roles.get(role, [])


# Access Simulation
def access_data(role, encrypted_data, key):
    if has_access(role, "read"):
        return decrypt_data(encrypted_data, key)
    else:
        return "Access Denied"


# Main Execution
if __name__ == "__main__":
    key = Fernet.generate_key()
    data = generate_mock_data()
    encrypted_data = encrypt_data(data, key)

    print("Encrypted Data:", encrypted_data)

    roles_to_test = ["doctor", "nurse", "receptionist"]
    for role in roles_to_test:
        print(f"\nRole: {role}")
        decrypted_data = access_data(role, encrypted_data, key)
        print("Decrypted Data:", decrypted_data)
