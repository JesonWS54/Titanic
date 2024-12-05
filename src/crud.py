import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from utils import save
from utils import load
FILEPATH = "data/Titanic.csv"
# Load dữ liệu
def load_data(FILEPATH):
    load(FILEPATH)

# data = load(FILEPATH)
# # Lưu dữ liệu
def save_data(data, FILEPATH):
    save(data, FILEPATH)

deleted_passenger_ids = []
def create_entry(data, passenger_id, survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked):
    """
    Thêm một hành khách mới vào DataFrame hiện tại.

    Args:
        data (pd.DataFrame): Dữ liệu hiện tại của hành khách (DataFrame).
        passenger_id (int): ID của hành khách mới.
        survived (int): Tình trạng sống sót (0 = không, 1 = có).
        pclass (int): Hạng vé (1, 2, 3).
        name (str): Tên hành khách.
        sex (str): Giới tính (male/female).
        age (float): Tuổi.
        sibsp (int): Số anh chị em/bạn đời trên tàu.
        parch (int): Số cha mẹ/con đi cùng.
        ticket (str): Số vé.
        fare (float): Giá vé.
        cabin (str): Cabin (có thể để trống).
        embarked (str): Cảng lên tàu (C, Q, S).

    Returns:
        pd.DataFrame: DataFrame mới với hành khách vừa được thêm.
                      Nếu có lỗi nhập liệu, trả về DataFrame gốc.
    """
    try:
        new_entry = {
            "PassengerId": passenger_id,
            "Survived": survived,
            "Pclass": pclass,
            "Name": name,
            "Sex": sex,
            "Age": age,
            "SibSp": sibsp,
            "Parch": parch,
            "Ticket": ticket,
            "Fare": fare,
            "Cabin": cabin,
            "Embarked": embarked
        }
        new_row = pd.DataFrame([new_entry])
        return pd.concat([data, new_row], ignore_index=True), True
    
    except ValueError as e:
        return data, False

def add(data):
    add_window = tk.Toplevel()
    def submit_data(data):
        try:
            passenger_id = int(passenger_id_entry.get())
            if passenger_id in data["PassengerId"].values:
                messagebox.showerror("Lỗi", "PassengerId đã tồn tại!")
                return
            survived = int(survived_var.get())
            pclass = int(pclass_var.get())
            name = name_entry.get()
            sex = sex_var.get()
            age = float(age_entry.get())
            if age <= 0:
                messagebox.showerror("Lỗi", "Tuổi không được âm hoặc bằng 0")
                return
            sibsp = int(sibsp_entry.get())
            if sibsp < 0:
                messagebox.showerror("Lỗi", "Sibsp không được âm")
                return 
            parch = int(parch_entry.get())
            if parch < 0:
                messagebox.showerror("Lỗi", "Parch không được âm")
                return
            ticket = ticket_entry.get()
            fare = float(fare_entry.get())
            if fare < 0:
                messagebox.showerror("Lỗi", "Fare không được âm")
                return
            cabin = cabin_entry.get()
            embarked = embarked_var.get()
           
        
            data, success = create_entry(data, passenger_id, survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked)

            if success:
                save_data(data, FILEPATH)
                messagebox.showinfo("Thông báo", "Đã thêm hành khách mới.")
                add_window.destroy()
            else:
                messagebox.showerror("Lỗi", "Có lỗi xảy ra khi thêm hành khách.")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập đúng dữ liệu.")
        except Exception as e:
            messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {e}")
            return data
    add_window.title("Thêm hành khách mới")
    add_window.geometry("900x900")
    
    tk.Label(add_window, text="PassengerId:").pack(anchor="w")
    passenger_id_entry = tk.Entry(add_window)
    passenger_id_entry.pack(fill="x")
    tk.Label(add_window, text="Survived:").pack(anchor="w")
    survived_var = tk.IntVar(value='')
    ttk.Combobox(add_window, textvariable=survived_var, values=[0,1],state="readonly").pack(fill="x")
    tk.Label(add_window, text="Pclass:").pack(anchor="w")
    pclass_var = tk.IntVar(value='')
    ttk.Combobox(add_window, textvariable=pclass_var, values=[1, 2, 3], state="readonly").pack(fill="x")
    tk.Label(add_window, text="Name:").pack(anchor="w")
    name_entry = tk.Entry(add_window)
    name_entry.pack(fill="x")
    tk.Label(add_window, text="Sex:").pack(anchor="w")
    sex_var = tk.StringVar(value="")
    ttk.Combobox(add_window, textvariable=sex_var, values=["male", "female"], state="readonly").pack(fill="x")
    tk.Label(add_window, text="Age:").pack(anchor="w")
    age_entry = tk.Entry(add_window)
    age_entry.pack(fill="x")
    tk.Label(add_window, text="SibSp:").pack(anchor="w")
    sibsp_entry = tk.Entry(add_window)
    sibsp_entry.pack(fill="x")
    tk.Label(add_window, text="Parch:").pack(anchor="w")
    parch_entry = tk.Entry(add_window)
    parch_entry.pack(fill="x")
    tk.Label(add_window, text="Ticket:").pack(anchor="w")
    ticket_entry = tk.Entry(add_window)
    ticket_entry.pack(fill="x")
    tk.Label(add_window, text="Fare:").pack(anchor="w")
    fare_entry = tk.Entry(add_window)
    fare_entry.pack(fill="x")
    tk.Label(add_window, text="Cabin:").pack(anchor="w")
    cabin_entry = tk.Entry(add_window)
    cabin_entry.pack(fill="x")
    tk.Label(add_window, text="Embarked:").pack(anchor="w")
    embarked_var = tk.StringVar(value="")
    ttk.Combobox(add_window, textvariable=embarked_var, values=["C", "Q", "S"], state="readonly").pack(fill="x")
    tk.Button(add_window, text="Thêm", command=lambda: submit_data(data)).pack(pady=10)


    

def read_entry(data, passenger_id):
    """
    Tìm và hiển thị thông tin hành khách dựa trên PassengerId.

    Args:
        data (pd.DataFrame): Dữ liệu hiện tại của hành khách (DataFrame).
        passenger_id (int): ID của hành khách cần tìm.

    Returns:
        dict: Dictionary chứa thông tin hành khách nếu tìm thấy.
              None nếu không tìm thấy hành khách hoặc đã bị xóa.
    """
    result = data[data["PassengerId"] == passenger_id]
    if not result.empty:
        return result.iloc[0].to_dict()
    else:
        return None


def read(data):
        # global data
    try:
        passenger_id = simpledialog.askinteger("Đọc dữ liệu", "Nhập Passenger ID:")
        result = data[data["PassengerId"] == passenger_id]
        if not result.empty:
            info = "\n".join([f"{col}: {result.iloc[0][col]}" for col in result.columns])
            messagebox.showinfo("Thông tin hành khách", info)
        else:
            messagebox.showerror("Lỗi", "Hành khách không tồn tại.")
    except Exception as e:
        messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {e}")
  


def update_entry(data, passenger_id,survival=None, pclass=None, name=None, sex=None, age=None, sibsp=None, parch=None, ticket=None
                 , fare=None, cabin=None, embarked=None):
    """
    Cập nhật thông tin của hành khách dựa trên PassengerId.

    Args:
        data (pd.DataFrame): Dữ liệu hiện tại của hành khách (DataFrame).
        passenger_id (int): ID của hành khách cần cập nhật.
        name (str): Tên hành khách.
        sex (str): Giới tính (male/female).
        age (float): Tuổi.
        sibsp (int): Số anh chị em/bạn đời trên tàu.
        parch (int): Số cha mẹ/con đi cùng.
        ticket (str): Số vé.
        fare (float): Giá vé.
        cabin (str): Cabin (có thể để trống).
        embarked (str): Cảng lên tàu (C, Q, S).
        
    Returns:
        pd.DataFrame: DataFrame đã được cập nhật.
                      Nếu PassengerId không tồn tại, trả về thông báo lỗi.
    """

    if passenger_id not in data["PassengerId"].values:
        return None
    if survival is not None:
        data.loc[data["PassengerId"] == passenger_id, "Survived"] = survival
    if pclass is not None:
        data.loc[data["PassengerId"] == passenger_id, "Pclass"] = pclass
    if name is not None:
        data.loc[data["PassengerId"] == passenger_id, "Name"] = name
    if sex is not None:
        data.loc[data["PassengerId"] == passenger_id, "Sex"] = sex
    if age is not None:
        data.loc[data["PassengerId"] == passenger_id, "Age"] = age
    if sibsp is not None:
        data.loc[data["PassengerId"] == passenger_id, "SibSp"] = sibsp
    if parch is not None:
        data.loc[data["PassengerId"] == passenger_id, "Parch"] = parch
    if ticket is not None:
        data.loc[data["PassengerId"] == passenger_id, "Ticket"] = ticket
    if fare is not None:
        data.loc[data["PassengerId"] == passenger_id, "Fare"] = fare
    if cabin is not None:
        data.loc[data["PassengerId"] == passenger_id, "Cabin"] = cabin
    if embarked is not None:
        data.loc[data["PassengerId"] == passenger_id, "Embarked"] = embarked
    
    return data

def update(data):
    update_window = tk.Toplevel()
    update_window.attributes("-fullscreen", True)
    screen_width = update_window.winfo_screenwidth()
    screen_height = update_window.winfo_screenheight()
    exit_button = tk.Button(
        update_window, 
        text="Exit", 
        command=update_window.destroy, 
        font=("Arial", 10), 
        bg="red", 
        fg="white", 
        width=8, 
        height=1
    )
    exit_button.place(x=screen_width - 80, y=screen_height - 40)
    update_window.title("Cập nhật thông tin hành khách")
    update_window.geometry("900x900")
    def search_passenger():
        try:
            passenger_id = int(entry_passenger_id.get())
            passenger = data[data["PassengerId"] == passenger_id]
            
            if passenger.empty:
                messagebox.showerror("Lỗi", "Hành khách không tồn tại.")
                return
            entry_survival.delete(0, tk.END)
            entry_pclass.delete(0, tk.END)
            entry_name.delete(0, tk.END)
            entry_sex.delete(0, tk.END)
            entry_age.delete(0, tk.END)
            entry_sibsp.delete(0, tk.END)
            entry_parch.delete(0, tk.END)
            entry_ticket.delete(0, tk.END)
            entry_fare.delete(0, tk.END)
            entry_cabin.delete(0, tk.END)
            entry_embarked.delete(0, tk.END)

            entry_survival.insert(0, passenger["Survived"].values[0])
            entry_pclass.insert(0, passenger["Pclass"].values[0])
            entry_name.insert(0, passenger["Name"].values[0])
            entry_sex.insert(0, passenger["Sex"].values[0])
            entry_age.insert(0, passenger["Age"].values[0])
            entry_sibsp.insert(0, passenger["SibSp"].values[0])
            entry_parch.insert(0, passenger["Parch"].values[0])
            entry_ticket.insert(0, passenger["Ticket"].values[0])
            entry_fare.insert(0, passenger["Fare"].values[0])
            entry_cabin.insert(0, passenger["Cabin"].values[0])
            entry_embarked.insert(0, passenger["Embarked"].values[0])
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập ID hợp lệ.")
    
    def update_passenger():
        try:
            passenger_id = int(entry_passenger_id.get())
            if passenger_id not in data["PassengerId"].values:
                messagebox.showerror("Lỗi", "Hành khách không tồn tại.")
                return
            survival = entry_survival.get()
            pclass = entry_pclass.get()
            name = entry_name.get()
            sex = entry_sex.get()
            age = float(entry_age.get()) if entry_age.get() else None
            sibsp = int(entry_sibsp.get()) if entry_sibsp.get() else None
            parch = int(entry_parch.get()) if entry_parch.get() else None
            ticket = entry_ticket.get()
            fare = float(entry_fare.get()) if entry_fare.get() else None
            cabin = entry_cabin.get()
            embarked = entry_embarked.get()
            
            updated_data = update_entry(
                data,
                passenger_id,
                survival if survival != 'CANCEL' else None,
                pclass if pclass != 'CANCEL' else None,
                name if name != 'CANCEL' else None,
                sex if sex != 'CANCEL' else None,
                age if age is not None else None,
                sibsp if sibsp is not None else None,
                parch if parch is not None else None,
                ticket if ticket != 'CANCEL' else None,
                fare if fare is not None else None,
                cabin if cabin != 'CANCEL' else None,
                embarked if embarked != 'CANCEL' else None
            )
            if updated_data is not None:
                data.update(updated_data)
                save_data(updated_data, FILEPATH)
                messagebox.showinfo("Thông báo", "Đã cập nhật thông tin hành khách.")
                update_window.destroy()  # Đóng cửa sổ sau khi cập nhật thành công
            else:
                messagebox.showerror("Lỗi", "Hành khách không tồn tại.")
    
        except Exception as e:
            messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {e}")   
    tk.Label(update_window, text="Passenger ID:").pack(pady=2)
    entry_passenger_id = tk.Entry(update_window)
    entry_passenger_id.pack(pady=5)

    tk.Button(update_window, text="Tìm kiếm", command=search_passenger).pack(pady=3)

    tk.Label(update_window, text="Survived:").pack(pady=3)
    entry_survival = tk.Entry(update_window)
    entry_survival.pack(pady=5)

    tk.Label(update_window, text="Pclass:").pack(pady=3)
    entry_pclass = tk.Entry(update_window)
    entry_pclass.pack(pady=5)

    tk.Label(update_window, text="Name:").pack(pady=3)
    entry_name = tk.Entry(update_window)
    entry_name.pack(pady=5)

    tk.Label(update_window, text="Sex:").pack(pady=3)
    entry_sex = tk.Entry(update_window)
    entry_sex.pack(pady=5)

    tk.Label(update_window, text="Age:").pack(pady=3)
    entry_age = tk.Entry(update_window)
    entry_age.pack(pady=5)

    tk.Label(update_window, text="SibSp:").pack(pady=3)
    entry_sibsp = tk.Entry(update_window)
    entry_sibsp.pack(pady=5)

    tk.Label(update_window, text="Parch:").pack(pady=3)
    entry_parch = tk.Entry(update_window)
    entry_parch.pack(pady=5)

    tk.Label(update_window, text="Ticket:").pack(pady=3)
    entry_ticket = tk.Entry(update_window)
    entry_ticket.pack(pady=5)

    tk.Label(update_window, text="Fare:").pack(pady=3)
    entry_fare = tk.Entry(update_window)
    entry_fare.pack(pady=5)

    tk.Label(update_window, text="Cabin:").pack(pady=3)
    entry_cabin = tk.Entry(update_window)
    entry_cabin.pack(pady=5)

    tk.Label(update_window, text="Embarked:").pack(pady=3)
    entry_embarked = tk.Entry(update_window)
    entry_embarked.pack(pady=5)
    tk.Button(update_window, text="Cập nhật", command=update_passenger).pack(pady=10)

def delete_entry(data, passenger_id):
    """
    Xóa thông tin của một hành khách dựa trên PassengerId.

    Args:
        data (pd.DataFrame): Dữ liệu hiện tại của hành khách (DataFrame).
        passenger_id (int): ID của hành khách cần xóa.

    Returns:
        pd.DataFrame: DataFrame mới sau khi xóa hành khách.
                      Nếu PassengerId không tồn tại, trả về thông báo lỗi.
    """
    
    return data[~data["PassengerId"].isin(passenger_id)]

def delete(data):
    def confirm_delete():
        nonlocal data
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một hành khách để xóa.")
            return
        
        selected_ids = [int(tree.item(item, "values")[0]) for item in selected_items]
        data = delete_entry(data, selected_ids)
        save_data(data, FILEPATH)
        messagebox.showinfo("Thông báo", "Đã xóa hành khách thành công.")
        refresh_treeview()
    def refresh_treeview():
        for item in tree.get_children():
            tree.delete(item)
        for _, row in data.iterrows():
            tree.insert("", "end", values=(row["PassengerId"], row["Name"]))
    window = tk.Toplevel()
    window.title("Xóa hành khách")
    tree = ttk.Treeview(window, columns=("ID", "Name"), show="headings")
    tree.heading("ID", text="Passenger ID")
    tree.heading("Name", text="Name")
    tree.pack(fill="both", expand=True)
    refresh_treeview()
    delete_button = tk.Button(window, text="Xóa", command=confirm_delete)
    delete_button.pack(pady=10)
