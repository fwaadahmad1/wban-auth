from gateway import Gateway
from utils import decrypt, hash_data


class Sensor:
    """Processes forwarded messages and establishes session keys."""

    def __init__(self, sensor_id, mobile_id, gateway: Gateway):
        self.key = hash_data(sensor_id)
        self.sensor_id = sensor_id
        self.mobile_id = mobile_id
        ku_snj, kgw_snj = gateway.register_sensor_node(sensor_id, mobile_id)
        self.ku_snj = ku_snj
        self.kgw_snj = kgw_snj
        print(f"Sensor Node Registered: KU_SNJ={ku_snj}, KGW_SNJ={kgw_snj}")

    def process_request(self, encrypted_data: bytes, session_components: str):
        decrypted_data = decrypt(self.key, encrypted_data)
        session_key = hash_data(session_components)
        session_key_hex = session_key.hex()
        return f"Sensor Processed. Session Key: {session_key_hex}"

    def authenticate(self, expert_id, mobile_id, nonce, gateway: Gateway):
        return gateway.authenticate_sensor(self.sensor_id, expert_id, mobile_id, nonce)
