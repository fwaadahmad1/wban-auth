# Data Security System

This project simulates a data security system involving a Gateway, Mobile Devices, Sensors, and Medical Experts. The system demonstrates registration, encryption, decryption, and authentication processes.

## Files

- `gateway.py`: Contains the `Gateway` class, which handles registration and authentication of devices and experts.
- `mobile_device.py`: Contains the `MobileDevice` class, which forwards encrypted messages between the Gateway and Sensors.
- `sensor.py`: Contains the `Sensor` class, which processes forwarded messages and establishes session keys.
- `medical_expert.py`: Contains the `MedicalExpert` class, which initiates the authentication and data request process.
- `utils.py`: Contains utility functions for hashing, encryption, and decryption.
- `main.py`: The main script to run the demo.

## How to Run the Demo

1. **Install Dependencies**: Ensure you have the required dependencies installed. You can install them using pip:
    ```sh
    pip install cryptography
    ```

2. **Run the Main Script**: Execute the `main.py` script to see the simulation of the registration and authentication process.
    ```sh
    python main.py
    ```

## Explanation

1. **Gateway**: The central authority responsible for registering devices and experts, and managing keys.
2. **MobileDevice**: Registers with the Gateway and forwards encrypted messages to Sensors.
3. **Sensor**: Registers with the Gateway, processes messages, and establishes session keys.
4. **MedicalExpert**: Registers with the Gateway and initiates data requests and authentication.
5. **Utils**: Provides utility functions for hashing, encryption, and decryption.

### Output Example

```plaintext
Mobile Device Registered: KGW_U=b'[\xb3\xb6\xd8mb\xaa\xa0\xae\xda\x88\xa7\xb7\xb8\x1by'
Sensor Node Registered: KU_SNJ=b'vRK\x1e\x9a+m\x80\x11\xd8\xfcS\xf9\xc0\xd7\xa0', KGW_SNJ=b"\x16Z\x05\xed\x1a\x8f\xe5\xd9\xbf\xdaM'\xc0\xd6\xa9\xed"        
Medical Expert Registered: EPW=b'\xfbQ\xf0;\x10\x16L<\x9b~\xf7yu\xab\xd8\xeb', RD=2508, C=b'ss\xaef\xaa{\xc9v\x8e,\xcav\xbeP\xb5\xcc\xbf&\xc5)B\x9a\x939Z4\x80]IW\xc6y', NI=b'\x05\xa2\x8a\xf7\xb5\xd5p.\xb0\xac<DZ\x05{i', KJ=b'|\xcc\xdd\xe9\xe6\xf3DY5\xcf.\xb1\xaa\xb3_\xc6', KL=b'y\xb1{(l\xaa\x17^\xaeyi\x8c9\xfd|\xb2'

=== Authentication Phase ===
Authentication Result: L=b'g\xa9M\x95TE\x17]\x8c<\xc8\x05-{oBKk\xa5\x16\x89B\xb1\x96oiI[\t\xbd\xe8\x12', KSSK=b"\xe4\x06d'\xc2\xdb/N\xcbJ5\xe6\xc0\r\x10v"
```

### Authentication Process

1. **Medical Expert**: Sends an encrypted request to the Mobile Device.
2. **Mobile Device**: Forwards the encrypted request to the Sensor.
3. **Sensor**: Processes the request and generates a session key.
4. **Gateway**: Authenticates the Medical Expert, Mobile Device, and Sensor, and returns the session key.

The `main.py` script demonstrates this process step-by-step, printing the results at each stage.