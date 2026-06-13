class PlayfairCipher:
    def __init__(self):
        pass

    def generate_matrix(self, key):
        key = key.upper().replace('J', 'I')
        matrix = []
        seen = set()

        for char in key:
            if char.isalpha() and char not in seen:
                seen.add(char)
                matrix.append(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in seen:
                seen.add(char)
                matrix.append(char)

        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(self, matrix, char):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col
        return None

    def prepare_text(self, text):
        text = text.upper().replace('J', 'I')
        prepared = ""
        i = 0
        while i < len(text):
            if text[i].isalpha():
                prepared += text[i]
                if i + 1 < len(text) and text[i+1].isalpha():
                    if text[i] == text[i+1]:
                        prepared += 'X'
                    else:
                        prepared += text[i+1]
                        i += 1
                else:
                    prepared += 'X'
            i += 1
        return prepared

    def playfair_encrypt(self, plain_text, key):
        matrix = self.generate_matrix(key)
        prepared_text = self.prepare_text(plain_text)
        cipher_text = ""

        for i in range(0, len(prepared_text), 2):
            char1, char2 = prepared_text[i], prepared_text[i+1]
            row1, col1 = self.find_position(matrix, char1)
            row2, col2 = self.find_position(matrix, char2)

            if row1 == row2:
                cipher_text += matrix[row1][(col1 + 1) % 5]
                cipher_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                cipher_text += matrix[(row1 + 1) % 5][col1]
                cipher_text += matrix[(row2 + 1) % 5][col2]
            else:
                cipher_text += matrix[row1][col2]
                cipher_text += matrix[row2][col1]

        return cipher_text

    def playfair_decrypt(self, cipher_text, key):
        matrix = self.generate_matrix(key)
        plain_text = ""

        for i in range(0, len(cipher_text), 2):
            char1, char2 = cipher_text[i], cipher_text[i+1]
            row1, col1 = self.find_position(matrix, char1)
            row2, col2 = self.find_position(matrix, char2)

            if row1 == row2:
                plain_text += matrix[row1][(col1 - 1) % 5]
                plain_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plain_text += matrix[(row1 - 1) % 5][col1]
                plain_text += matrix[(row2 - 1) % 5][col2]
            else:
                plain_text += matrix[row1][col2]
                plain_text += matrix[row2][col1]

        return plain_text