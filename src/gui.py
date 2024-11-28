import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_cleaning import clean_data
import visualization as vs
import crud as ld
from utils import load
from utils import save
# Đường dẫn tới file CSV
FILEPATH = "data/Titanic.csv"

# Load dữ liệu
def load_data(filepath):
    load(filepath)

data = load(FILEPATH)
# Lưu dữ liệu
def save_data(data, filepath):
    save(data, filepath)



# Hiển thị dữ liệu với phân trang
def display_data():
    global data
    data_window = tk.Toplevel()
    data_window.title("Hiển thị dữ liệu")
    
    # Đặt cửa sổ ở chế độ toàn màn hình
    data_window.state('zoomed') 

    # Frame chứa Treeview và Scrollbars
    frame = ttk.Frame(data_window)
    frame.pack(fill=tk.BOTH, expand=True)

    scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)

    tree = ttk.Treeview(
        frame, columns=list(data.columns), show="headings",
        yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set
    )
    scrollbar_y.config(command=tree.yview)
    scrollbar_x.config(command=tree.xview)

    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar_y.grid(row=0, column=1, sticky='ns')
    scrollbar_x.grid(row=1, column=0, sticky='ew')

    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    records_per_page = 30
    total_pages = (len(data) + records_per_page - 1) // records_per_page
    current_page = tk.IntVar(value=1)
    page_info = tk.StringVar()

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

    nav_frame = ttk.Frame(data_window)
    nav_frame.pack(fill=tk.X, side=tk.BOTTOM)

    ttk.Button(nav_frame, text="Trang trước", command=prev_page).pack(side=tk.LEFT, padx=5, pady=5)
    ttk.Label(nav_frame, textvariable=page_info).pack(side=tk.LEFT, padx=5, pady=5)
    ttk.Button(nav_frame, text="Trang tiếp", command=next_page).pack(side=tk.LEFT, padx=5, pady=5)

    load_page(current_page.get())


# Chức năng CRUD
def crud_interface():
    global data
    def add_passenger():
        global data
        data=ld.add(data)
    def read_passenger():
        global data
        ld.read(data)
    def update_passenger():
        global data
        ld.update(data)
    def delete_passenger():
        global data
        data=ld.delete(data)

    crud_window = tk.Toplevel()
    crud_window.title("Chức năng CRUD")
    crud_window.geometry("400x300")

    ttk.Button(crud_window, text="Thêm", command=add_passenger).pack(pady=5)
    ttk.Button(crud_window, text="Đọc", command=read_passenger).pack(pady=5)
    ttk.Button(crud_window, text="Cập nhật", command=update_passenger).pack(pady=5)
    ttk.Button(crud_window, text="Xóa", command=delete_passenger).pack(pady=5)

# Làm sạch dữ liệu
def clean_data_interface():
    global data
    clean_data(data)
    save_data(data, FILEPATH)
    messagebox.showinfo("Thông báo", "Dữ liệu đã được làm sạch.")

# Trực quan hóa dữ liệu
def visualize_data_interface():
    global data

    viz_window = tk.Toplevel()
    viz_window.title("Trực quan hóa dữ liệu")

    # Kích thước cửa sổ
    window_width = 600
    window_height = 500

    # Lấy kích thước màn hình
    screen_width = viz_window.winfo_screenwidth()
    screen_height = viz_window.winfo_screenheight()

    # Tính toán vị trí trung tâm
    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2

    # Đặt kích thước và vị trí cửa sổ
    viz_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    ttk.Button(viz_window, text="Biểu đồ phân phối tuổi", command=lambda: vs.Histogram(data)).pack(pady=10)
    ttk.Button(viz_window, text="Tỷ lệ sống sót theo giới tính", command=lambda: vs.Barchartsurvival(data)).pack(pady=10)
    ttk.Button(viz_window, text="Tỷ lệ sống sót theo tầng lớp vé", command=lambda: vs.Barchartticket(data)).pack(pady=10)
    ttk.Button(viz_window, text="Tỷ lệ sống sót theo theo tầng lớp vé và giới tính", command=lambda: vs.BarChartGenderSurvival(data)).pack(pady=10)
    ttk.Button(viz_window, text="Biểu đồ thể hiện số lượng người sống sót theo giá vé", command=lambda: vs.FareSurvivalmain(data)).pack(pady=10)
    ttk.Button(viz_window, text="Biểu đồ thể hiện số lượng người sống sót theo tuổi", command=lambda: vs.SurvivalByAge(data)).pack(pady=10)
    ttk.Button(viz_window, text="Biểu đồ thể hiện số lượng người sống sót theo tuổi và giới tính", command=lambda: vs.AgeGenderSurvival(data)).pack(pady=10)

# Giao diện chính
def main_gui():
    root = tk.Tk()
    root.title("Chương trình phân tích dữ liệu Titanic")

    # Kích thước cửa sổ
    window_width = 400
    window_height = 300

    # Lấy kích thước màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Tính toán vị trí trung tâm
    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2

    # Đặt kích thước và vị trí cửa sổ
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    ttk.Button(root, text="Hiển thị dữ liệu", command=display_data).pack(pady=10)
    
    ttk.Button(root, text="Làm sạch dữ liệu", command=clean_data_interface).pack(pady=10)
    ttk.Button(root, text="Chức năng CRUD", command=crud_interface).pack(pady=10)
    ttk.Button(root, text="Trực quan hóa dữ liệu", command=visualize_data_interface).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
