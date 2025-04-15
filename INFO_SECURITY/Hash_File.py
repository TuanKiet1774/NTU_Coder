import urllib.request
from Cryptodome.Hash import MD5, SHA256

url = input() 
temp = urllib.request.urlopen(url)
data = temp.read()

#Giá trị băm MD5
md5 = MD5.new()
md5.update(data)

#Giá trị băm SHA256
sha256 = SHA256.new()
sha256.update(data)

#hexdigest() để trả về giá trị băm của dữ liệu dưới dạng một chuỗi thập lục phân
print(md5.hexdigest())
print(sha256.hexdigest())

#Ví dụ
#input: https://64cntt3.ntucoder.net/ckfinder/userfiles/files/LoremIpsum.txt
#output:
#Giá trị MD5: 4299bec5205abc671e01d3d1cddb5fc1
#Giá trị SHA1: 175c7c1cb973a0b8960b9d9f76be13388e67cb256db15e888f3faedbd5db952a
