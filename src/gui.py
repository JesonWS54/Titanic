import os
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import visualization as vs
import crud as ld
from utils import load, save
from data_cleaning import clean_data
from PIL import ImageTk, Image

# Đường dẫn tới file CSV
FILEPATH = "data/Titanic.csv"
data = load(FILEPATH)

# Lưu dữ liệu
def save_data(data, filepath):
    save(data, filepath)

# Giao diện chính
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Phân tích dữ liệu Titanic")
        self.state("zoomed")  # Mở ở chế độ toàn màn hình

        # Bố cục: Chia thành 3 phần
        self.columnconfigure(0, weight=1)  # Phần bên trái (CHỨC NĂNG)
        self.columnconfigure(1, weight=2)  # Phần giữa (TÙY CHỌN)
        self.columnconfigure(2, weight=3)  # Phần bên phải (GIỚI THIỆU)

        # Tiêu đề cho từng phần
        self.create_headers()

        # Menu bên trái
        self.create_left_menu()

        # Khung giữa và bên phải
        self.center_frame = tk.Frame(self, bg="#A9A9A9")  # Màu xám đậm cho bảng TÙY CHỌN
        self.center_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.right_frame = tk.Frame(self, bg="white")  # Giữ màu trắng cho bảng GIỚI THIỆU
        self.right_frame.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

        # Hiển thị nội dung giới thiệu mặc định
        self.show_intro()
    def display_chart(self, chart_function):
        """Hiển thị biểu đồ bên phải."""
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.show_intro()  # Giữ phần giới thiệu

        # Vẽ biểu đồ
        fig = chart_function(data)
        canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    def create_headers(self):
        """Tạo tiêu đề cho từng phần."""
        header_left = tk.Label(self, text="CHỨC NĂNG", font=("Arial", 14, "bold"), anchor="center", bg="#4B0082", fg="white")
        header_left.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        header_center = tk.Label(self, text="TÙY CHỌN", font=("Arial", 14, "bold"), anchor="center", bg="#808080", fg="white")
        header_center.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        header_right = tk.Label(self, text="GIỚI THIỆU", font=("Arial", 14, "bold"), anchor="center", bg="white")
        header_right.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

    def create_left_menu(self):
        """Tạo menu chức năng bên trái."""
        left_menu = tk.Frame(self, bg="#4B0082")  # Màu tím đậm cho bảng CHỨC NĂNG
        left_menu.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Các nút chức năng căn đều
        ttk.Button(left_menu, text="Hiển thị dữ liệu", command=self.display_data).pack(fill=tk.X, pady=5)
        ttk.Button(left_menu, text="Trực quan hóa dữ liệu", command=self.show_visualization_options).pack(fill=tk.X, pady=5)
        ttk.Button(left_menu, text="Sắp xếp dữ liệu", command=self.show_sort_options).pack(fill=tk.X, pady=5)
        ttk.Button(left_menu, text="Chức năng CRUD", command=self.show_crud_options).pack(fill=tk.X, pady=5)
        ttk.Button(left_menu, text="Làm sạch dữ liệu", command=self.clean_data).pack(fill=tk.X, pady=5)

    def show_intro(self):
        """Hiển thị giới thiệu bên phải."""
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        intro_label = tk.Label(
            self.right_frame,
            text="Giới thiệu về tập dữ liệu Titanic",
            font=("Arial", 14, "bold"),
            anchor="center",
            bg="white",
        )
        intro_label.pack(pady=10)

        tk.Label(
            self.right_frame,
            text=(
                "Tập dữ liệu Titanic chứa thông tin về hành khách trên con tàu Titanic huyền thoại, "
                "bao gồm các đặc điểm như giới tính, độ tuổi, tầng lớp xã hội và tình trạng sống sót. "
                "Phân tích dữ liệu này giúp làm sáng tỏ các yếu tố ảnh hưởng đến khả năng sống sót, "
                "đồng thời cung cấp góc nhìn khoa học về sự kiện lịch sử nổi tiếng này."
            ),
            wraplength=500,
            justify="left",
            bg="white",
        ).pack(pady=10)
    def __init__(self):
        super().__init__()
        self.title("Phân tích dữ liệu Titanic")
        self.state("zoomed")  

        self.columnconfigure(0, weight=1)  
        self.columnconfigure(1, weight=2)  
        self.columnconfigure(2, weight=3)  

        self.create_headers()
        self.create_left_menu()

        self.center_frame = tk.Frame(self, bg="#A9A9A9")  
        self.center_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.right_frame = tk.Frame(self, bg="white")  
        self.right_frame.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

        self.show_intro()

    def display_chart(self, chart_function):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        
        self.show_intro()  

        fig = chart_function(data)
        canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_headers(self):
        header_left = tk.Label(self, text="CHỨC NĂNG", font=("Arial", 14, "bold"), anchor="center", bg="#4B0082", fg="white")
        header_left.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        header_center = tk.Label(self, text="TÙY CHỌN", font=("Arial", 14, "bold"), anchor="center", bg="#808080", fg="white")
        header_center.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        header_right = tk.Label(self, text="GIỚI THIỆU", font=("Arial", 14, "bold"), anchor="center", bg="white")
        header_right.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

    def create_left_menu(self):
        left_menu = tk.Frame(self, bg="#4B0082")  
        left_menu.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        ttk.Button(left_menu, text="Hiển thị dữ liệu", command=self.display_data).pack(fill=tk.X, pady=5)
        ttk.Button(left_menu, text="Trực quan hóa dữ liệu", command=self.show_visualization_options).pack(fill=tk.X, pady=5)
        ttk.Button(left_menu, text="Sắp xếp dữ liệu", command=self.show_sort_options).pack(fill=tk.X, pady=5)
        ttk.Button(left_menu, text="Chức năng CRUD", command=self.show_crud_options).pack(fill=tk.X, pady=5)
        ttk.Button(left_menu, text="Làm sạch dữ liệu", command=self.clean_data).pack(fill=tk.X, pady=5)

    def show_intro(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        intro_label = tk.Label(
            self.right_frame,
            text="Giới thiệu về tập dữ liệu Titanic",
            font=("Arial", 14, "bold"),
            anchor="center",
            bg="white",
        )
        intro_label.pack(pady=10)
        tk.Label(
            self.right_frame,
            text=(
                "Tập dữ liệu Titanic chứa thông tin về hành khách trên con tàu Titanic huyền thoại, "
                "bao gồm các đặc điểm như giới tính, độ tuổi, tầng lớp xã hội và tình trạng sống sót. "
                "Phân tích dữ liệu này giúp làm sáng tỏ các yếu tố ảnh hưởng đến khả năng sống sót, "
                "đồng thời cung cấp góc nhìn khoa học về sự kiện lịch sử nổi tiếng này."
            ),
            wraplength=500,
            justify="left",
            bg="white",
        ).pack(pady=10)
        file_path = r'C:\Titanic\titanic_image.jpg'  # Đảm bảo đường dẫn đúng với file ảnh của bạn
        if not os.path.exists(file_path):
            print(f"File {file_path} không tồn tại.")
        else:
            print(f"File {file_path} tồn tại.")

            # Mở và hiển thị ảnh
            img_import = Image.open(file_path)  # Mở ảnh bằng Pillow
            resize = img_import.resize((300, 300), Image.LANCZOS)  # Resize ảnh
            img = ImageTk.PhotoImage(resize)

            # Tạo nút với ảnh
            label_img = tk.Label(self.right_frame, image=img)
            label_img.image = img  # Lưu tham chiếu ảnh
            label_img.pack(pady=10)
    def display_data(self):
        def load_page(page):
            tree.delete(*tree.get_children())
            start = (page - 1) * records_per_page
            end = min(start + records_per_page, len(data))
            for _, row in data.iloc[start:end].iterrows():
                tree.insert("", tk.END, values=list(row))
            page_info.set(f"Trang {page}/{total_pages}")

        def prev_page():
            if current_page.get() > 1:
                current_page.set(current_page.get() - 1)
                load_page(current_page.get())

        def next_page():
            if current_page.get() < total_pages:
                current_page.set(current_page.get() + 1)
                load_page(current_page.get())

        data_window = tk.Toplevel(self)
        data_window.title("Hiển thị dữ liệu")
        data_window.state("zoomed")

        records_per_page = 30
        total_pages = (len(data) + records_per_page - 1) // records_per_page
        current_page = tk.IntVar(value=1)
        page_info = tk.StringVar()

        tree = ttk.Treeview(data_window, columns=list(data.columns), show="headings")
        tree.pack(fill=tk.BOTH, expand=True)

        for col in data.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        nav_frame = ttk.Frame(data_window)
        nav_frame.pack(fill=tk.X, side=tk.BOTTOM)

        ttk.Button(nav_frame, text="Trang trước", command=prev_page).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Label(nav_frame, textvariable=page_info).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(nav_frame, text="Trang tiếp", command=next_page).pack(side=tk.LEFT, padx=5, pady=5)

        load_page(current_page.get())

    def show_crud_options(self):
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        ttk.Button(self.center_frame, text="Thêm", command=self.add_passenger).pack(fill=tk.X, pady=5)
        ttk.Button(self.center_frame, text="Đọc", command=self.read_passenger).pack(fill=tk.X, pady=5)
        ttk.Button(self.center_frame, text="Cập nhật", command=self.update_passenger).pack(fill=tk.X, pady=5)
        ttk.Button(self.center_frame, text="Xóa", command=self.delete_passenger).pack(fill=tk.X, pady=5)

    def show_visualization_options(self):
        for widget in self.center_frame.winfo_children():
            widget.destroy() 
        options = [
            ("Phân phối tuổi", vs.Histogram),
            ("Tỷ lệ sống sót theo giới tính", vs.Barchartsurvival),
            ("Tỷ lệ sống sót theo tầng lớp vé", vs.Barchartticket),
            ("Tỷ lệ sống sót theo tầng lớp vé và giới tính", vs.BarChartGenderSurvival),
            ("Biểu đồ thể hiện số lượng người sống sót theo giá vé", vs.FareSurvivalmain),
            ("Biểu đồ thể hiện số lượng người sống sót theo tuổi", vs.SurvivalByAge),
            ("Biểu đồ thể hiện số lượng người sống sót theo tuổi và giới tính", vs.AgeGenderSurvival),
        ]

        for text, func in options:
            ttk.Button(self.center_frame, text=text, command=lambda f=func: self.display_chart(f)).pack(fill=tk.X, pady=5)

    def show_sort_options(self):
        """Hiển thị các tùy chọn sắp xếp dữ liệu."""
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        ttk.Button(self.center_frame, text="Sắp xếp theo PassengerId", command=lambda: self.sort_data('PassengerId')).pack(fill=tk.X, pady=5)
        ttk.Button(self.center_frame, text="Sắp xếp theo Age", command=lambda: self.sort_data('Age')).pack(fill=tk.X, pady=5)
        ttk.Button(self.center_frame, text="Sắp xếp theo Name", command=lambda: self.sort_data('Name')).pack(fill=tk.X, pady=5)

    def sort_data(self, column_name):
        try:
            data.sort_values(by=[column_name], ascending=True, inplace=True)  # Sắp xếp dữ liệu
            save_data(data, FILEPATH)
            messagebox.showinfo("Thông báo", f"Dữ liệu đã được sắp xếp theo '{column_name}' thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể sắp xếp dữ liệu: {e}")

    def add_passenger(self):
        ld.add(data)

    def read_passenger(self):
        ld.read(data)

    def update_passenger(self):
        ld.update(data)

    def delete_passenger(self):
        ld.delete(data)

    def clean_data(self):
        global data
        clean_data(data)
        save_data(data, FILEPATH)
        messagebox.showinfo("Thông báo", "Dữ liệu đã được làm sạch.")

# Chạy chương trình
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
