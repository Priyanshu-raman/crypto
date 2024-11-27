from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message: str) -> str:
    """Encrypt the message using the shared secret key."""
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message.decode() 

def decrypt_message(encrypted_message: str) -> str:
    """Decrypt the encrypted message using the shared secret key."""
    try:
        decrypted_message = cipher.decrypt(encrypted_message.encode())
        return decrypted_message.decode()
    except Exception as e:
        return f"Error decrypting message: {e}"

print("=== Cryptographic Communication ===")
choice = int(input("1 for Encrypt a message, 2 for Decrypt a message: "))

if choice == 1:
    message = input("Enter your message to encrypt: ")
    encrypted = encrypt_message(message)
    print(f"Encrypted Message: {encrypted}")
    print(f"Share this key securely: {key.decode()}")
elif choice == 2:
    encrypted_message = input("Enter the encrypted message to decrypt: ")
    key_input = input("Enter the shared secret key: ")
    try:
        custom_cipher = Fernet(key_input.encode())
        decrypted = custom_cipher.decrypt(encrypted_message.encode()).decode()
        print(f"Decrypted Message: {decrypted}")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Invalid choice!")
