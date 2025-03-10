import tkinter as tk
from tkinter import ttk
from collections import Counter

class MaHoa_ThayThe:
    def __init__(self, root):
        self.root = root
        self.root.title("Mã hóa thay thế đơn bảng")
        self.root.geometry("1200x680")
        self,root.configure(bg = "Black")
        
        # Ô nhập bản mã
        self.text_input = tk.Text(root, width=50, height=15, font=("Arial", 10), fg="black")
        self.text_input.place(x=20, y=10, width=441, height=241)
        
        # Nút thống kê và phá mã
        self.analyze_button = tk.Button(root, text="Thống Kê", command=self.Phan_Tich, bg="lightblue", fg="black")
        self.analyze_button.place(x=60, y=280, width=93, height=28)
        
        self.decrypt_button = tk.Button(root, text="Phá Mã", command=self.Ma_Hoa, bg="lightgreen", fg="black")
        self.decrypt_button.place(x=290, y=280, width=93, height=28)
        
        # Ô hiển thị bản rõ
        self.text_output = tk.Text(root, width=50, height=15, font=("Arial", 10), fg="blue",)
        self.text_output.place(x=20, y=320, width=441, height=241)
        
        # Bảng tần suất ký tự
        self.char_table_frame = tk.Frame(root)
        self.char_table_frame.place(x=500, y=10, width=210, height=650)
        
        self.char_table = ttk.Treeview(self.char_table_frame, columns=("Char", "Freq", "Repl"), show="headings")
        self.char_table.heading("Char", text="Chữ")
        self.char_table.heading("Freq", text="Tần Số")
        self.char_table.heading("Repl", text="Thay")
        self.char_table.column("Char", width=50)
        self.char_table.column("Freq", width=70)
        self.char_table.column("Repl", width=50)
        self.char_table.pack(fill=tk.BOTH, expand=True)
        
        # Bảng tần suất ký tự đôi
        self.digram_table_frame = tk.Frame(root)
        self.digram_table_frame.place(x=740, y=10, width=210, height=650)
        
        self.digram_table = ttk.Treeview(self.digram_table_frame, columns=("Digram", "Freq"), show="headings")
        self.digram_table.heading("Digram", text="Digram")
        self.digram_table.heading("Freq", text="Tần Số")
        self.digram_table.column("Digram", width=82)
        self.digram_table.column("Freq", width=82)
        self.digram_table.pack(fill=tk.BOTH, expand=True)
        
        # Bảng tần suất kỳ tự ba
        self.trigram_table_frame = tk.Frame(root)
        self.trigram_table_frame.place(x=980, y=10, width=210, height=650)
        
        self.trigram_table = ttk.Treeview(self.trigram_table_frame, columns=("Trigram", "Freq"), show="headings")
        self.trigram_table.heading("Trigram", text="Trigram")
        self.trigram_table.heading("Freq", text="Tần Số")
        self.trigram_table.column("Trigram", width=82)
        self.trigram_table.column("Freq", width=82)
        self.trigram_table.pack(fill=tk.BOTH, expand=True)
        
        # Cột ký tự thay thế
        self.char_table.bind("<Double-1>", self.Chinh_Sua_Thay_The)
        self.current_edit = None

    def Phan_Tich(self):
        for item in self.char_table.get_children():
            self.char_table.delete(item)
        for item in self.digram_table.get_children():
            self.digram_table.delete(item)
        for item in self.trigram_table.get_children():
            self.trigram_table.delete(item)
        
        #Chuyển văn bản thành hoa
        text = self.text_input.get("1.0", tk.END).upper()
        letters_only = [c for c in text if c.isalpha()]
        
        #Đếm tần suất
        letter_counts = sorted(Counter(letters_only).items(), key=lambda x: x[1], reverse=True)
        digram_counts = sorted(Counter("".join(letters_only[i:i+2]) for i in range(len(letters_only)-1)).items(), key=lambda x: x[1], reverse=True)
        trigram_counts = sorted(Counter("".join(letters_only[i:i+3]) for i in range(len(letters_only)-2)).items(), key=lambda x: x[1], reverse=True)
        
        for char, freq in letter_counts:
            self.char_table.insert("", tk.END, values=(char, freq, ""))
        
        for digram, freq in digram_counts:
            self.digram_table.insert("", tk.END, values=(digram, freq))
        
        for trigram, freq in trigram_counts:
            self.trigram_table.insert("", tk.END, values=(trigram, freq))

    def Chinh_Sua_Thay_The(self, event):
        item = self.char_table.identify_row(event.y)
        column = self.char_table.identify_column(event.x)
        
        if column == "#3" and item:
            x, y, width, height = self.char_table.bbox(item, column)
            
            #Nhập để chỉnh sửa
            entry = tk.Entry(self.char_table, width=5)
            entry.place(x=x, y=y, width=width, height=height)
            
            # Đặt giá trị mục nhập hiện tại nếu có
            current_value = self.char_table.item(item, "values")[2]
            entry.insert(0, current_value)
            entry.focus_set()
            
            # Lưu mục đang được chỉnh sửa
            self.current_edit = (item, entry)
            
            # Liên kết các sự kiện Enter và Focus Out để lưu giá trị đã chỉnh sửa
            entry.bind("<Return>", lambda e: self.Luu_Chinh_Sua())
            entry.bind("<FocusOut>", lambda e: self.Luu_Chinh_Sua())

    def Luu_Chinh_Sua(self):
        if self.current_edit:
            item, entry = self.current_edit
            values = list(self.char_table.item(item, "values"))
            values[2] = entry.get()
            self.char_table.item(item, values=values)
            entry.destroy()
            self.current_edit = None

    def Ma_Hoa(self):
        text = self.text_input.get("1.0", tk.END)
        
        replace_map = {}
        for item in self.char_table.get_children():
            values = self.char_table.item(item, "values")
            letter = values[0]
            replacement = values[2]
            if letter and replacement:
                replace_map[letter] = replacement

        decrypted_text = ""
        for char in text:
            if char in replace_map:  
                decrypted_text += replace_map[char]
            elif char.isalpha():  
                decrypted_text += " "  
            else:  
                decrypted_text += char  
        
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert("1.0", decrypted_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MaHoa_ThayThe(root)
    root.mainloop()