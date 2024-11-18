import pandas as pd

def load_data(filepath):
    """
    Đọc dữ liệu từ file CSV và trả về một DataFrame.
    
    Args:
        filepath (str): Đường dẫn tới file CSV.
    
    Returns:
        pandas.DataFrame: DataFrame chứa dữ liệu từ file.
    """
    try:
        data = pd.read_csv(filepath)
        print(f"Dữ liệu đã được tải thành công từ {filepath}")
        return data
    except FileNotFoundError:
        print(f"Không tìm thấy file tại: {filepath}")
    except pd.errors.EmptyDataError:
        print("File CSV trống!")
    except pd.errors.ParserError:
        print("Lỗi khi phân tích file CSV!")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi tải dữ liệu: {e}")

def save_data(data, filepath):
    """
    Lưu dữ liệu từ DataFrame vào file CSV.
    
    Args:
        data (pandas.DataFrame): DataFrame cần lưu.
        filepath (str): Đường dẫn lưu file CSV.
    """
    try:
        data.to_csv(filepath, index=False)
        print(f"Dữ liệu đã được lưu thành công tại {filepath}")
    except PermissionError:
        print(f"Không có quyền ghi file tại: {filepath}")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi lưu dữ liệu: {e}")

def get_summary(data):
    """
    Tạo báo cáo tổng quan về dữ liệu.
    
    Args:
        data (pandas.DataFrame): DataFrame cần tạo báo cáo.
    
    Returns:
        dict: Báo cáo tổng quan về dữ liệu.
    """
    try:
        summary = {
            "Số dòng": data.shape[0],
            "Số cột": data.shape[1],
            "Kiểu dữ liệu các cột": data.dtypes.to_dict(),
            "Số lượng giá trị trống (per column)": data.isnull().sum().to_dict(),
            "Số lượng giá trị duy nhất (per column)": data.nunique().to_dict(),
            "Các giá trị duy nhất (per column)": {col: data[col].unique().tolist() for col in data.columns},
            "Thống kê cơ bản": data.describe(include='all').to_dict()
        }
        print("Báo cáo tổng quan dữ liệu đã được tạo.")
        return summary
    except Exception as e:
        print(f"Đã xảy ra lỗi khi tạo báo cáo dữ liệu: {e}")
