### Experiment: **Real-Time Anomaly Detection in WBAN Health Data**

#### Goal:

- Simulate health data streams from multiple sensors.
- Use a threshold-based anomaly detection system to flag abnormal readings.
- Log anomalies with timestamps and sensor details for further action.

---

### Implementation Plan:

1. **Simulate Real-Time Sensor Data**:
   - Generate random health data (e.g., heart rate, blood pressure) for multiple sensors.
2. **Define Anomaly Thresholds**:
   - Set acceptable ranges for health metrics.
3. **Detect and Log Anomalies**:
   - Flag and log abnormal readings in real-time.

---

### Output Example

```plaintext
Sensor-2 data: {'heart_rate': 85, 'blood_pressure': 135, 'temperature': 36.5}
Sensor-1 data: {'heart_rate': 55, 'blood_pressure': 150, 'temperature': 37.5}
Anomaly detected on Sensor-1 at 2024-12-03 15:45:30: {'heart_rate': 55, 'blood_pressure': 150, 'temperature': 37.5}
Sensor-3 data: {'heart_rate': 70, 'blood_pressure': 110, 'temperature': 35.2}
Anomaly detected on Sensor-3 at 2024-12-03 15:45:31: {'temperature': 35.2}

Anomaly Log:
{'sensor_id': 'Sensor-1', 'anomalies': {'heart_rate': 55, 'blood_pressure': 150, 'temperature': 37.5}, 'timestamp': '2024-12-03 15:45:30'}
{'sensor_id': 'Sensor-3', 'anomalies': {'temperature': 35.2}, 'timestamp': '2024-12-03 15:45:31'}
```

---

### Explanation for Presentation:

1. **Real-Time Monitoring**:
   - Simulates continuous data from wearable sensors.
2. **Threshold-Based Anomaly Detection**:
   - Flags health metrics outside normal ranges, demonstrating WBAN monitoring capabilities.
3. **Relevance**:
   - Highlights how WBANs can enable early detection of health issues in real time.
4. **Extendable**:
   - Could integrate machine learning for more sophisticated anomaly detection.
