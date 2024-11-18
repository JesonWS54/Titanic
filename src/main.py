import crud
import data_cleaning
import visualization
import utils

import pandas as pd
filepath = "data/Titanic.csv"
titanic_data=pd.read_csv(filepath)
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
             new_data, success = crud.create_entry(data)
            if success:
                data = new_data
                utils.save_data(data,filepath)
                print("Đã thêm hành khách mới.")
            else:
                print("Không thể thêm hành khách. Vui lòng kiểm tra lại nhập liệu.")
        
        elif choice == '2':
            ry:
                passenger_id = int(input("Nhập ID hành khách: "))
                crud.read_entry(data, passenger_id)
            except ValueError:
                print("ID hành khách phải là một số nguyên.")
        
        elif choice == '3':
            try:
                passenger_id = int(input("Nhập ID hành khách: "))
                data = crud.update_entry(data, passenger_id) 
            except ValueError:
                print("ID hành khách phải là một số nguyên.")
        
        elif choice == '4':
            try:
                passenger_id = int(input("Nhập ID hành khách: "))
                if passenger_id not in data["PassengerId"].values:
                    print(f"Lỗi: Hành khách với ID {passenger_id} không tồn tại.")
                else:
                    new_data = crud.delete_entry(data, passenger_id)
                    if new_data is not data:  
                        data = new_data
                        crud.save_data(data, filepath)
            except ValueError:
                print("Lỗi: ID hành khách phải là một số nguyên.")
        
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
            titanic_data_clean=data_cleaning.clean_data(titanic_data) 
            titanic_data_clean.to_csv('data/titanic_data_clean.csv', index=False, encoding='utf-8') 
        elif choice == '3':
            visualization.visualize_data()  
        elif choice == '4':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
