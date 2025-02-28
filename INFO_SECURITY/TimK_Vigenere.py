def TimKhoa(ciphertext, plaintext):
    key_values = []
    for i in range(len(plaintext)):
       
        c_val = ord(ciphertext[i]) - ord('A')
        p_val = ord(plaintext[i]) - ord('A')
        k_val = (c_val - p_val) % 26
        
        key_values.append(chr(k_val + ord('A')))
    
    for key_length in range(2, len(plaintext) // 2 + 1):
        flag = True
        for i in range(key_length, len(key_values)):
            if key_values[i] != key_values[i % key_length]:
                flag = False
                break
        if flag:
            return ''.join(key_values[:key_length])
    
    return ''.join(key_values)

ciphertext = input().strip()
plaintext = input().strip()

key = TimKhoa(ciphertext, plaintext)
print(key)

#Ví dụ
#Bản mã: ZICVTWQNGRZGVTWAVZHCQYGLMGJ
#Bản rõ: WEAREDISCOVEREDSAVEYOURSELF
#Khóa: DECEPTIVE