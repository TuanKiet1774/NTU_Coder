from Cryptodome.Hash import MD5, SHA256

password = input() 
temp = password.encode()

#Giá trị băm MD5
md5 = MD5.new()
md5.update(temp)

#Giá trị băm SHA256
sha256 = SHA256.new()
sha256.update(temp)

#hexdigest() để trả về giá trị băm của dữ liệu dưới dạng một chuỗi thập lục phân
print(md5.hexdigest())
print(sha256.hexdigest())

#Ví dụ
#input: iloveyou
#output:
#Giá trị MD5: f25a2fc72690b780b2a14e140ef6a9e0
#Giá trị SHA1: e4ad93ca07acb8d908a3aa41e920ea4f4ef4f26e7f86cf8291c5db289780a5ae