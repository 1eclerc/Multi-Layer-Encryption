# 🔐 Multi-Layer Text Encryption in Python

This Python project applies **four layers of encryption** to any input text:

1. **ROT13 Cipher** – Rotates each alphabet letter by 13 places.
2. **XOR Cipher** – Applies XOR encryption with a single ASCII character key.
3. **Reverse Cipher** – Reverses the XOR-encrypted string.
4. **Base64 Encoding** – Encodes the final result to Base64 for safe transfer.

---

## ✨ Example

**Input:**
- Plaintext: `cryptography is fun!`
- XOR Key: `X`

**Output:**
```
eTkwK3g+Lng0LTs2PSw6Pzs0PSg=
```

---

## 📁 Files

```
├── multi_layer_encryption.py  # The main encryption script
└── README.md                  # This file
```

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Run the script:

```bash
python multi_layer_encryption.py
```

3. Enter your plaintext and XOR key when prompted.

---

## ⚠️ Note

- The XOR key must be a **single ASCII character**.
- This script performs **one-way encryption**. Reversing the process would require a custom decryption function.

---

## 🧠 Why These Layers?

Each encryption layer adds complexity:
- **ROT13** is a basic substitution cipher.
- **XOR** adds a layer of binary obfuscation.
- **Reversing** adds confusion for pattern detection.
- **Base64** ensures the result is readable and safely transmittable.

---

## 📄 License

This project is provided for educational and experimental purposes.
