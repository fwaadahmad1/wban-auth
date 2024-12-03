import secrets
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Step 1: Generate parameters for Diffie-Hellman
parameters = dh.generate_parameters(generator=2, key_size=2048)


# Step 2: Simulate two WBAN nodes
def generate_private_key(parameters):
    return parameters.generate_private_key()


def generate_shared_key(private_key, peer_public_key):
    shared_key = private_key.exchange(peer_public_key)
    # Derive a usable key using HKDF
    derived_key = HKDF(
        algorithm=SHA256(), length=32, salt=None, info=b"secure communication"
    ).derive(shared_key)
    return derived_key


# Step 3: Encrypt and Decrypt messages
def encrypt_message(key, message):
    cipher = Cipher(algorithms.AES(key), modes.CFB8(b"1234567890123456"))
    encryptor = cipher.encryptor()
    return encryptor.update(message.encode())


def decrypt_message(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CFB8(b"1234567890123456"))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext).decode()


# Node A key generation
private_key_a = generate_private_key(parameters)
public_key_a = private_key_a.public_key()

# Node B key generation
private_key_b = generate_private_key(parameters)
public_key_b = private_key_b.public_key()

# Step 4: Derive shared keys
shared_key_a = generate_shared_key(private_key_a, public_key_b)
shared_key_b = generate_shared_key(private_key_b, public_key_a)

# Validate that the shared keys are identical
assert shared_key_a == shared_key_b
print("Shared key established successfully.")

# Step 5: Secure communication
message = "Patient Heart Rate: 72 bpm"
print("\nOriginal Message:", message)

# Encrypt at Node A
encrypted_message = encrypt_message(shared_key_a, message)
print("\nEncrypted Message:", encrypted_message)

# Decrypt at Node B
decrypted_message = decrypt_message(shared_key_b, encrypted_message)
print("\nDecrypted Message:", decrypted_message)
