import math

class TranspositionCipher:
    def __init__(self):
        pass

    # Hàm lấy thứ tự hoán vị của các cột dựa trên từ khóa Key
    def get_key_order(self, key):
        key = key.upper()
        # Trả về thứ tự sắp xếp của các ký tự trong key theo bảng chữ cái
        return sorted(range(len(key)), key=lambda k: key[k])

    # Hàm thực hiện mã hóa hoán vị cột (Transposition Encrypt)
    def transposition_encrypt(self, plain_text, key):
        plain_text = plain_text.upper().replace(" ", "")
        key_length = len(key)
        col_order = self.get_key_order(key)
        
        # Chia văn bản thành các hàng dữ liệu
        num_rows = math.ceil(len(plain_text) / key_length)
        # Thêm ký tự 'X' vào cuối nếu hàng cuối cùng bị thiếu ký tự
        plain_text += 'X' * (num_rows * key_length - len(plain_text))
        
        # Tạo ma trận lưới ký tự
        matrix = [plain_text[i:i + key_length] for i in range(0, len(plain_text), key_length)]
        
        # Đọc dữ liệu theo từng cột đã được hoán vị
        cipher_text = ""
        for col in col_order:
            for row in range(num_rows):
                cipher_text += matrix[row][col]
                
        return cipher_text

    # Hàm thực hiện giải mã hoán vị cột (Transposition Decrypt)
    def transposition_decrypt(self, cipher_text, key):
        key_length = len(key)
        col_order = self.get_key_order(key)
        num_rows = math.ceil(len(cipher_text) / key_length)
        
        # Tạo một ma trận trống để đổ ngược dữ liệu vào
        matrix = [['' for _ in range(key_length)] for _ in range(num_rows)]
        
        # Điền các ký tự từ chuỗi mã hóa vào từng cột theo thứ tự hoán vị
        cipher_idx = 0
        for col in col_order:
            for row in range(num_rows):
                if cipher_idx < len(cipher_text):
                    matrix[row][col] = cipher_text[cipher_idx]
                    cipher_idx += 1
                    
        # Đọc lại ma trận theo từng hàng để lấy lại văn bản gốc
        plain_text = ""
        for row in range(num_rows):
            plain_text += "".join(matrix[row])
            
        return plain_text