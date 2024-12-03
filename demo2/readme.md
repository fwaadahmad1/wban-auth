### Experiment: **Simulating Distributed Data Integrity in WBAN**

#### Goal:
- Use hashing to ensure data integrity during distributed storage.
- Detect any data tampering in a WBAN-like scenario where nodes store encrypted data.

---

### Output Example

```plaintext
node1 data integrity verified.
Data tampered on node2!
node3 data integrity verified.
```

---

### Implementation Plan:
1. **Simulate Distributed Nodes**:
   - Create multiple nodes (simulated with dictionaries) storing encrypted patient data.
2. **Add Integrity Check**:
   - Generate and store hash digests for each node's data.
3. **Tampering Simulation**:
   - Alter data on one of the nodes to simulate an attack.
4. **Integrity Verification**:
   - Use hash comparison to detect tampering.

### Explanation for Presentation:
1. **Distributed Storage**: Simulates how WBAN nodes store data independently.
2. **Hashing for Integrity**: Ensures data consistency using SHA-256 hashes.
3. **Tampering Detection**: Demonstrates the ability to detect unauthorized changes, highlighting the importance of integrity assurance in WBANs.