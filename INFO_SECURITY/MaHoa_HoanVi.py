def MaHoa_HoanVi(text, key):
    text = text.replace(" ", "")
    
    cot = len(key)
    dong = (len(text) + cot - 1) // cot
    
    so_o = dong * cot
    
    if len(text) < so_o:
        pad_len = so_o - len(text)
        for i in range(pad_len):
            pad_char = chr(ord('A') + i % 26)
            text += pad_char
    
    #Xếp dãy bản rõ vào ma trận
    matrix = []
    for i in range(dong):
        row = []
        for j in range(cot):
            index = i * cot + j
            if index < len(text):
                row.append(text[index])
            else:
                row.append('')
        matrix.append(row)
    
    #Sắp xếp khóa
    key_order = []
    for char in key:
        pos = 0
        for exist_char in key[:key.index(char)]:
            if exist_char > char:
                pos -= 1
        key_order.append(key.index(char) + pos)
    
    key_pos = [(char, i) for i, char in enumerate(key)]
    key_pos.sort()  
    column_order = [pos for char, pos in key_pos]
    
    ban_ma = ''
    for col_idx in column_order:
        for row_idx in range(dong):
            ban_ma += matrix[row_idx][col_idx]
    
    return ban_ma

text = input().strip()
key = input().strip()

ban_ma = MaHoa_HoanVi(text, key)
print(ban_ma)

#Ví dụ
#Bản rõ: WEAREDISCOVERED
#Khóa: QUITE
#Mã: EODASRWDVRCEEIE
