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

### Authentication Process

1. **Medical Expert**: Sends an encrypted request to the Mobile Device.
2. **Mobile Device**: Forwards the encrypted request to the Sensor.
3. **Sensor**: Processes the request and generates a session key.
4. **Gateway**: Authenticates the Medical Expert, Mobile Device, and Sensor, and returns the session key.

The `main.py` script demonstrates this process step-by-step, printing the results at each stage.