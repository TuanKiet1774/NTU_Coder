from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad
from Cryptodome.Random import get_random_bytes

# Đọc dữ liệu đầu vào
key = input().strip().encode()  # Khóa K 8 byte
n = int(input().strip())        # Số lượng byte bản rõ
plaintext_bytes = bytes(map(int, input().strip().split()))  # Dãy byte bản rõ

# Tạo IV ngẫu nhiên 8 byte
iv = get_random_bytes(8)

# Khởi tạo DES ở chế độ CBC
cipher = DES.new(key, DES.MODE_CBC, iv)

# Áp dụng padding PKCS7
padded_plaintext = pad(plaintext_bytes, DES.block_size)

# Mã hóa dữ liệu
ciphertext = cipher.encrypt(padded_plaintext)

# Ghép IV và bản mã thành một khối dữ liệu
final_output = iv + ciphertext

# Xuất kết quả
print(len(final_output))
print(" ".join(map(str, final_output)))
