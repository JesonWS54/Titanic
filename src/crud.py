import pandas as pd
deleted_passenger_ids = []
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
        print("Đã thêm hành khách mới.")
        return pd.concat([data, new_row], ignore_index=True), True
    
    except ValueError as e:
        print("Lỗi nhập liệu:", e), False
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
    data_to_show = data[data["PassengerId"].isin(deleted_passenger_ids) == False]
    result = data_to_show[data_to_show["PassengerId"] == passenger_id]
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

    data_to_update = data[data["PassengerID"].isin(deleted_passenger_ids) == False]
    if passenger_id not in data_to_update["PassengerID"].values:
        print(f"Hành khách với ID {passenger_id} không tồn tại.")
        return data
    
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
                print("Đã cập nhật thông tin hành khách.")
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
        if passenger_id in deleted_passenger_ids:
            print(f"Hành khách với ID {passenger_id} đã bị xóa trước đó.")
            return data
        deleted_passenger_ids.append(passenger_id)
        print(f"Hành khách với ID {passenger_id} đã được xóa.")
    else:
        print(f"Hành khách với ID {passenger_id} không tồn tại.")

    return data



