from flask import Flask, request, jsonify
from flask_cors import CORS
from cryptography.fernet import Fernet

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    key = Fernet.generate_key()
    cipher = Fernet(key)
    """Encrypt the message using the shared secret key."""
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    encrypted_message = cipher.encrypt(message.encode())
    return jsonify({'encrypted_message': encrypted_message.decode(), 'key': key.decode()})


@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    """Decrypt the encrypted message using the shared secret key."""
    data = request.json
    encrypted_message = data.get('encrypted_message')
    key = data.get('key')
    cipher = Fernet(key)
    if not encrypted_message:
        return jsonify({'error': 'No encrypted message provided'}), 400
    try:
        decrypted_message = cipher.decrypt(encrypted_message.encode())
        return jsonify({'decrypted_message': decrypted_message.decode()})
    except Exception as e:
        return jsonify({'error': f"Error decrypting message: {e}"}), 400


if __name__ == '__main__':
    app.run(debug=True)
