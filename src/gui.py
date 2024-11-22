import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import utils
import crud
import data_cleaning
import visualization
import pandas as pd

# Đường dẫn tới file CSV
filepath = "data/Titanic.csv"
data = utils.load_data(filepath)  # Giữ trạng thái dữ liệu chung

# Hiển thị dữ liệu với phân trang
def display_data():
    global data
    data_window = tk.Toplevel()
    data_window.title("Hiển thị dữ liệu")
    data_window.geometry("800x600")

    tree = ttk.Treeview(data_window, columns=list(data.columns), show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    records_per_page = 20
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

    def add_entry():
        crud.create_entry(data)
        utils.save_data(data, filepath)
        messagebox.showinfo("Thông báo", "Đã thêm hành khách mới.")

    def read_entry():
        passenger_id = simpledialog.askinteger("Đọc dữ liệu", "Nhập Passenger ID:")
        result = crud.read_entry(data, passenger_id)
        if result is not None:
            info = "\n".join([f"{col}: {val}" for col, val in result.items()])
            messagebox.showinfo("Thông tin hành khách", info)
        else:
            messagebox.showerror("Lỗi", "Hành khách không tồn tại.")

    def update_entry():
        passenger_id = simpledialog.askinteger("Cập nhật dữ liệu", "Nhập Passenger ID:")
        crud.update_entry(data, passenger_id)
        utils.save_data(data, filepath)
        messagebox.showinfo("Thông báo", "Đã cập nhật thông tin hành khách.")

    def delete_entry():
        passenger_id = simpledialog.askinteger("Xóa dữ liệu", "Nhập Passenger ID:")
        crud.delete_entry(data, passenger_id)
        utils.save_data(data, filepath)
        messagebox.showinfo("Thông báo", "Đã xóa hành khách.")

    crud_window = tk.Toplevel()
    crud_window.title("Chức năng CRUD")
    crud_window.geometry("400x300")

    ttk.Button(crud_window, text="Thêm", command=add_entry).pack(pady=5)
    ttk.Button(crud_window, text="Đọc", command=read_entry).pack(pady=5)
    ttk.Button(crud_window, text="Cập nhật", command=update_entry).pack(pady=5)
    ttk.Button(crud_window, text="Xóa", command=delete_entry).pack(pady=5)

# Làm sạch dữ liệu
def clean_data_interface():
    global data
    data = data_cleaning.clean_data(data)
    utils.save_data(data, filepath)
    messagebox.showinfo("Thông báo", "Dữ liệu đã được làm sạch.")

# Trực quan hóa dữ liệu
def visualize_data_interface():
    global data
    visualization.visualize_data()

# Giao diện chính
def main_gui():
    root = tk.Tk()
    root.title("Chương trình phân tích dữ liệu Titanic")
    root.geometry("400x300")

    ttk.Button(root, text="Hiển thị dữ liệu", command=display_data).pack(pady=10)
    ttk.Button(root, text="Chức năng CRUD", command=crud_interface).pack(pady=10)
    ttk.Button(root, text="Làm sạch dữ liệu", command=clean_data_interface).pack(pady=10)
    ttk.Button(root, text="Trực quan hóa dữ liệu", command=visualize_data_interface).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
