import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
FILEPATH = "data/Titanic.csv"
def load(FILEPATH):
    try:
        return pd.read_csv(FILEPATH)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải dữ liệu: {e}")
        return pd.DataFrame()

def save(data, FILEPATH):
    try:
        data.to_csv(FILEPATH, index=False)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {e}")

# Hàm sắp xếp dữ liệu (tùy chọn cột)
# def sort_data():
#     global data
#     if data.empty:
#         messagebox.showerror("Lỗi", "Dữ liệu trống. Không thể sắp xếp.")
#         return
#     allowed_columns = ['PassengerId', 'Age', 'Name']  
#     available_columns = [col for col in allowed_columns if col in data.columns]

#     if not available_columns:
#         messagebox.showerror("Lỗi", "Không có cột hợp lệ để sắp xếp.")
#         return

#     sort_window = tk.Toplevel()
#     sort_window.title("Sắp xếp dữ liệu")

#     def sort_by_column(column_name):
#         try:
#             data.sort_values(by=[column_name], ascending=True, inplace=True) # sắp
#             save(data, FILEPATH)
#             messagebox.showinfo("Thông báo", f"Dữ liệu đã được sắp xếp theo '{column_name}' thành công!")
#             sort_window.destroy()
#         except Exception as e:
#             messagebox.showerror("Lỗi", f"Không thể sắp xếp dữ liệu: {e}")

#     # Giao diện chọn cột để sắp xếp
#     ttk.Label(sort_window, text="Chọn cột để sắp xếp:").pack(pady=10)
#     for column in available_columns:
#         ttk.Button(sort_window, text=f"Sắp xếp theo {column}", 
#                    command=lambda col=column: sort_by_column(col)).pack(pady=5)

#     sort_window.mainloop()
