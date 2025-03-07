#Lưu ý: Cài thư viện PyCryptodomex
#pip install pycryptodomex
#pip install pycryptodome
from Cryptodome.Cipher import DES

def pad(tmp):
    n = len(tmp) % 8
    if n > 0: n = 8-n
    return tmp + (b' ' * n)

key = input().encode()
plain = input().encode()
padded = pad(plain)

des = DES.new(key, DES.MODE_ECB)
cipher = des.encrypt(padded)

print(len(cipher))
for v in cipher:  print(v, end=' ')
print()

tmp = des.decrypt(cipher)  
text = tmp.decode()
print(text)

#Ví dụ
#Khóa K: hello123
#Bản rõ: Python is the Best Language!
#Kết quả
#Chiều dài bản mã m = 32
#Bản mã: 123 1 94 254 213 209 143 77 26 204 213 188 4 28 14 109 36 44 193 199 119 45 72 49 230 62 8 37 33 171 208 88
#Bản giải mã: Python is the Best Language!
