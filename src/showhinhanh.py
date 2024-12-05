import os
from tkinter import Tk, Button
from PIL import Image, ImageTk

# Kiểm tra xem file ảnh có tồn tại không
file_path = r'C:\Dictionary\titanic_image.jpg'
if not os.path.exists(file_path):
    print(f"File {file_path} không tồn tại.")
else:
    print(f"File {file_path} tồn tại.")
    root = Tk()
    # Mở và hiển thị ảnh
    img_import = Image.open(file_path)  # Mở ảnh bằng Pillow
    resize = img_import.resize((300, 300), Image.LANCZOS)  # Resize ảnh
    img = ImageTk.PhotoImage(resize)

    # Tạo cửa sổ Tkinter và hiển thị ảnh
    hinh_anh = Button(root, text='', image=img)
    hinh_anh.image = img  # Lưu tham chiếu ảnh
    hinh_anh.place(x=30, y=60)

    root.mainloop()
