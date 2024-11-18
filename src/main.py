import crud
import data_cleaning
import visualization
import utils

import pandas as pd
filepath = "data/Titanic.csv"
def crud_menu(filepath):
    data = utils.load_data(filepath)

    while True:
        print("\n=== MENU CRUD ===")
        print("1. Thêm hành khách mới")
        print("2. Hiển thị thông tin hành khách")
        print("3. Cập nhật thông tin hành khách")
        print("4. Xóa hành khách")
        print("5. Quay lại menu chính")

        choice = input("Chọn một tùy chọn: ")

        if choice == '1':
            data = crud.create_entry(data)
            utils.save_data(data, filepath) 
            print("Đã thêm hành khách mới.")
        
        elif choice == '2':
            passenger_id = int(input("Nhập ID hành khách: "))
            data = crud.read_entry(data, passenger_id)
        
        elif choice == '3':
            passenger_id = int(input("Nhập ID hành khách: "))
            data = crud.update_entry(data, passenger_id)
            utils.save_data(data, filepath)  
            print("Đã cập nhật thông tin hành khách.")
        
        elif choice == '4':
            passenger_id = int(input("Nhập ID hành khách: "))
            data = crud.delete_entry(data, passenger_id)
            utils.save_data(data, filepath)  
            print("Đã xóa hành khách.")
        
        elif choice == '5':
            print("Quay lại menu chính.")
            break
        
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")


def main():
    while True:
        print("\nChương trình phân tích dữ liệu Titanic")
        print("1. CRUD - Thêm, Đọc, Cập nhật, Xóa dữ liệu")
        print("2. Làm sạch và chuẩn hóa dữ liệu")
        print("3. Trực quan hóa dữ liệu")
        print("4. Thoát")
        choice = input("Chọn một tùy chọn: ")

        if choice == '1':
            crud_menu(filepath)  
        elif choice == '2':
            data_cleaning.clean_data(filepath)  
        elif choice == '3':
            visualization.visualize_data()  
        elif choice == '4':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()