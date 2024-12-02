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

    # Authentication Simulation
    print("\n=== Authentication Simulation ===")

    # Step 1: Medical Expert sends request
    encrypted_request, nonce = expert.request_data(mobile_id, sensor_id)
    print(f"Medical Expert Request (Encrypted): {encrypted_request}")

    # Step 2: Mobile device forwards request
    forwarded_request = mobile.forward_to_sensor(encrypted_request, sensor.key)
    print(f"Forwarded Request (Encrypted): {forwarded_request}")

    # Step 3: Sensor processes request and generates session key
    session_key_components = f"{expert_id}|{sensor_id}|{nonce}"
    response = sensor.process_request(forwarded_request, session_key_components)
    print(f"Sensor Response: {response}")

    nonce = str(random.randint(1000, 9999))

    # Authentication Phase
    print("\n=== Authentication Phase ===")
    l, kssk = expert.authenticate(mobile_id, sensor_id, nonce, gateway)
    if kssk is not None:
        print(f"Authentication Result: L={l}, KSSK={kssk}")
    else:
        print("Authentication failed")
