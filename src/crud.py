import pandas as pd
from tkinter import ttk, messagebox, simpledialog

from utils import save
from utils import load
FILEPATH = "data/Titanic.csv"
# Load dữ liệu
def load_data(filepath):
    load(filepath)

# data = load(FILEPATH)
# # Lưu dữ liệu
def save_data(data, filepath):
    save(data, filepath)

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
    # global data
    try:
        while True:
            passenger_id = int(simpledialog.askstring("Thêm dữ liệu", "Nhập PassengerId:"))
            if passenger_id in data["PassengerId"].values:
                    messagebox.showerror("Lỗi", "PassengerId đã tồn tại. Vui lòng nhập lại!")
            else:
                break
                
        while True:
            survived = int(simpledialog.askstring("Thêm dữ liệu", "Nhập Survived (0 hoặc 1):"))
            if survived not in [0,1]:
                messagebox.showerror("Lỗi", "Yêu cầu nhập lại 0 hoặc 1")
            else:
                break
        while True:
            pclass = int(simpledialog.askstring("Thêm dữ liệu", "Nhập Pclass (1, 2, 3):"))
            if pclass not in [1,2,3]:
                messagebox.showerror("Lỗi", "Yêu cầu nhập đúng!")
            else:
                break
        name = simpledialog.askstring("Thêm dữ liệu", "Nhập Name:")
        while True: 
            sex = simpledialog.askstring("Thêm dữ liệu", "Nhập Sex (male/female):")
            if sex.lower() not in ["male","female"]:
                messagebox.showerror("Lỗi", "Yêu cầu nhập đúng!")
            else:
                break
        while True:         
            age = float(simpledialog.askstring("Thêm dữ liệu", "Nhập Age:"))
            if age <= 0:
                messagebox.showerror("Lỗi", "Yêu cầu nhập đúng!")
            else:
                break
        sibsp = int(simpledialog.askstring("Thêm dữ liệu", "Nhập SibSp:"))
        parch = int(simpledialog.askstring("Thêm dữ liệu", "Nhập Parch:"))
        ticket = simpledialog.askstring("Thêm dữ liệu", "Nhập Ticket:")
        fare = float(simpledialog.askstring("Thêm dữ liệu", "Nhập Fare:"))
        cabin = simpledialog.askstring("Thêm dữ liệu", "Nhập Cabin (có thể để trống):")
        while True:
            embarked = simpledialog.askstring("Thêm dữ liệu", "Nhập Embarked (C, Q, S):")
            if embarked not in ["C","Q","S"]:
                messagebox.showerror("Lỗi", "Yêu cầu nhập đúng!")
            else:
                break
        data, success = create_entry(data, passenger_id, survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked)

        if success:
            save_data(data, FILEPATH)
            messagebox.showinfo("Thông báo", "Đã thêm hành khách mới.")
        else:
            messagebox.showerror("Lỗi", "Có lỗi xảy ra khi thêm hành khách.")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng dữ liệu.")
    except Exception as e:
        messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {e}")
    return data


    

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
    if passenger_id in deleted_passenger_ids:
        return None  
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
  


def update_entry(data, passenger_id,survival, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked):
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

    data_to_update = data[data["PassengerId"].isin(deleted_passenger_ids) == False]
    if passenger_id not in data_to_update["PassengerId"].values:
        return None
    if survival:
        data.loc[data["PassengerId"] == passenger_id, "Survived"] = survival
    if pclass:
        data.loc[data["PassengerId"] == passenger_id, "Pclass"] = pclass
    if name:
        data.loc[data["PassengerId"] == passenger_id, "Name"] = name
    if sex:
        data.loc[data["PassengerId"] == passenger_id, "Sex"] = sex
    if age:
        data.loc[data["PassengerId"] == passenger_id, "Age"] = age
    if sibsp:
        data.loc[data["PassengerId"] == passenger_id, "SibSp"] = sibsp
    if parch:
        data.loc[data["PassengerId"] == passenger_id, "Parch"] = parch
    if ticket:
        data.loc[data["PassengerId"] == passenger_id, "Ticket"] = ticket
    if fare:
        data.loc[data["PassengerId"] == passenger_id, "Fare"] = fare
    if cabin:
        data.loc[data["PassengerId"] == passenger_id, "Cabin"] = cabin
    if embarked:
        data.loc[data["PassengerId"] == passenger_id, "Embarked"] = embarked
    
    return data

def update(data):
    # global data

    try:
        passenger_id = simpledialog.askinteger("Cập nhật thông tin", "Nhập Passenger ID:")
        if passenger_id not in data["PassengerId"].values:
            messagebox.showerror("Lỗi", "Hành khách không tồn tại.")
            return
        survival = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Survival (CANCEL nếu không thay đổi):")
        pclass = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Pclass (CANCEL nếu không thay đổi):")
        name = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Name (CANCEL nếu không thay đổi):")
        sex = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Sex (CANCEL nếu không thay đổi):")
        age = simpledialog.askfloat("Cập nhật dữ liệu", "Nhập Age (CANCEL nếu không thay đổi):")
        sibsp = simpledialog.askinteger("Cập nhật dữ liệu", "Nhập SibSp (CANCEL nếu không thay đổi):")
        parch = simpledialog.askinteger("Cập nhật dữ liệu", "Nhập Parch (CANCEL nếu không thay đổi):")
        ticket = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Ticket (CANCEL nếu không thay đổi):")
        fare = simpledialog.askfloat("Cập nhật dữ liệu", "Nhập Fare (CANCEL nếu không thay đổi):")
        cabin = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Cabin (CANCEL nếu không thay đổi):")
        embarked = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Embarked (CANCEL nếu không thay đổi):")
            
        updated_data = update_entry(data, passenger_id,survival,pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked)
            
        if updated_data is not None:
            save_data(updated_data, FILEPATH)
            messagebox.showinfo("Thông báo", "Đã cập nhật thông tin hành khách.")
        else:
            messagebox.showerror("Lỗi", "Hành khách không tồn tại.")
    except Exception as e:
        messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {e}")

def delete_entry(data, passenger_ids):
    """
    Xóa thông tin của các hành khách dựa trên danh sách PassengerId.

    Args:
        data (pd.DataFrame): Dữ liệu hiện tại của hành khách (DataFrame).
        passenger_ids (list): Danh sách ID của hành khách cần xóa.

    Returns:
        pd.DataFrame: DataFrame mới sau khi xóa các hành khách.
    """
    try:
        passenger_ids_to_delete = [pid for pid in passenger_ids if pid in data["PassengerId"].values]
        
        if passenger_ids_to_delete:
            data = data[~data["PassengerId"].isin(passenger_ids_to_delete)].reset_index(drop=True)
        return data
    except Exception as e:
        raise ValueError(f"Lỗi trong quá trình xóa: {e}")

def delete():
    def perform_deletion():
        global data
        try:
            selected_indices = listbox.curselection()
            ids_to_delete = [id_list[i] for i in selected_indices]

            if not ids_to_delete:
                messagebox.showerror("Lỗi", "Vui lòng chọn ít nhất một hành khách.")
                return
            updated_data = delete_entry(data, ids_to_delete)

            if len(updated_data) < len(data): 
                data = updated_data
                save_data(data, FILEPATH)
                messagebox.showinfo("Thông báo", "Đã xóa thành công các hành khách.")
                delete_window.destroy() 
            else:
                messagebox.showerror("Lỗi", "Không tìm thấy ID hợp lệ để xóa.")
        except Exception as e:
            messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {e}")

    delete_window = tk.Toplevel()
    delete_window.title("Xóa hành khách")
    delete_window.geometry("400x300")

    tk.Label(delete_window, text="Danh sách hành khách (chọn để xóa):", font=("Arial", 12)).pack(pady=10)


    listbox = tk.Listbox(delete_window, selectmode=tk.MULTIPLE, font=("Arial", 10), width=50, height=15)
    listbox.pack(pady=10)

    id_list = data["PassengerId"].tolist()
    for idx, passenger_id in enumerate(id_list):
        name = data.loc[data["PassengerId"] == passenger_id, "Name"].values[0]
        listbox.insert(idx, f"ID: {passenger_id} - {name}")

    tk.Button(delete_window, text="Xóa", command=perform_deletion, bg="red", fg="white").pack(pady=10)







