from cryptography.fernet import Fernet
import base64



# ============================================================
# FERNET DECRYPTION
# ============================================================

def fernet_decrypt(key, ciphertext):
    """
    Decrypt a Fernet encrypted message.

    key        -> Fernet key used during encryption
    ciphertext -> Encrypted message
    """

    try:
        f = Fernet(key.encode())
        plaintext = f.decrypt(ciphertext.encode())

        return plaintext.decode()

    except Exception as e:
        return f"Decryption failed: {e}"


# ============================================================
# CAESAR CIPHER DECRYPTION
# ============================================================

def caesar_decrypt(ciphertext, shift):
    """
    Decrypt a Caesar Cipher message.
    """

    plaintext = ""

    for char in ciphertext:

        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            plaintext += chr(
                (ord(char) - base - shift) % 26 + base
            )

        else:
            plaintext += char

    return plaintext


# ============================================================
# XOR DECRYPTION
# ============================================================

def xor_decrypt(ciphertext, key):
    """
    Decrypt Base64-encoded XOR ciphertext.
    """

    try:
        encrypted = base64.b64decode(ciphertext)

        plaintext = ""

        for i, byte in enumerate(encrypted):

            plaintext += chr(
                byte ^ ord(key[i % len(key)])
            )

        return plaintext

    except Exception as e:
        return f"Decryption failed: {e}"


# ============================================================
# BASE64 DECODE
# ============================================================

def base64_decrypt(encoded_message):
    """
    Decode a Base64 encoded message.

    Note: Base64 is encoding, not encryption.
    """

    try:
        decoded = base64.b64decode(encoded_message)

        return decoded.decode()

    except Exception as e:
        return f"Base64 decoding failed: {e}"

def main():
    print("Welcome to the JCrypt Decryptor")
    print("1. Fernet Decrypt  2. Caesar Decrypt  3. XOR Decrypt  4. Base64 Decode")

    choice = input("Enter your choice: ").strip().lower()

    if choice in ["fernet", "1"]:
        key = input("Enter the Fernet key: ")
        ciphertext = input("Enter the ciphertext: ")
        plaintext = fernet_decrypt(key, ciphertext)
        print(f"Decrypted message: {plaintext}")

    elif choice in ["caesar", "2"]:
        ciphertext = input("Enter the ciphertext: ")
        shift = int(input("Enter the shift value: "))
        plaintext = caesar_decrypt(ciphertext, shift)
        print(f"Decrypted message: {plaintext}")

    elif choice in ["xor", "3"]:
        ciphertext = input("Enter the Base64-encoded XOR ciphertext: ")
        key = input("Enter the key used for XOR encryption: ")
        plaintext = xor_decrypt(ciphertext, key)
        print(f"Decrypted message: {plaintext}")

    elif choice in ["base64", "4"]:
        encoded_message = input("Enter the Base64 encoded message: ")
        decoded_message = base64_decrypt(encoded_message)
        print(f"Decoded message: {decoded_message}")

    else:
        print("Invalid option. Please try again.")


 