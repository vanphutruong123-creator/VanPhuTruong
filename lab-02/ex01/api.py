from cipher.playfair import PlayfairCipher
from cipher.railfence import RailFenceCipher
from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher  # Thêm dòng này vào đầu file (Trang 76)

app = Flask(__name__)

# ==========================================
# 1. CAESAR CIPHER ALGORITHM (Bài cũ giữ nguyên)
# ==========================================
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'encrypted_message': decrypted_text})


# ==========================================
# 2. VIGENERE CIPHER ALGORITHM (Thêm mới - Trang 76)
# ==========================================
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ==========================================
# 3. RAIL FENCE CIPHER ALGORITHM (Thêm mới - Trang 80)
# ==========================================
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])  # Trong ảnh code là num_rails, lấy từ tham số 'key' nhận vào
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

  # ==========================================
# 4. PLAYFAIR CIPHER ALGORITHM (Cập nhật đầy đủ)
# ==========================================
playfair_cipher = PlayfairCipher()

# Route 1: Mã hóa (Trang 85)
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

# Route 2: Giải mã (Trang 85)
@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Route 3: Tạo và hiển thị ma trận 5x5 (Mới bổ sung theo yêu cầu)
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_create_matrix():
    data = request.json
    key = data['key']
    matrix = playfair_cipher.generate_matrix(key)
    return jsonify({'matrix': matrix})
# ==========================================
# MAIN FUNCTION
# ==========================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)