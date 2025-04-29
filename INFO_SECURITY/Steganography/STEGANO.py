#Tham khảo mạng và chat
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography - Giấu tin trong ảnh")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Variables
        self.image_path = None
        self.image_data = None
        self.display_image = None  # Store the PhotoImage object globally
        
        # Main image display
        self.image_frame = tk.Frame(root, bg="#d3d3d3", width=680, height=350)
        self.image_frame.place(x=60, y=30)
        self.image_frame.pack_propagate(False)  # Prevent frame from resizing to fit content
        
        self.image_label = tk.Label(self.image_frame, text="Chọn Ảnh", font=("Arial", 14), bg="#d3d3d3")
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Input message and image info section
        tk.Label(root, text="Nhập thông điệp", font=("Arial", 12)).place(x=90, y=395)
        self.message_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.message_entry.place(x=90, y=420, width=280, height=40)
        
        tk.Label(root, text="Thông tin trong ảnh", font=("Arial", 12)).place(x=430, y=395)
        self.hidden_text = tk.Entry(root, width=30, font=("Arial", 12), state="readonly")
        self.hidden_text.place(x=430, y=420, width=280, height=40)
        
        # Buttons
        self.hide_button = tk.Button(root, text="Giấu Tin", font=("Arial", 12), bg="#d3d3d3", 
                              command=self.hide_message)
        self.hide_button.place(x=175, y=500, width=100, height=40)
        
        self.select_button = tk.Button(root, text="Chọn ảnh", font=("Arial", 12), bg="#d3d3d3",
                                command=self.select_image)
        self.select_button.place(x=350, y=500, width=100, height=40)
        
        self.decode_button = tk.Button(root, text="Giải Tin", font=("Arial", 12), bg="#d3d3d3",
                               command=self.decode_message)
        self.decode_button.place(x=525, y=500, width=100, height=40)
        
        # Status bar
        self.status_label = tk.Label(root, text="Trạng thái: ", relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.place(x=90, y=560, width=620, height=25)
    
    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        
        if file_path:
            self.image_path = file_path
            self.update_image_display(file_path)
            self.status_label.config(text=f"Trạng thái: Đã chọn ảnh: {os.path.basename(file_path)}")
    
    def update_image_display(self, image_path):
        try:
            # Open image
            image = Image.open(image_path)
            self.image_data = image.copy()  # Store original image data
            
            # Calculate dimensions while maintaining aspect ratio
            display_width = 680
            display_height = 350
            
            # Get original dimensions
            width, height = image.size
            
            # Calculate ratio to fit in the frame
            ratio = min(display_width/width, display_height/height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            
            # Resize image for display
            display_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.display_image = ImageTk.PhotoImage(display_image)
            
            # Update label with new image
            self.image_label.config(image=self.display_image, text="", bg="#d3d3d3")
            self.image_label.place(relx=0.5, rely=0.5, anchor="center")
            
            # Force update display
            self.root.update_idletasks()
            
        except Exception as e:
            messagebox.showerror("Error", f"Không thể mở ảnh: {str(e)}")
            print(f"Image display error: {str(e)}")  # Debugging
    
    def hide_message(self):
        if not self.image_path:
            messagebox.showwarning("Thông báo", "Vui lòng chọn ảnh trước!")
            return
        
        message = self.message_entry.get()
        if not message:
            messagebox.showwarning("Thông báo", "Vui lòng nhập thông điệp để giấu!")
            return
        
        try:
            # Create a copy of the original image
            img = self.image_data.copy()
            
            # Convert message to binary
            binary_message = ''.join(format(ord(char), '08b') for char in message)
            binary_message += '1111111111111110'  # EOF marker
            
            # Check if the message can fit in the image
            if len(binary_message) > img.width * img.height * 3:
                messagebox.showerror("Lỗi", "Thông điệp quá dài cho ảnh này!")
                return
            
            data_index = 0
            
            # Loop through each pixel and modify the least significant bit
            for y in range(img.height):
                for x in range(img.width):
                    # Get pixel value at (x,y)
                    pixel = list(img.getpixel((x, y)))
                    
                    # Modify each color channel (RGB)
                    for color_channel in range(3):
                        if data_index < len(binary_message):
                            # Replace the least significant bit
                            pixel[color_channel] = pixel[color_channel] & ~1 | int(binary_message[data_index])
                            data_index += 1
                    
                    # Set the modified pixel
                    img.putpixel((x, y), tuple(pixel))
                    
                    # Check if we've encoded the entire message
                    if data_index >= len(binary_message):
                        break
                        
                if data_index >= len(binary_message):
                    break
            
            # Ask user where to save the image
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")],
                title="Lưu ảnh chứa thông điệp"
            )
            
            if save_path:
                img.save(save_path)
                messagebox.showinfo("Thành công", "Đã giấu thông điệp thành công!")
                self.status_label.config(text=f"Trạng thái: Đã giấu thông điệp và lưu ảnh tại {os.path.basename(save_path)}")
                
                # Update display with the new image that contains hidden message
                self.image_path = save_path
                self.update_image_display(save_path)
        
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi giấu thông điệp: {str(e)}")
            print(f"Hide message error: {str(e)}")  # Debugging
    
    def decode_message(self):
        if not self.image_path:
            messagebox.showwarning("Thông báo", "Vui lòng chọn ảnh trước!")
            return
        
        try:
            # Open the image
            img = self.image_data
            
            binary_message = ""
            found_eof = False
            max_bits = img.width * img.height * 3  # Maximum possible bits
            
            # Loop through each pixel and extract the least significant bit
            for y in range(img.height):
                if found_eof:
                    break
                    
                for x in range(img.width):
                    pixel = img.getpixel((x, y))
                    
                    # Extract from each color channel
                    for color_channel in range(3):
                        binary_message += str(pixel[color_channel] & 1)
                        
                        # Check for the EOF marker
                        if len(binary_message) >= 16 and binary_message[-16:] == '1111111111111110':
                            # Found EOF marker, remove it and stop extraction
                            binary_message = binary_message[:-16]
                            found_eof = True
                            break
                            
                        # Safety check to prevent infinite loops
                        if len(binary_message) >= max_bits:
                            found_eof = True
                            break
                    
                    if found_eof:
                        break
            
            # Convert binary message to text
            message = ""
            for i in range(0, len(binary_message), 8):
                if i + 8 <= len(binary_message):
                    byte = binary_message[i:i+8]
                    message += chr(int(byte, 2))
            
            # Display the message
            self.hidden_text.config(state="normal")
            self.hidden_text.delete(0, tk.END)
            self.hidden_text.insert(0, message)
            self.hidden_text.config(state="readonly")
            
            self.status_label.config(text=f"Trạng thái: Đã giải mã thông điệp thành công")
            
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi khi giải mã thông điệp: {str(e)}")
            print(f"Decode message error: {str(e)}")  # Debugging

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
