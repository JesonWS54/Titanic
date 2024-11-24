import pandas as pd
from tkinter import ttk, messagebox, simpledialog
FILEPATH = "data/Titanic.csv"
def load_data(filepath):
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải dữ liệu: {e}")
        return pd.DataFrame()

data = load_data(FILEPATH)
def save_data(data, filepath):
    try:
        data.to_csv(filepath, index=False)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {e}")
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

def add():
        global data
        try:
            passenger_id = int(simpledialog.askstring("Thêm dữ liệu", "Nhập PassengerId:"))
            survived = int(simpledialog.askstring("Thêm dữ liệu", "Nhập Survived (0 hoặc 1):"))
            pclass = int(simpledialog.askstring("Thêm dữ liệu", "Nhập Pclass (1, 2, 3):"))
            name = simpledialog.askstring("Thêm dữ liệu", "Nhập Name:")
            sex = simpledialog.askstring("Thêm dữ liệu", "Nhập Sex (male/female):")
            age = float(simpledialog.askstring("Thêm dữ liệu", "Nhập Age:"))
            sibsp = int(simpledialog.askstring("Thêm dữ liệu", "Nhập SibSp:"))
            parch = int(simpledialog.askstring("Thêm dữ liệu", "Nhập Parch:"))
            ticket = simpledialog.askstring("Thêm dữ liệu", "Nhập Ticket:")
            fare = float(simpledialog.askstring("Thêm dữ liệu", "Nhập Fare:"))
            cabin = simpledialog.askstring("Thêm dữ liệu", "Nhập Cabin (có thể để trống):")
            embarked = simpledialog.askstring("Thêm dữ liệu", "Nhập Embarked (C, Q, S):")

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

def read():
        global data
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

def update():
    global data
    try:
        passenger_id = simpledialog.askinteger("Cập nhật thông tin", "Nhập Passenger ID:")
        if passenger_id not in data["PassengerId"].values:
            messagebox.showerror("Lỗi", "Hành khách không tồn tại.")
            return
        survival = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Survival (CANCE nếu không thay đổi):")
        pclass = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Sex (CANCE nếu không thay đổi):")
        name = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Name (CANCE nếu không thay đổi):")
        sex = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Sex (CANCE nếu không thay đổi):")
        age = simpledialog.askfloat("Cập nhật dữ liệu", "Nhập Age (CANCE nếu không thay đổi):")
        sibsp = simpledialog.askinteger("Cập nhật dữ liệu", "Nhập SibSp (CANCE nếu không thay đổi):")
        parch = simpledialog.askinteger("Cập nhật dữ liệu", "Nhập Parch (CANCE nếu không thay đổi):")
        ticket = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Ticket (CANCE nếu không thay đổi):")
        fare = simpledialog.askfloat("Cập nhật dữ liệu", "Nhập Fare (CANCE nếu không thay đổi):")
        cabin = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Cabin (CANCE nếu không thay đổi):")
        embarked = simpledialog.askstring("Cập nhật dữ liệu", "Nhập Embarked (CANCE nếu không thay đổi):")
            
        updated_data = update_entry(data, passenger_id,survival,pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked)
            
        if updated_data is not None:
            save_data(updated_data, FILEPATH)
            messagebox.showinfo("Thông báo", "Đã cập nhật thông tin hành khách.")
        else:
            messagebox.showerror("Lỗi", "Hành khách không tồn tại.")
    except Exception as e:
        messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {e}")

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
    
    if passenger_id in data["PassengerId"].values:
        if passenger_id in deleted_passenger_ids:
            deleted_passenger_ids.append(passenger_id)
            data = data[data["PassengerId"] != passenger_id])
            return data
    else:
        return data

def delete():
        global data
        try:
            passenger_id = simpledialog.askinteger("Xóa hành khách", "Nhập Passenger ID:")
            updated_data = delete_entry(data, passenger_id)
            
            if updated_data is not None:
                data = updated_data
                save_data(data, FILEPATH)
                messagebox.showinfo("Thông báo", "Đã xóa hành khách thành công.")
            else:
                messagebox.showerror("Lỗi", "Không thể xóa hành khách. Vui lòng kiểm tra lại ID.")

        except Exception as e:
            messagebox.showerror("Lỗi hệ thống", f"Đã xảy ra lỗi: {e}")



