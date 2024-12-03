from gateway import Gateway
from utils import encrypt, hash_data


class MobileDevice:
    """Handles forwarding encrypted messages between Gateway and Sensors."""

    def __init__(self, mobile_id, gateway: Gateway):
        self.key = hash_data(mobile_id)
        self.mobile_id = mobile_id
        kgw_u = gateway.register_mobile_device(mobile_id)
        self.kgw_u = kgw_u
        print(f"Mobile Device Registered: KGW_U={kgw_u}")

    def forward_to_sensor(self, encrypted_data: bytes, sensor_key: bytes) -> bytes:
        """Forward the encrypted message to the sensor."""
        return encrypt(
            sensor_key, encrypted_data.decode("latin1")
        )  # 'latin1' ensures that bytes are handled as is

    def authenticate(self, expert_id, password, sensor_id, nonce, gateway: Gateway):
        return gateway.authenticate_mobile(
            self.mobile_id, expert_id, password, sensor_id, nonce
        )
