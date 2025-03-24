from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import sys

def generate_rsa_keys():
    key = RSA.generate(1024)
    private_key_pem = key.export_key()
    public_key_pem = key.publickey().export_key()
    return private_key_pem.decode(), public_key_pem.decode(), key

def encrypt_session_key(session_key_hex, public_key_pem):
    session_key = bytes.fromhex(session_key_hex)
    public_key = RSA.import_key(public_key_pem)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_session_key = cipher.encrypt(session_key)
    return encrypted_session_key.hex()

def decrypt_session_key(encrypted_session_key_hex, private_key_pem):
    encrypted_session_key = bytes.fromhex(encrypted_session_key_hex)
    private_key = RSA.import_key(private_key_pem)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_session_key = cipher.decrypt(encrypted_session_key)
    return decrypted_session_key.hex()

session_key_hex = input().strip()  # Nhận đầu vào là khóa phiên DES dạng hex (16 ký tự hexa)
  
private_key_pem, public_key_pem, key = generate_rsa_keys()
encrypted_session_key_hex = encrypt_session_key(session_key_hex, public_key_pem)
decrypted_session_key_hex = decrypt_session_key(encrypted_session_key_hex, private_key_pem)

print(private_key_pem)  # In khóa riêng ở định dạng PEM
print(public_key_pem)   # In khóa công khai ở định dạng PEM
print(encrypted_session_key_hex)  # In bản mã hóa khóa phiên
print(decrypted_session_key_hex)  # In bản giải mã khóa phiên

"""
Input: abcdef0123456789
Output:
-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQC0fCxa9zQPro4cXDd6boP6XEFuGC7yiGNsLXsu2uQP7TYmgLoD
2rh7YYbqjLh+bIDht3LPeYTJ2PHboXZfPhYdDP9ciG5J/X0o2OMRX6wEUE0BssdM
+nMzsfCtQMFT43isYtk/tymF9dbH7g0NjAeGekrV5SWM329eFphAY1bixQIDAQAB
AoGABv8TRxlzGrKFDsNiYSwckJ136dklJMC1vfFLZ6cTlSx4X2i5DUIyyZGfxcLb
ugbhvh465KEMzThMM9vf91Q0Ti45pbVyradGlOn77uAWPHeaqKQFQ5cRDjhA/q5i
Xf9h+mHeK/9MRm55bDn6YnYuS8QVlsmFbPUHVDU9q9ndD0cCQQDAwI0yBrM1hZF6
QRUUHD8ror3WipKS0trzfXRAOnWCW9J/wd3lQQa5Asaqx3eAOeZxV1Ig38HtC+3/
JDskWh6nAkEA77UrBsJezzLfttHdQbm7/U173na1bxGHuIiXiMJ8Di72a3mLFlow
qgZEiP3lZNsVPV1vMvHBOjT1zZpNixNsswJAIw7in4a4cbOpkiLkQpQgqT8gaDUs
E6hmSoM28bewR9WLo9EPGvOI1X27xLQi+B+P2m2XcoNAMm1JDG76ktIRYQJAEAQ/
8rysDxYsIpAVQ54AdKVnwG6YIuq98dOWpHmyRlRW/MlrRLwUAlhW3fxxBnMpESec
FYBX0+bUAb/srH1IxwJABcIbIBRAovyS+FJrW+xOycp3UbubthfVOoUTD+V4UhVP
Bd6iaN8+KgylSaBrrZFLWypuvVLWUyxi/+/SPetmtQ==
-----END RSA PRIVATE KEY-----
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC0fCxa9zQPro4cXDd6boP6XEFu
GC7yiGNsLXsu2uQP7TYmgLoD2rh7YYbqjLh+bIDht3LPeYTJ2PHboXZfPhYdDP9c
iG5J/X0o2OMRX6wEUE0BssdM+nMzsfCtQMFT43isYtk/tymF9dbH7g0NjAeGekrV
5SWM329eFphAY1bixQIDAQAB
-----END PUBLIC KEY-----
6087da556c7833edd503e54eca1e90bfa3a6d804b9759cb1fc1f38725249e00cee2491d2478ff7c88d297a8575e48d2395c96c968d1322b748ffb687b39d5a7ef2e65a64c16323d2c747d3b81bb236970d20b3392fd15ca0b82b5f0f1c0f9c832926f790e4bb6224a88f402deef3cbf2c39d9d08496edaa5cc4e185612d74e81
abcdef0123456789
"""