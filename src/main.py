import crud
import data_cleaning
import visualization
import utils

def main():
    while True:
        print("\nChương trình phân tích dữ liệu Titanic")
        print("1. CRUD - Thêm, Đọc, Cập nhật, Xóa dữ liệu")
        print("2. Làm sạch và chuẩn hóa dữ liệu")
        print("3. Trực quan hóa dữ liệu")
        print("4. Thoát")
        choice = input("Chọn một tùy chọn: ")

        if choice == '1':
            crud_menu()  # Gọi hàm menu CRUD
        elif choice == '2':
            data_cleaning.clean_data()  # Gọi hàm làm sạch
        elif choice == '3':
            visualization.visualize_data()  # Gọi hàm trực quan hóa
        elif choice == '4':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
