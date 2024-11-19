import pandas as pd

def load_data(filepath):
    """
    Đọc dữ liệu từ file CSV và trả về một DataFrame.
    """
    try:
        data = pd.read_csv(filepath)
        print(f"Dữ liệu đã được tải thành công từ {filepath}")
        return data
    except FileNotFoundError:
        print(f"Không tìm thấy file tại: {filepath}")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi tải dữ liệu: {e}")

def save_data(data, filepath):
    """
    Lưu dữ liệu từ DataFrame vào file CSV.
    """
    try:
        data.to_csv(filepath, index=False)
        print(f"Dữ liệu đã được lưu thành công tại {filepath}")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi lưu dữ liệu: {e}")

def get_summary(data):
    """
    Tạo báo cáo tổng quan về dữ liệu.
    """
    try:
        summary = {
            "Số dòng": data.shape[0],
            "Số cột": data.shape[1],
            "Kiểu dữ liệu các cột": data.dtypes.to_dict(),
            "Số lượng giá trị trống (per column)": data.isnull().sum().to_dict(),
            "Thống kê cơ bản": data.describe(include='all').to_dict()
        }
        print("Báo cáo tổng quan dữ liệu đã được tạo.")
        return summary
    except Exception as e:
        print(f"Đã xảy ra lỗi khi tạo báo cáo dữ liệu: {e}")

def delete_passenger(data, filepath, passenger_id):
    """
    Xóa hành khách dựa trên PassengerId và cập nhật file CSV.
    
    Args:
        data (pandas.DataFrame): DataFrame chứa dữ liệu hành khách.
        filepath (str): Đường dẫn tới file CSV.
        passenger_id (int): ID của hành khách cần xóa.
    
    Returns:
        pandas.DataFrame: DataFrame sau khi xóa hành khách.
    """
    try:
        if passenger_id in data['PassengerId'].values:
            data = data[data['PassengerId'] != passenger_id]
            save_data(data, filepath)
            print(f"Hành khách với PassengerId = {passenger_id} đã được xóa.")
        else:
            print(f"Không tìm thấy hành khách với PassengerId = {passenger_id}.")
        return data
    except KeyError:
        print("Không tìm thấy cột 'PassengerId' trong dữ liệu.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi xóa hành khách: {e}")
