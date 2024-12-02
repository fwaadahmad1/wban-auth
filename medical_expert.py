from gateway import Gateway, encrypt
import random


class MedicalExpert:
    """Initiates the authentication and data request process."""

    def __init__(self, expert_id, password, gateway: Gateway):
        self.expert_id = expert_id
        self.password = password
        epw, rd, c, ni, kj, kl = gateway.register_medical_expert(expert_id, password)

        self.epw = epw
        self.rd = rd
        self.c = c
        self.ni = ni
        self.kj = kj
        self.kl = kl

        print(
            f"Medical Expert Registered: EPW={epw}, RD={rd}, C={c}, NI={ni}, KJ={kj}, KL={kl}"
        )

    def request_data(self, mobile_id, sensor_id):
        nonce = str(random.randint(1000, 9999))
        message = f"{self.expert_id}|{mobile_id}|{sensor_id}|{nonce}"
        encrypted_request = encrypt(
            self.key, message
        )  # This is already returning bytes
        return encrypted_request, nonce
