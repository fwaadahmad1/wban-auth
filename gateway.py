import random
from utils import hash_data, encrypt, decrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

class Gateway:
    """Central authority for registration and key management."""
    def __init__(self):
        self.mobile_keys = {}
        self.sensor_keys = {}
        self.expert_keys = {}
        self.gateway_id = "gateway_001"
        self.secret_key = hash_data("secret_key")

    def register_medical_expert(self, expert_id, password):
        rd = random.randint(1000, 9999)
        epw = hash_data(password + str(rd))
        kj = hash_data(expert_id + "_kj")
        kl = hash_data(expert_id + "_kl")
        c = encrypt(kj, f"{expert_id}|{self.gateway_id}")
        ni = hash_data(expert_id + epw.decode('latin1') + self.secret_key.decode('latin1'))
        self.expert_keys[expert_id] = (c, ni, kj, kl)
        return epw, rd, c, ni, kj, kl

    def register_mobile_device(self, mobile_id):
        kgw_u = hash_data(mobile_id + self.gateway_id)
        self.mobile_keys[mobile_id] = kgw_u
        return kgw_u

    def register_sensor_node(self, sensor_id, mobile_id):
        ku_snj = hash_data(mobile_id + sensor_id)
        kgw_snj = hash_data(self.gateway_id + sensor_id)
        self.sensor_keys[sensor_id] = (ku_snj, kgw_snj)
        return ku_snj, kgw_snj

    def authenticate(self, expert_id, password, mobile_id, sensor_id, nonce):
        # Step 1
        rd = self.expert_keys[expert_id][1]
        ni = hash_data(expert_id + hash_data(password + str(rd)).decode('latin1') + self.secret_key.decode('latin1'))
        if ni != self.expert_keys[expert_id][1]:
            return "Authentication failed", None
        h_mid = hash_data(expert_id)
        cid_i = encrypt(self.expert_keys[expert_id][3], f"{h_mid.decode('latin1')}|{mobile_id}|{sensor_id}|{nonce}")
        # Step 2
        kj, kl = self.expert_keys[expert_id][2], self.expert_keys[expert_id][3]
        decrypted_cid_i = decrypt(kl, cid_i)
        h_mid_received, m, mobile_id_received, sensor_id_received, t1 = decrypted_cid_i.split('|')
        if h_mid_received != h_mid.decode('latin1') or mobile_id_received != mobile_id or sensor_id_received != sensor_id:
            return "Authentication failed", None
        x = encrypt(self.sensor_keys[sensor_id][1], f"{expert_id}|{m}")
        vi = encrypt(self.mobile_keys[mobile_id], f"{mobile_id}|{sensor_id}|{x.decode('latin1')}|{nonce}")
        # Step 3
        decrypted_vi = decrypt(self.mobile_keys[mobile_id], vi)
        mobile_id_received, sensor_id_received, x_received, t3 = decrypted_vi.split('|')
        if mobile_id_received != mobile_id or sensor_id_received != sensor_id:
            return "Authentication failed", None
        vi = encrypt(self.sensor_keys[sensor_id][0], f"{x_received}|{mobile_id}|{sensor_id}|{nonce}")
        # Step 4
        decrypted_vi = decrypt(self.sensor_keys[sensor_id][0], vi)
        x_received, mobile_id_received, sensor_id_received, t5 = decrypted_vi.split('|')
        decrypted_x = decrypt(self.sensor_keys[sensor_id][1], x_received)
        expert_id_received, m_received = decrypted_x.split('|')
        if expert_id_received != expert_id:
            return "Authentication failed", None
        kssk = hash_data(f"{expert_id}|{sensor_id}|{m_received}")
        l = encrypt(kssk, f"{sensor_id}|{expert_id}|{nonce}")
        return l, kssk

    def update_password(self, expert_id, old_password, new_password):
        rd = self.expert_keys[expert_id][1]
        ni = hash_data(expert_id + hash_data(old_password + str(rd)).decode('latin1') + self.secret_key.decode('latin1'))
        if ni != self.expert_keys[expert_id][1]:
            return "Password update failed"
        rnew_d = random.randint(1000, 9999)
        epw_new = hash_data(new_password + str(rnew_d))
        nnew_i = hash_data(expert_id + epw_new.decode('latin1') + self.secret_key.decode('latin1'))
        self.expert_keys[expert_id] = (self.expert_keys[expert_id][0], rnew_d, self.expert_keys[expert_id][2], self.expert_keys[expert_id][3], nnew_i)
        return epw_new, rnew_d, nnew_i