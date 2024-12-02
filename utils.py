
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def hash_data(data: str) -> bytes:
    """Generate a SHA-256 hash and return the first 16 bytes (128 bits)."""
    return hashlib.sha256(data.encode()).digest()[:16]

def encrypt(key: bytes, plaintext: str) -> bytes:
    """Encrypt plaintext using AES-128."""
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    return encryptor.update(padded_data) + encryptor.finalize()

def decrypt(key: bytes, ciphertext: bytes) -> str:
    """Decrypt ciphertext using AES-128."""
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    return unpadder.update(padded_data).decode()