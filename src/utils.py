import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
#load data
def load(filepath):
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải dữ liệu: {e}")
        return pd.DataFrame()

# Lưu dữ liệu
def save(data, filepath):
    try:
        data.to_csv(filepath, index=False)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {e}")

