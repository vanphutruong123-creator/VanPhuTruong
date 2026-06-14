import sys
import os
import ctypes
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
# Nạp lớp giao diện từ file caesar.py bạn đã dịch
from caesar import Ui_MainWindow 
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện click chuột của các button với hàm xử lý API
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        
        # Lấy dữ liệu từ các ô nhập liệu trên giao diện
        payload = {
            "plain_text": self.ui.txt_plain.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        
        try:
            # Gửi yêu cầu mã hóa đến Server Flask
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị chuỗi đã mã hóa lên ô CipherText
                self.ui.txt_cipher.setPlainText(data["encrypted_message"])
                
                # Hiển thị thông báo thành công
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.setWindowTitle("Success")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        
        # Lấy dữ liệu mã hóa và khóa để gửi đi giải mã
        payload = {
            "cipher_text": self.ui.txt_cipher.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        
        try:
            # Gửi yêu cầu giải mã đến Server Flask
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Trả kết quả chữ ban đầu về ô Plain Text
                self.ui.txt_plain.setPlainText(data["decoded_message"])
                
                # Hiển thị thông báo thành công
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.setWindowTitle("Success")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

if __name__ == "__main__":
    # --- ĐOẠN FIX LỖI HIỂN THỊ CO GIÃN ĐỘ PHÂN GIẢI (HIGH DPI) ---
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass
            
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    # ------------------------------------------------------------

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())