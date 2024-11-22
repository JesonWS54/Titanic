import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đường dẫn tới file CSV
FILEPATH = "data/Titanic.csv"

# Load dữ liệu
def load_data(filepath):
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải dữ liệu: {e}")
        return pd.DataFrame()

data = load_data(FILEPATH)

# Lưu dữ liệu
def save_data(data, filepath):
    try:
        data.to_csv(filepath, index=False)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {e}")

# Hiển thị dữ liệu với phân trang
def display_data():
    global data
    data_window = tk.Toplevel()
    data_window.title("Hiển thị dữ liệu")
    data_window.geometry("800x600")

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
        new_row = {col: simpledialog.askstring("Thêm dữ liệu", f"Nhập {col}:") for col in data.columns}
        data.loc[len(data)] = new_row
        save_data(data, FILEPATH)
        messagebox.showinfo("Thông báo", "Đã thêm hành khách mới.")

    def read_entry():
        passenger_id = simpledialog.askinteger("Đọc dữ liệu", "Nhập Passenger ID:")
        result = data[data["PassengerId"] == passenger_id]
        if not result.empty:
            info = "\n".join([f"{col}: {result.iloc[0][col]}" for col in result.columns])
            messagebox.showinfo("Thông tin hành khách", info)
        else:
            messagebox.showerror("Lỗi", "Hành khách không tồn tại.")

    def update_entry():
        passenger_id = simpledialog.askinteger("Cập nhật dữ liệu", "Nhập Passenger ID:")
        if passenger_id in data["PassengerId"].values:
            for col in data.columns:
                new_value = simpledialog.askstring("Cập nhật dữ liệu", f"Nhập {col} (bỏ qua để giữ nguyên):")
                if new_value:
                    data.loc[data["PassengerId"] == passenger_id, col] = new_value
            save_data(data, FILEPATH)
            messagebox.showinfo("Thông báo", "Đã cập nhật thông tin hành khách.")
        else:
            messagebox.showerror("Lỗi", "Hành khách không tồn tại.")

    def delete_entry():
        passenger_id = simpledialog.askinteger("Xóa dữ liệu", "Nhập Passenger ID:")
        if passenger_id in data["PassengerId"].values:
            data.drop(data[data["PassengerId"] == passenger_id].index, inplace=True)
            save_data(data, FILEPATH)
            messagebox.showinfo("Thông báo", "Đã xóa hành khách.")
        else:
            messagebox.showerror("Lỗi", "Hành khách không tồn tại.")

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
    data.dropna(inplace=True)
    save_data(data, FILEPATH)
    messagebox.showinfo("Thông báo", "Dữ liệu đã được làm sạch.")

# Trực quan hóa dữ liệu
def visualize_data_interface():
    global data

    def histogram():
        plt.figure(figsize=(10, 6))
        sns.histplot(data['Age'], bins=30, kde=True, color='blue', edgecolor='black')
        plt.title('Distribution of Passenger Age', fontsize=16, fontweight='bold')
        plt.xlabel('Age', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.show()

    def bar_chart_survival():
        plt.figure(figsize=(8, 6))
        survival_by_gender = data.groupby('Sex')['Survived'].mean() * 100
        sns.barplot(x=survival_by_gender.index, y=survival_by_gender.values, palette='viridis')
        plt.title('Survival Rate by Gender (%)', fontsize=16, fontweight='bold')
        plt.xlabel('Gender', fontsize=14)
        plt.ylabel('Survival Rate (%)', fontsize=14)
        plt.show()

    viz_window = tk.Toplevel()
    viz_window.title("Trực quan hóa dữ liệu")
    viz_window.geometry("400x300")

    ttk.Button(viz_window, text="Biểu đồ phân phối tuổi", command=histogram).pack(pady=10)
    ttk.Button(viz_window, text="Tỷ lệ sống sót theo giới tính", command=bar_chart_survival).pack(pady=10)

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
