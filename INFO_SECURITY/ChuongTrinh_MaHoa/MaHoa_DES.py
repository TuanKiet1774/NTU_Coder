import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class AppMaHoa:
    def __init__(self, root):
        self.root = root
        self.root.title("Mã Hóa Des")
        self.root.geometry("600x650")  # Tăng kích thước để chứa nhiều tính năng hơn
        self.root.resizable(False, False)
        
        self.key = None
        self.iv = None
        self.input_file_path = None
        self.output_file_path = None
        
        self.tao_giao_dien()
        
    def tao_giao_dien(self):
        # Frame chính
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Tiêu đề
        title_label = ttk.Label(main_frame, text="Mã Hóa và Giải Mã DES", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Chọn file đầu vào
        input_frame = ttk.LabelFrame(main_frame, text="File đầu vào", padding=10)
        input_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=5)
        
        self.input_path_var = tk.StringVar()
        input_entry = ttk.Entry(input_frame, textvariable=self.input_path_var, width=50)
        input_entry.grid(row=0, column=0, padx=5, pady=5)
        
        browse_button = ttk.Button(input_frame, text="Duyệt...", command=self.duyet_file)
        browse_button.grid(row=0, column=1, padx=5, pady=5)
        
        # Hiển thị thông tin file
        self.file_info_var = tk.StringVar()
        file_info_label = ttk.Label(input_frame, textvariable=self.file_info_var, foreground="blue")
        file_info_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=5)
        
        # Khóa mã hóa
        key_frame = ttk.LabelFrame(main_frame, text="Khóa mã hóa", padding=10)
        key_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=5)
        
        self.key_var = tk.StringVar()
        key_entry = ttk.Entry(key_frame, textvariable=self.key_var, width=50)
        key_entry.grid(row=0, column=0, padx=5, pady=5)
        
        key_button_frame = ttk.Frame(key_frame)
        key_button_frame.grid(row=0, column=1, padx=5, pady=5)
        
        tao_khoa_button = ttk.Button(key_button_frame, text="Tạo khóa", command=self.tao_khoa, width=10)
        tao_khoa_button.grid(row=0, column=0, padx=2)
        
        luu_khoa_button = ttk.Button(key_button_frame, text="Lưu khóa", command=self.luu_khoa, width=10)
        luu_khoa_button.grid(row=0, column=1, padx=2)
        
        tai_khoa_button = ttk.Button(key_button_frame, text="Tải khóa", command=self.tai_khoa, width=10)
        tai_khoa_button.grid(row=0, column=2, padx=2)
        
        # Khung IV (Initialization Vector) - Ban đầu ẩn
        self.iv_frame = ttk.LabelFrame(main_frame, text="IV (Initialization Vector)", padding=10)
        self.iv_frame.grid(row=3, column=0, columnspan=3, sticky="ew", pady=5)
        self.iv_frame.grid_remove()  # Ẩn ban đầu, chỉ hiển thị khi chọn CBC
        
        self.iv_var = tk.StringVar()
        iv_entry = ttk.Entry(self.iv_frame, textvariable=self.iv_var, width=50)
        iv_entry.grid(row=0, column=0, padx=5, pady=5)
        
        iv_button_frame = ttk.Frame(self.iv_frame)
        iv_button_frame.grid(row=0, column=1, padx=5, pady=5)
        
        tao_iv_button = ttk.Button(iv_button_frame, text="Tạo IV", command=self.tao_iv, width=10)
        tao_iv_button.grid(row=0, column=0, padx=2)
        
        # Thêm lưu ý về IV
        iv_note = ttk.Label(self.iv_frame, text="IV sẽ được tự động tạo khi mã hóa và được đọc từ file khi giải mã", 
                           foreground="gray", font=("Arial", 9, "italic"))
        iv_note.grid(row=1, column=0, columnspan=2, sticky="w", padx=5)
        
        # File đầu ra
        output_frame = ttk.LabelFrame(main_frame, text="File đầu ra", padding=10)
        output_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=5)
        
        output_name_label = ttk.Label(output_frame, text="Tên file:")
        output_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.output_name_var = tk.StringVar()
        output_name_entry = ttk.Entry(output_frame, textvariable=self.output_name_var, width=30)
        output_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        self.output_path_var = tk.StringVar()
        output_entry = ttk.Entry(output_frame, textvariable=self.output_path_var, width=50)
        output_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        save_button = ttk.Button(output_frame, text="Chọn thư mục...", command=self.cho_luu)
        save_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Chế độ mã hóa
        self.encryption_mode = tk.StringVar(value="ECB")
        mode_frame = ttk.LabelFrame(main_frame, text="Chế độ mã hóa", padding=10)
        mode_frame.grid(row=5, column=0, columnspan=3, sticky="ew", pady=5)
        
        ecb_radio = ttk.Radiobutton(mode_frame, text="ECB (Electronic Codebook)", 
                                    variable=self.encryption_mode, value="ECB", 
                                    command=self.toggle_iv_visibility)
        ecb_radio.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        cbc_radio = ttk.Radiobutton(mode_frame, text="CBC (Cipher Block Chaining)", 
                                    variable=self.encryption_mode, value="CBC", 
                                    command=self.toggle_iv_visibility)
        cbc_radio.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Nút thao tác
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=6, column=0, columnspan=3, pady=15)
        
        encrypt_button = ttk.Button(action_frame, text="Mã hóa", command=self.ma_hoa, width=15)
        encrypt_button.grid(row=0, column=0, padx=10)
        
        decrypt_button = ttk.Button(action_frame, text="Giải mã", command=self.giai_ma, width=15)
        decrypt_button.grid(row=0, column=1, padx=10)
        
        # Thanh trạng thái
        self.status_var = tk.StringVar()
        self.status_var.set("Sẵn sàng")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=8, column=0, columnspan=3, sticky="ew", pady=5)
    
    def toggle_iv_visibility(self):
        """Hiển thị/ẩn khung IV dựa trên chế độ mã hóa được chọn"""
        if self.encryption_mode.get() == "CBC":
            self.iv_frame.grid()
            # Tự động tạo IV mới nếu chưa có
            if not self.iv_var.get():
                self.tao_iv()
        else:
            self.iv_frame.grid_remove()
    
    def tao_iv(self):
        """Tạo IV mới và hiển thị ở dạng base64"""
        self.iv = get_random_bytes(8)  # DES block size là 8 bytes
        iv_b64 = base64.b64encode(self.iv).decode('utf-8')
        self.iv_var.set(iv_b64)
        self.status_var.set("Đã tạo IV mới")
    
    def duyet_file(self):
        filename = filedialog.askopenfilename(title="Chọn file cần mã hóa/giải mã", filetypes=[("Tất cả các file", "*.*")])
        if filename:
            self.input_file_path = filename
            self.input_path_var.set(filename)
            
            # Hiển thị thông tin file
            file_size = os.path.getsize(filename)
            size_str = self.dinh_dang_kich_thuoc(file_size)
            file_name = os.path.basename(filename)
            self.file_info_var.set(f"File: {file_name} - Kích thước: {size_str}")
            
            # Tự động đề xuất tên file đầu ra
            base_name = os.path.basename(filename)
            file_name, file_ext = os.path.splitext(base_name)
            
            # Đề xuất tên file mới với suffix
            if not self.output_name_var.get():
                if self.file_mahoa(filename):
                    # Nếu tên file có vẻ đã được mã hóa, đề xuất tên giải mã
                    suggested_name = f"{file_name.replace('_encrypted', '')}{file_ext}"
                else:
                    # Ngược lại, đề xuất tên mã hóa
                    suggested_name = f"{file_name}_encrypted{file_ext}"
                self.output_name_var.set(suggested_name)
    
    def file_mahoa(self, filename):
        # Kiểm tra xem file có vẻ đã được mã hóa hay chưa dựa trên tên
        base_name = os.path.basename(filename)
        return "_encrypted" in base_name
    
    def dinh_dang_kich_thuoc(self, size_bytes):
        """Format kích thước file từ byte sang KB, MB, GB"""
        if size_bytes < 1024:
            return f"{size_bytes} bytes"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.2f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.2f} MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"
    
    def cho_luu(self):
        directory = filedialog.askdirectory(title="Chọn thư mục lưu file đầu ra")
        if directory:
            self.output_path_var.set(directory)
            
            # Cập nhật đường dẫn đầy đủ của file đầu ra
            self.cap_nhat_link_file()
    
    def cap_nhat_link_file(self):
        output_dir = self.output_path_var.get()
        output_name = self.output_name_var.get()
        
        if output_dir and output_name:
            self.output_file_path = os.path.join(output_dir, output_name)
    
    def tao_khoa(self):
        # DES yêu cầu khóa 8 byte (64 bit)
        self.key = get_random_bytes(8)
        # Hiển thị khóa ở dạng base64 cho người dùng
        key_b64 = base64.b64encode(self.key).decode('utf-8')
        self.key_var.set(key_b64)
        self.status_var.set("Đã tạo khóa mới")
    
    def luu_khoa(self):
        if not self.key_var.get():
            messagebox.showerror("Lỗi", "Không có khóa để lưu! Vui lòng tạo hoặc nhập khóa trước.")
            return
        
        key_file = filedialog.asksaveasfilename(
            title="Lưu khóa",
            defaultextension=".key",
            filetypes=[("Key files", "*.key"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if key_file:
            try:
                with open(key_file, 'w') as file:
                    file.write(self.key_var.get())
                messagebox.showinfo("Thành công", f"Đã lưu khóa vào file: {os.path.basename(key_file)}")
                self.status_var.set(f"Đã lưu khóa vào: {os.path.basename(key_file)}")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể lưu khóa: {str(e)}")
                self.status_var.set(f"Lỗi khi lưu khóa: {str(e)}")
    
    def tai_khoa(self):
        key_file = filedialog.askopenfilename(
            title="Tải khóa",
            filetypes=[("Key files", "*.key"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if key_file:
            try:
                with open(key_file, 'r') as file:
                    key_content = file.read().strip()
                
                # Kiểm tra xem nội dung file có phải là Base64 hợp lệ không
                try:
                    base64.b64decode(key_content)
                    self.key_var.set(key_content)
                    self.status_var.set(f"Đã tải khóa từ: {os.path.basename(key_file)}")
                except:
                    messagebox.showerror("Lỗi", "File không chứa khóa hợp lệ!")
                    self.status_var.set("Không thể tải khóa: Định dạng không hợp lệ")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể đọc file: {str(e)}")
                self.status_var.set(f"Lỗi khi đọc file khóa: {str(e)}")
    
    def lay_khoa(self):
        if not self.key_var.get():
            messagebox.showerror("Lỗi", "Vui lòng tạo hoặc nhập khóa mã hóa!")
            return None
        
        try:
            # Nếu người dùng đã nhập khóa dưới dạng base64
            key_input = self.key_var.get()
            if self.key and key_input == base64.b64encode(self.key).decode('utf-8'):
                return self.key
            
            # Nếu người dùng nhập khóa mới
            return base64.b64decode(key_input)
        except:
            messagebox.showerror("Lỗi", "Khóa không hợp lệ! Vui lòng nhập khóa ở định dạng Base64 hoặc tạo khóa mới.")
            return None
    
    def lay_iv(self):
        """Lấy IV từ ô nhập liệu hoặc tạo IV mới nếu cần"""
        if self.encryption_mode.get() != "CBC":
            return None
            
        if not self.iv_var.get():
            self.tao_iv()
            
        try:
            iv_input = self.iv_var.get()
            if self.iv and iv_input == base64.b64encode(self.iv).decode('utf-8'):
                return self.iv
                
            return base64.b64decode(iv_input)
        except:
            messagebox.showerror("Lỗi", "IV không hợp lệ! Tạo IV mới.")
            self.tao_iv()
            return self.iv
    
    def get_cipher(self, key, encrypt=True):
        mode = self.encryption_mode.get()
        
        if mode == "ECB":
            return DES.new(key, DES.MODE_ECB)
        elif mode == "CBC":
            # Với CBC cần IV (Initialization Vector)
            if encrypt:
                # Khi mã hóa, lấy IV từ giao diện hoặc tạo IV mới
                iv = self.lay_iv()
                cipher = DES.new(key, DES.MODE_CBC, iv)
                return cipher, iv
            else:
                # Khi giải mã, IV được đọc từ 8 byte đầu tiên của file
                return None  # Sẽ tạo cipher sau khi đọc IV từ file
        
        return None
    
    def ma_hoa(self):
        # Cập nhật đường dẫn file đầu ra trước khi mã hóa
        self.cap_nhat_link_file()
        
        if not self.ktra_file():
            return
        
        key = self.lay_khoa()
        if not key:
            return
        
        try:
            # Đọc file đầu vào
            with open(self.input_file_path, 'rb') as file:
                data = file.read()
            
            # Kích thước file
            file_size = len(data)
            self.status_var.set(f"Đang mã hóa file {os.path.basename(self.input_file_path)}...")
            
            # Đảm bảo dữ liệu là bội số của kích thước khối DES (8 bytes)
            padded_data = pad(data, DES.block_size)
            
            mode = self.encryption_mode.get()
            iv = None
            
            if mode == "ECB":
                # Tạo cipher DES với chế độ ECB
                cipher = DES.new(key, DES.MODE_ECB)
                encrypted_data = cipher.encrypt(padded_data)
            else:  # CBC mode
                # Tạo cipher DES với chế độ CBC, sử dụng IV từ giao diện
                iv = self.lay_iv()
                cipher = DES.new(key, DES.MODE_CBC, iv)
                encrypted_data = cipher.encrypt(padded_data)
                
                # Hiển thị IV được sử dụng (có thể đã thay đổi nếu người dùng đã nhập IV mới)
                if iv:
                    iv_b64 = base64.b64encode(iv).decode('utf-8')
                    self.iv_var.set(iv_b64)
                    self.iv = iv
            
            # Ghi dữ liệu đã mã hóa ra file
            with open(self.output_file_path, 'wb') as file:
                # Nếu sử dụng CBC, lưu IV ở đầu file để sử dụng khi giải mã
                if mode == "CBC" and iv:
                    file.write(iv)
                file.write(encrypted_data)
            
            self.status_var.set(f"Đã mã hóa thành công file: {os.path.basename(self.input_file_path)}")
            
            # Hiển thị kích thước file trước và sau khi mã hóa
            encrypted_size = os.path.getsize(self.output_file_path)
            size_before = self.dinh_dang_kich_thuoc(file_size)
            size_after = self.dinh_dang_kich_thuoc(encrypted_size)
            
            messagebox.showinfo("Thành công", 
                f"Đã mã hóa file thành công!\n\n"
                f"File gốc: {size_before}\n"
                f"File đã mã hóa: {size_after}\n\n"
                f"Lưu tại: {self.output_file_path}")
            
        except Exception as e:
            self.status_var.set(f"Lỗi: {str(e)}")
            messagebox.showerror("Lỗi", f"Không thể mã hóa file: {str(e)}")
    
    def giai_ma(self):
        # Cập nhật đường dẫn file đầu ra trước khi giải mã
        self.cap_nhat_link_file()
        
        if not self.ktra_file():
            return
        
        key = self.lay_khoa()
        if not key:
            return
        
        try:
            mode = self.encryption_mode.get()
            
            # Đọc file đã mã hóa
            with open(self.input_file_path, 'rb') as file:
                encrypted_data = file.read()
            
            self.status_var.set(f"Đang giải mã file {os.path.basename(self.input_file_path)}...")
            
            if mode == "ECB":
                # Tạo cipher DES
                cipher = DES.new(key, DES.MODE_ECB)
                # Giải mã dữ liệu và loại bỏ padding
                decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)
            else:  # CBC mode
                # Đọc IV từ 8 byte đầu tiên của file
                iv = encrypted_data[:8]
                encrypted_data = encrypted_data[8:]  # Phần còn lại là dữ liệu đã mã hóa
                
                # Hiển thị IV đã đọc từ file
                iv_b64 = base64.b64encode(iv).decode('utf-8')
                self.iv_var.set(iv_b64)
                self.iv = iv
                
                # Tạo cipher với IV đã đọc
                cipher = DES.new(key, DES.MODE_CBC, iv)
                # Giải mã dữ liệu và loại bỏ padding
                decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)
            
            # Ghi dữ liệu đã giải mã ra file
            with open(self.output_file_path, 'wb') as file:
                file.write(decrypted_data)
            
            self.status_var.set(f"Đã giải mã thành công file: {os.path.basename(self.input_file_path)}")
            
            # Hiển thị kích thước file trước và sau khi giải mã
            encrypted_size = os.path.getsize(self.input_file_path)
            decrypted_size = os.path.getsize(self.output_file_path)
            size_before = self.dinh_dang_kich_thuoc(encrypted_size)
            size_after = self.dinh_dang_kich_thuoc(decrypted_size)
            
            messagebox.showinfo("Thành công", 
                f"Đã giải mã file thành công!\n\n"
                f"File đã mã hóa: {size_before}\n"
                f"File sau khi giải mã: {size_after}\n\n"
                f"Lưu tại: {self.output_file_path}")
            
        except Exception as e:
            self.status_var.set(f"Lỗi: {str(e)}")
            messagebox.showerror("Lỗi", f"Không thể giải mã file: {str(e)}")
    
    def ktra_file(self):
        # Kiểm tra file đầu vào
        if not self.input_file_path or not os.path.exists(self.input_file_path):
            messagebox.showerror("Lỗi", "Vui lòng chọn file đầu vào hợp lệ!")
            return False
        
        # Kiểm tra tên file đầu ra
        if not self.output_name_var.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập tên cho file đầu ra!")
            return False
        
        # Kiểm tra thư mục đầu ra
        if not self.output_path_var.get():
            messagebox.showerror("Lỗi", "Vui lòng chọn thư mục lưu file đầu ra!")
            return False
        
        # Kiểm tra đường dẫn đầy đủ của file đầu ra
        self.cap_nhat_link_file()
        
        # Kiểm tra xem file đầu ra đã tồn tại chưa
        if os.path.exists(self.output_file_path):
            response = messagebox.askyesno("Cảnh báo", 
                f"File {os.path.basename(self.output_file_path)} đã tồn tại. Bạn có muốn ghi đè không?")
            if not response:
                return False
        
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMaHoa(root)
    root.mainloop()
