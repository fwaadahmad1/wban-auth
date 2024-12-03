import random
from gateway import Gateway
from mobile_device import MobileDevice
from sensor import Sensor
from medical_expert import MedicalExpert

if __name__ == "__main__":
    # Setup gateway and entities
    gateway = Gateway()
    mobile_id = "mobile_123"
    sensor_id = "sensor_456"
    expert_id = "expert_789"
    password = "secure_password"

    # Setup entities and register with the gateway
    mobile = MobileDevice(mobile_id, gateway)
    sensor = Sensor(sensor_id, mobile_id, gateway)
    expert = MedicalExpert(expert_id, password, gateway)

    nonce = str(random.randint(1000, 9999))

    # Authentication Phase
    print("\n=== Authentication Phase ===")
    l, kssk = expert.authenticate(mobile_id, sensor_id, nonce, gateway)
    if kssk is not None:
        print(f"Authentication Result: L={l}, KSSK={kssk}")
    else:
        print("Authentication failed")
