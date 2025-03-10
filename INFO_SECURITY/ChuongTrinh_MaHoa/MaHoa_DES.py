import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class DESEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mã Hóa Des")
        self.root.geometry("600x450")  # Tăng kích thước để chứa các tính năng mới
        self.root.resizable(False, False)
        
        self.key = None
        self.input_file_path = None
        self.output_file_path = None
        
        self.create_widgets()
        
    def create_widgets(self):
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
        
        browse_button = ttk.Button(input_frame, text="Duyệt...", command=self.browse_input_file)
        browse_button.grid(row=0, column=1, padx=5, pady=5)
        
        # Khóa mã hóa
        key_frame = ttk.LabelFrame(main_frame, text="Khóa mã hóa", padding=10)
        key_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=5)
        
        self.key_var = tk.StringVar()
        key_entry = ttk.Entry(key_frame, textvariable=self.key_var, width=50)
        key_entry.grid(row=0, column=0, padx=5, pady=5)
        
        key_button_frame = ttk.Frame(key_frame)
        key_button_frame.grid(row=0, column=1, padx=5, pady=5)
        
        generate_key_button = ttk.Button(key_button_frame, text="Tạo khóa", command=self.generate_key, width=10)
        generate_key_button.grid(row=0, column=0, padx=2)
        
        save_key_button = ttk.Button(key_button_frame, text="Lưu khóa", command=self.save_key, width=10)
        save_key_button.grid(row=0, column=1, padx=2)
        
        load_key_button = ttk.Button(key_button_frame, text="Tải khóa", command=self.load_key, width=10)
        load_key_button.grid(row=0, column=2, padx=2)
        
        # File đầu ra
        output_frame = ttk.LabelFrame(main_frame, text="File đầu ra", padding=10)
        output_frame.grid(row=3, column=0, columnspan=3, sticky="ew", pady=5)
        
        output_name_label = ttk.Label(output_frame, text="Tên file:")
        output_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.output_name_var = tk.StringVar()
        output_name_entry = ttk.Entry(output_frame, textvariable=self.output_name_var, width=30)
        output_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        self.output_path_var = tk.StringVar()
        output_entry = ttk.Entry(output_frame, textvariable=self.output_path_var, width=50)
        output_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        save_button = ttk.Button(output_frame, text="Chọn thư mục...", command=self.select_output_directory)
        save_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Nút thao tác
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=4, column=0, columnspan=3, pady=15)
        
        encrypt_button = ttk.Button(action_frame, text="Mã hóa", command=self.encrypt_file, width=15)
        encrypt_button.grid(row=0, column=0, padx=10)
        
        decrypt_button = ttk.Button(action_frame, text="Giải mã", command=self.decrypt_file, width=15)
        decrypt_button.grid(row=0, column=1, padx=10)
        
        # Thanh trạng thái
        self.status_var = tk.StringVar()
        self.status_var.set("Sẵn sàng")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=5, column=0, columnspan=3, sticky="ew", pady=10)
        
    def browse_input_file(self):
        filename = filedialog.askopenfilename(title="Chọn file cần mã hóa/giải mã")
        if filename:
            self.input_file_path = filename
            self.input_path_var.set(filename)
            
            # Tự động đề xuất tên file đầu ra
            base_name = os.path.basename(filename)
            file_name, file_ext = os.path.splitext(base_name)
            
            # Đề xuất tên file mới với suffix
            if not self.output_name_var.get():
                suggested_name = f"{file_name}_output{file_ext}"
                self.output_name_var.set(suggested_name)
    
    def select_output_directory(self):
        directory = filedialog.askdirectory(title="Chọn thư mục lưu file đầu ra")
        if directory:
            self.output_path_var.set(directory)
            
            # Cập nhật đường dẫn đầy đủ của file đầu ra
            self.update_output_file_path()
    
    def update_output_file_path(self):
        output_dir = self.output_path_var.get()
        output_name = self.output_name_var.get()
        
        if output_dir and output_name:
            self.output_file_path = os.path.join(output_dir, output_name)
    
    def generate_key(self):
        # DES yêu cầu khóa 8 byte (64 bit)
        self.key = get_random_bytes(8)
        # Hiển thị khóa ở dạng base64 cho người dùng
        key_b64 = base64.b64encode(self.key).decode('utf-8')
        self.key_var.set(key_b64)
        #messagebox.showinfo("Thông báo", "Đã tạo khóa ngẫu nhiên!")
    
    def save_key(self):
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
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể lưu khóa: {str(e)}")
    
    def load_key(self):
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
                    #messagebox.showinfo("Thành công", "Đã tải khóa thành công!")
                except:
                    messagebox.showerror("Lỗi", "File không chứa khóa hợp lệ!")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể đọc file: {str(e)}")
    
    def get_key(self):
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
    
    def encrypt_file(self):
        # Cập nhật đường dẫn file đầu ra trước khi mã hóa
        self.update_output_file_path()
        
        if not self.validate_inputs():
            return
        
        key = self.get_key()
        if not key:
            return
        
        try:
            # Đọc file đầu vào
            with open(self.input_file_path, 'rb') as file:
                data = file.read()
            
            # Đảm bảo dữ liệu là bội số của kích thước khối DES (8 bytes)
            padded_data = pad(data, DES.block_size)
            
            # Tạo cipher DES
            cipher = DES.new(key, DES.MODE_ECB)
            
            # Mã hóa dữ liệu
            encrypted_data = cipher.encrypt(padded_data)
            
            # Ghi dữ liệu đã mã hóa ra file
            with open(self.output_file_path, 'wb') as file:
                file.write(encrypted_data)
            
            self.status_var.set(f"Đã mã hóa thành công file: {os.path.basename(self.input_file_path)}")
            messagebox.showinfo("Thành công", f"Đã mã hóa file thành công và lưu tại: {self.output_file_path}")
            
        except Exception as e:
            self.status_var.set(f"Lỗi: {str(e)}")
            messagebox.showerror("Lỗi", f"Không thể mã hóa file: {str(e)}")
    
    def decrypt_file(self):
        # Cập nhật đường dẫn file đầu ra trước khi giải mã
        self.update_output_file_path()
        
        if not self.validate_inputs():
            return
        
        key = self.get_key()
        if not key:
            return
        
        try:
            # Đọc file đã mã hóa
            with open(self.input_file_path, 'rb') as file:
                encrypted_data = file.read()
            
            # Tạo cipher DES
            cipher = DES.new(key, DES.MODE_ECB)
            
            # Giải mã dữ liệu và loại bỏ padding
            decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)
            
            # Ghi dữ liệu đã giải mã ra file
            with open(self.output_file_path, 'wb') as file:
                file.write(decrypted_data)
            
            self.status_var.set(f"Đã giải mã thành công file: {os.path.basename(self.input_file_path)}")
            messagebox.showinfo("Thành công", f"Đã giải mã file thành công và lưu tại: {self.output_file_path}")
            
        except Exception as e:
            self.status_var.set(f"Lỗi: {str(e)}")
            messagebox.showerror("Lỗi", f"Không thể giải mã file: {str(e)}")
    
    def validate_inputs(self):
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
        self.update_output_file_path()
        
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = DESEncryptionApp(root)
    root.mainloop()