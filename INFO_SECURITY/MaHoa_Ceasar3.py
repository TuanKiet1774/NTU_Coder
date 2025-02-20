def giai_ma_ceasar(ban_ma):
    tu_dien = {"AN", "BAN", "BUA", "CHAO", "DANG", "DUNG", "GAP", "HEN", "HOM", "KHOE",
               "KHONG", "LAI", "MOI", "MUA", "NAM", "NANG", "NAY", "NGAY", "SANG", "THOI",
               "TIET", "TOI", "TROI", "VIET", "YEU"}
    
    def giai_ma_voi_khoa(ban_ma, khoa):
        ban_ro = ""
        for ky_tu in ban_ma:
            vt_kth = ord(ky_tu) - ord('A')
            vt_ktt = ord(ky_tu) - ord('a')
            if 'A' <= ky_tu <= 'Z':
                ban_ro += chr((vt_kth - khoa) % 26 + ord('A'))
            elif 'a' <= ky_tu <= 'z':
                ban_ro += chr((vt_ktt - khoa) % 26 + ord('a'))
            else:
                ban_ro += ky_tu  # Giữ nguyên khoảng trắng
        return ban_ro
    
    for khoa in range(26):
        ban_thu = giai_ma_voi_khoa(ban_ma, khoa)
        tu_ban_thu = set(ban_thu.upper().split())
        
        if tu_ban_thu & tu_dien:  
            return ban_thu
    
    return "0"

ban_ma = input().strip()
print(giai_ma_ceasar(ban_ma))
