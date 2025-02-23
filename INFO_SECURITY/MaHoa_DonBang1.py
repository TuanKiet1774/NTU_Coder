def MaHoa_DonBang(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mapping = {alphabet[i]: key[i] for i in range(26)} 
    #print(mapping) #Ứng với mỗi từ trong alphabet sẽ là một từ trong khóa key nhập vào
    
    crypto = "" 
    for char in text:  
        if char in mapping:  
            crypto += mapping[char]  
        else:  
            crypto += char  #Giữ nguyên khoảng trắng

    return crypto

text = input().strip()
key = input().strip()

print(MaHoa_DonBang(text, key))

#Ví dụ
#Bản rõ: meet me after the toga party
#Khóa: zpbyjrskflxqnwvdhmgutoiaec
#Kết quả: njju nj zrujm ukj uvsz dzmue