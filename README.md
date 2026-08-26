# 🔐 JCrypt — Python Message Encryption & Decryption Tool

**JCrypt** is a lightweight Python-based encryption and decryption tool designed to securely encrypt messages and decrypt them when needed.

The project provides a simple command-line interface (CLI) for protecting sensitive messages using modern cryptographic techniques.

> ⚠️ **Educational & Defensive Security Project**
> JCrypt is intended for learning cryptography, secure programming, and data protection concepts. Do not use it to protect highly sensitive production data without a proper security review.

---

## ✨ Features

* 🔒 Encrypt messages
* 🔓 Decrypt encrypted messages
* 🔑 Password-based encryption
* 🧂 Secure salt generation
* 🎲 Random initialization values/nonces where supported
* 🖥️ Simple command-line interface
* 📋 Encrypt text directly from the terminal
* 📄 Optional file encryption/decryption
* 🐍 Written completely in Python
* 📦 Easy to install and run
* 🛡️ Designed with secure cryptographic practices in mind

---

## 🏗️ Project Architecture

```text
                 ┌──────────────────┐
                 │      JCrypt      │
                 └────────┬─────────┘
                          │
                 ┌────────▼─────────┐
                 │   CLI Interface  │
                 └────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
        ┌─────▼─────┐           ┌─────▼─────┐
        │  Encrypt  │           │  Decrypt  │
        └─────┬─────┘           └─────┬─────┘
              │                       │
        ┌─────▼───────────────────────▼─────┐
        │       Cryptographic Layer         │
        │                                    │
        │  Key Derivation + Encryption      │
        └────────────────┬───────────────────┘
                         │
                  ┌──────▼──────┐
                  │ Encrypted   │
                  │   Output    │
                  └─────────────┘
```

---

## 📁 Project Structure

```text
JCrypt/
│
├── jcrypt/
│   ├── __init__.py
│   ├── cli.py
│   ├── crypto.py
│   ├── key_manager.py
│   └── utils.py
│
├── tests/
│   ├── test_crypto.py
│   └── test_key_manager.py
│
├── examples/
│   └── example.py
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Requirements

* Python 3.10+
* pip
* Recommended: virtual environment

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/JCrypt.git
```

Move into the project directory:

```bash
cd JCrypt
```

Create a virtual environment:

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Encryption

JCrypt allows users to encrypt a plaintext message using a password.

Example:

```bash
python -m jcrypt encrypt
```

Example workflow:

```text
Enter message: Hello, this is a secret message.

Enter password: ********

Encrypted message:
<encrypted-data>
```

The encrypted output should be treated as ciphertext and stored securely.

---

# 🔓 Decryption

To decrypt a message:

```bash
python -m jcrypt decrypt
```

Example:

```text
Enter encrypted message:
<encrypted-data>

Enter password: ********

Decrypted message:
Hello, this is a secret message.
```

If the password is incorrect or the ciphertext has been modified, JCrypt should reject the decryption instead of returning corrupted plaintext.

---

# 🧪 Example

### Original message

```text
Meet me at 10 AM.
```

### Encrypt

```text
Plaintext
    │
    ▼
Password
    │
    ▼
Key Derivation
    │
    ▼
Authenticated Encryption
    │
    ▼
Ciphertext
```

Example output:

```text
JCrypt> encrypt

Message:
Meet me at 10 AM.

Encrypted:
<encrypted-data>
```

### Decrypt

```text
Ciphertext
    │
    ▼
Password
    │
    ▼
Key Derivation
    │
    ▼
Authenticated Decryption
    │
    ▼
Original Message
```

Output:

```text
JCrypt> decrypt

Decrypted message:
Meet me at 10 AM.
```

---

# 🔑 Cryptographic Design

JCrypt should **not implement cryptographic algorithms from scratch**.

Instead, it should rely on well-tested cryptographic libraries.

Recommended design:

```text
User Password
      │
      ▼
   KDF
      │
      ▼
Derived Encryption Key
      │
      ▼
Authenticated Encryption
      │
      ▼
Ciphertext + Required Metadata
```

For password-based encryption, a modern password-based key derivation function such as **Argon2id** or **scrypt** can be used.

For authenticated encryption, algorithms such as:

* AES-GCM
* ChaCha20-Poly1305

are appropriate choices when implemented through a reputable cryptographic library.

---

# 🧂 Password Security

Passwords should **never be used directly as encryption keys**.

JCrypt should derive an encryption key from the password using a password-based KDF.

Conceptually:

```text
Password
   +
Random Salt
   │
   ▼
Password KDF
   │
   ▼
Encryption Key
```

A unique random salt should be generated for each encrypted message.

The salt does not need to be secret and can be stored alongside the ciphertext.

---

# 🛡️ Authentication

Encryption alone does not necessarily provide integrity.

JCrypt should use **authenticated encryption** so that modifications to ciphertext can be detected.

For example:

```text
Plaintext
   │
   ▼
Authenticated Encryption
   │
   ├── Ciphertext
   │
   └── Authentication Tag
```

During decryption:

```text
Ciphertext
     │
     ▼
Authentication Check
     │
   ┌─┴─┐
   │   │
Valid Invalid
 │      │
 ▼      ▼
Decrypt  Reject
```

This prevents JCrypt from silently accepting altered ciphertext.

---

# 📦 Encrypted Data Format

A versioned encrypted format can be used so future versions of JCrypt can remain compatible.

Example:

```text
JC1:<salt>:<nonce>:<ciphertext>:<tag>
```

Where:

| Field        | Purpose               |
| ------------ | --------------------- |
| `JC1`        | JCrypt format/version |
| `salt`       | KDF salt              |
| `nonce`      | Encryption nonce      |
| `ciphertext` | Encrypted data        |
| `tag`        | Authentication data   |

The exact encoding and format should be documented by the implementation.

---

# 🧪 Testing

Run the test suite with:

```bash
python -m pytest
```

Example tests should include:

* Encryption/decryption round trip
* Empty messages
* Unicode messages
* Long messages
* Incorrect password
* Modified ciphertext
* Invalid input
* Random salt generation
* Random nonce generation

Example:

```text
Original
   ↓
Encrypt
   ↓
Decrypt
   ↓
Original
```

Expected result:

```text
PASS
```

---

# 🔍 Security Considerations

JCrypt follows several important security principles:

### Never hard-code encryption keys

❌ Do not do:

```python
KEY = "my-secret-key"
```

### Never store plaintext passwords

Passwords should only be used as input to the password-based KDF.

### Never reuse nonces incorrectly

Encryption modes such as AES-GCM require correct nonce management.

### Use secure randomness

Use Python's cryptographically secure randomness facilities or the cryptographic library's secure random generation.

### Do not create custom cryptographic algorithms

JCrypt should use established cryptographic primitives instead of attempting to invent its own encryption algorithm.

---

# 🖥️ Planned CLI

The project may eventually support commands such as:

```bash
jcrypt encrypt
```

```bash
jcrypt decrypt
```

```bash
jcrypt encrypt --message "Hello World"
```

```bash
jcrypt decrypt --data "<encrypted-data>"
```

File operations:

```bash
jcrypt encrypt-file secret.txt
```

```bash
jcrypt decrypt-file secret.enc
```

---

# 🗺️ Roadmap

## Version 1.0

* [ ] Basic CLI
* [ ] Message encryption
* [ ] Message decryption
* [ ] Password-based key derivation
* [ ] Random salt generation
* [ ] Authenticated encryption
* [ ] Error handling
* [ ] Unit tests

## Version 1.1

* [ ] File encryption
* [ ] File decryption
* [ ] Better CLI arguments
* [ ] Configuration support
* [ ] Improved error messages

## Version 2.0

* [ ] Secure key-file support
* [ ] Multiple encryption profiles
* [ ] JSON encrypted container format
* [ ] Performance improvements
* [ ] Comprehensive security testing
* [ ] Documentation website

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Add tests.
5. Run the test suite.

```bash
pytest
```

6. Commit your changes.

```bash
git commit -m "Add new encryption feature"
```

7. Push the branch.

```bash
git push origin feature/new-feature
```

8. Open a Pull Request.

---

# 🐛 Reporting Security Issues

If you discover a security vulnerability in JCrypt, please do not immediately publish exploit details in a public issue.

Instead, contact the project maintainer privately so the vulnerability can be investigated and fixed responsibly.

---

# 📜 License

This project is released under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

# 👨‍💻 Author

**Your Name**

Cybersecurity Enthusiast | Python Developer | Security Researcher

GitHub: `https://github.com/YOUR_USERNAME`

---

# ⭐ Support

If you find JCrypt useful for learning about Python and cryptography, consider giving the repository a ⭐.

---

## ⚠️ Disclaimer

JCrypt is an educational and defensive security project.

The authors are not responsible for loss of data, compromised credentials, improper cryptographic implementation, or any other damage resulting from the use or misuse of this software.

For production systems handling highly sensitive information, use established, professionally reviewed cryptographic solutions and conduct an appropriate security assessment.
