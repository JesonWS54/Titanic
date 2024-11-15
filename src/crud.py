import pandas as pd
def create_entry(data):
    """
    Thêm một hành khách mới vào DataFrame hiện tại.

    Args:
        data (pd.DataFrame): Dữ liệu hiện tại của hành khách (DataFrame).

    Returns:
        pd.DataFrame: DataFrame mới với hành khách vừa được thêm.
                      Nếu có lỗi nhập liệu, trả về DataFrame gốc.
    """
    try:
        new_entry = {
            "PassengerId": int(input("PassengerId: ")),
            "Survived": int(input("Survived (0 = không, 1 = có): ")),
            "Pclass": int(input("Pclass (1, 2, 3): ")),
            "Name": input("Name: "),
            "Sex": input("Sex (male/female): "),
            "Age": float(input("Age: ")),
            "SibSp": int(input("SibSp: ")),
            "Parch": int(input("Parch: ")),
            "Ticket": input("Ticket: "),
            "Fare": float(input("Fare: ")),
            "Cabin": input("Cabin (có thể để trống): "),
            "Embarked": input("Embarked (C, Q, S): ")
        }
        new_row = pd.DataFrame([new_entry])
        return pd.concat([data, new_row], ignore_index=True)
    
    except ValueError as e:
        print("Lỗi nhập liệu:", e)
        return data

def read_entry(data, passenger_id):
    """
    Tìm và hiển thị thông tin hành khách dựa trên PassengerId.

    Args:
        data (pd.DataFrame): Dữ liệu hiện tại của hành khách (DataFrame).
        passenger_id (int): ID của hành khách cần tìm.

    Returns:
        None: In thông tin hành khách nếu tồn tại,
              in thông báo nếu hành khách không tồn tại.
    """
    result = data[data["PassengerId"] == passenger_id]
    if not result.empty:
        print(result)  
    else:
        print("Hành khách không tồn tại.")  


def update_entry(data, passenger_id):
    """
    Cập nhật thông tin của hành khách dựa trên PassengerId.

    Args:
        data (pd.DataFrame): Dữ liệu hiện tại của hành khách (DataFrame).
        passenger_id (int): ID của hành khách cần cập nhật.

    Returns:
        pd.DataFrame: DataFrame đã được cập nhật.
                      Nếu PassengerId không tồn tại, trả về thông báo lỗi.
    """

    if passenger_id not in data["PassengerId"].values:
        return "Hành khách không tồn tại."
    
    print("Nhập thông tin cần cập nhật (bỏ qua nếu không muốn cập nhật):")
    for column in data.columns:
        if column == "PassengerId":
            continue
        new_value = input(f"{column}: ")
        if new_value:
            try:
                if data[column].dtype == 'int64':
                    data.loc[data["PassengerId"] == passenger_id, column] = int(new_value)
                elif data[column].dtype == 'float64':
                    data.loc[data["PassengerId"] == passenger_id, column] = float(new_value)
                else:
                    data.loc[data["PassengerId"] == passenger_id, column] = new_value
            except ValueError as e:
                print(f"Lỗi khi cập nhật {column}: {e}")
    return data

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
        return data[data["PassengerId"] != passenger_id].reset_index(drop=True)
    else:
        return "Hành khách không tồn tại."



