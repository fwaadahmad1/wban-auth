### Experiment: **Diffie-Hellman Key Exchange for Secure Communication in WBANs**

#### Goal:

- Implement the Diffie-Hellman key exchange algorithm to establish a shared secret key between two WBAN nodes.
- Demonstrate secure data encryption using the derived key.
- Highlight the importance of key exchange in secure communications.

---

### Implementation Plan:

1. **Simulate Two WBAN Nodes**:
   - Represent the nodes as entities exchanging public keys.
2. **Perform Key Exchange**:
   - Use the Diffie-Hellman algorithm to derive a shared secret key.
3. **Encrypt and Decrypt Messages**:
   - Encrypt health data using the shared key and decrypt it at the other node.
4. **Demonstrate Security**:
   - Show that without the shared key, an intercepted message cannot be decrypted.

---

### Output Example

```plaintext
Shared key established successfully.

Original Message: Patient Heart Rate: 72 bpm

Encrypted Message: b'\x8fG@\x9e...'

Decrypted Message: Patient Heart Rate: 72 bpm
```

---

### Explanation for Presentation:

1. **Diffie-Hellman Key Exchange**:
   - Demonstrates secure, dynamic key generation between WBAN nodes without pre-sharing keys.
2. **Encryption and Decryption**:
   - Protects sensitive health data during communication.
3. **Security Insight**:
   - Highlights how shared keys remain secret even if public keys are intercepted.
4. **Relevance**:
   - This addresses the challenge of secure communication in WBANs, as described in the paper.
