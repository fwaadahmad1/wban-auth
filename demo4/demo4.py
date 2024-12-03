import random
import time
from datetime import datetime

# Step 1: Define sensor thresholds
THRESHOLDS = {
    "heart_rate": (60, 100),  # Normal range
    "blood_pressure": (90, 140),  # Normal systolic BP range
    "temperature": (36.1, 37.2),  # Normal body temperature in Celsius
}


# Step 2: Simulate sensor data
def generate_sensor_data():
    return {
        "heart_rate": random.randint(50, 120),  # Simulate variability
        "blood_pressure": random.randint(80, 160),
        "temperature": round(random.uniform(35.0, 38.0), 1),
    }


# Step 3: Anomaly detection function
def detect_anomalies(data):
    anomalies = {}
    for key, value in data.items():
        min_val, max_val = THRESHOLDS[key]
        if not (min_val <= value <= max_val):
            anomalies[key] = value
    return anomalies


# Step 4: Log anomalies
anomaly_log = []


def log_anomaly(sensor_id, anomalies):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    anomaly_log.append(
        {"sensor_id": sensor_id, "anomalies": anomalies, "timestamp": timestamp}
    )
    print(f"Anomaly detected on Sensor {sensor_id} at {timestamp}: {anomalies}")


# Step 5: Real-time simulation
def simulate_wban():
    for i in range(10):  # Simulate 10 readings
        sensor_id = f"Sensor-{random.randint(1, 3)}"  # Simulate multiple sensors
        data = generate_sensor_data()
        anomalies = detect_anomalies(data)
        print(f"{sensor_id} data: {data}")
        if anomalies:
            log_anomaly(sensor_id, anomalies)
        time.sleep(1)  # Simulate real-time delay


# Run simulation
simulate_wban()

# Display anomaly log
print("\nAnomaly Log:")
for log in anomaly_log:
    print(log)
