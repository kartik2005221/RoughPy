import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def guide():
    print("""
Welcome to the Encoding/Encrypting Tool!
- Choose the desired method from the menu.
- If the method supports decoding or decrypting, select the appropriate option.
- Provide the input (message or encoded/encrypted text) when prompted.

Available Methods:
1. Base64 - Encoding/Decoding.
2. SHA (SHA-1, SHA-256, SHA-512) - Hashing (one-way; no decoding).
3. AES (Advanced Encryption Standard) - Symmetric encryption (encrypt/decrypt with a key).
4. Exit - Quit the tool.
""")

def base64_tool():
    choice = input("Choose operation: [1] Encode [2] Decode: ")
    if choice == "1":
        message = input("Enter the message to encode: ")
        encoded = base64.b64encode(message.encode()).decode()
        print("Encoded Message:", encoded)
    elif choice == "2":
        encoded = input("Enter the Base64-encoded message: ")
        try:
            decoded = base64.b64decode(encoded).decode()
            print("Decoded Message:", decoded)
        except Exception as e:
            print("Invalid Base64 input:", e)
    else:
        print("Invalid choice.")

def sha_tool():
    print("Choose Hash Algorithm: [1] SHA-1 [2] SHA-256 [3] SHA-512")
    choice = input("Enter your choice: ")
    message = input("Enter the message to hash: ")
    if choice == "1":
        hashed = hashlib.sha1(message.encode()).hexdigest()
        print("SHA-1 Hash:", hashed)
    elif choice == "2":
        hashed = hashlib.sha256(message.encode()).hexdigest()
        print("SHA-256 Hash:", hashed)
    elif choice == "3":
        hashed = hashlib.sha512(message.encode()).hexdigest()
        print("SHA-512 Hash:", hashed)
    else:
        print("Invalid choice.")

def aes_tool():
    key = input("Enter a 16-character key (for AES): ").encode()
    if len(key) != 16:
        print("Key must be exactly 16 characters long!")
        return
    cipher = AES.new(key, AES.MODE_ECB)
    choice = input("Choose operation: [1] Encrypt [2] Decrypt: ")
    if choice == "1":
        message = input("Enter the message to encrypt: ")
        encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
        print("Encrypted Message (Base64):", base64.b64encode(encrypted).decode())
    elif choice == "2":
        encoded = input("Enter the Base64-encoded encrypted message: ")
        try:
            decoded_encrypted = base64.b64decode(encoded)
            decrypted = unpad(cipher.decrypt(decoded_encrypted), AES.block_size)
            print("Decrypted Message:", decrypted.decode())
        except Exception as e:
            print("Decryption failed:", e)
    else:
        print("Invalid choice.")

def main():
    while True:
        guide()
        choice = input("Choose your option [1-4]: ")
        if choice == "1":
            base64_tool()
        elif choice == "2":
            sha_tool()
        elif choice == "3":
            aes_tool()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
