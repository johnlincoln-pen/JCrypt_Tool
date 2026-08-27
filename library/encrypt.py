from cryptography.fernet import Fernet
import base64


# ============================================================
# 1. FERNET ENCRYPTION
# ============================================================

def fernet_encrypt(message):
    """Encrypt a message using Fernet."""
    key = Fernet.generate_key()
    f = Fernet(key)

    ciphertext = f.encrypt(message.encode())

    return key.decode(), ciphertext.decode()


# ============================================================
# 2. CAESAR CIPHER
# ============================================================

def caesar_encrypt(message, shift=3):
    """Encrypt a message using Caesar Cipher."""
    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


# ============================================================
# 3. XOR ENCRYPTION
# ============================================================

def xor_encrypt(message, key):
    """Simple XOR encryption for educational purposes."""
    result = ""

    for i, char in enumerate(message):
        result += chr(ord(char) ^ ord(key[i % len(key)]))

    return base64.b64encode(result.encode("latin-1")).decode()

# ============================================================
# 4. BASE64
# ============================================================

def base64_encode(message):
    encoded = base64.b64encode(message.encode())
    return encoded.decode()


# ============================================================
# AVAILABLE ALGORITHMS
# ============================================================

algorithms = {
    "fernet": fernet_encrypt,
    "caesar": caesar_encrypt,
    "xor": xor_encrypt,
    "base64": base64_encode,
}


# ============================================================
# DISPLAY ALGORITHMS
# ============================================================

def show_algorithms():
    print("\n===== Available Algorithms =====")

    for number, algorithm in enumerate(algorithms.keys(), start=1):
        print(f"{number}. {algorithm.upper()}")

    print("================================")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    show_algorithms()

    choice = input("\nChoose an encryption algorithm: ").strip().lower()

    if choice not in algorithms:
        print("Invalid algorithm!")
        return

    message = input("Enter your message: ")

    # Fernet
    if choice in ["fernet", "1"]:

        key, ciphertext = fernet_encrypt(message)

        print("\n----- FERNET RESULT -----")
        print("Key       :", key)
        print("Ciphertext:", ciphertext)

    # Caesar
    elif choice in ["caesar", "2"]:

        shift = int(input("Enter shift value: "))

        ciphertext = caesar_encrypt(message, shift)

        print("\n----- CAESAR RESULT -----")
        print("Ciphertext:", ciphertext)

    # XOR
    elif choice in ["xor", "3"]:

        key = input("Enter XOR key: ")

        if not key:
            print("Key cannot be empty!")
            return

        ciphertext = xor_encrypt(message, key)

        print("\n----- XOR RESULT -----")
        print("Ciphertext:", ciphertext)

    # Base64
    elif choice in ["base64", "4"]:
        encoded_message = base64_encode(message)
        print("\n----- BASE64 RESULT -----")
        print("Encoded Message:", encoded_message)

