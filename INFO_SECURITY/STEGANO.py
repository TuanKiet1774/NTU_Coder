import urllib.request
from PIL import Image
from io import BytesIO
import math

# Đọc input
url = input().strip()
message = input().strip()

# Bước 1: Tải ảnh từ URL
response = urllib.request.urlopen(url)
img_data = response.read()
image = Image.open(BytesIO(img_data)).convert("RGB")
pixels = list(image.getdata())

# Bước 2: Mã hóa message thành chuỗi bit
bits = []
for char in message:
    ascii_val = ord(char)
    bin_str = format(ascii_val, '08b')  # 8 bit
    bits.extend([int(b) for b in bin_str])

# Tính số pixel cần dùng
k = len(message)
p = (k * 8 - 1) // 3 + 1
print(p)

# Bước 3: Giấu các bit vào ảnh
new_pixels = []
bit_index = 0
for i in range(p):
    r, g, b = pixels[i]
    # Tạo bản sao để thay đổi bit cuối
    new_rgb = []
    for color in (r, g, b):
        if bit_index < len(bits):
            bit = bits[bit_index]
            color = (color & 0xFE) | bit  # thay bit LSB bằng bit cần giấu
            bit_index += 1
        new_rgb.append(color)

    print(*new_rgb)
