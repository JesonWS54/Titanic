
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = 'Titanic.csv'
titanic_data = pd.read_csv(file_path)
    # Set visual style
sns.set(style="whitegrid")
def visualize_data():
        # Biểu đồ phân phối tuổi (Histogram)
    def Histogram():
        plt.figure(figsize=(10, 6))
        sns.histplot(titanic_data['Age'], bins=30, kde=True, color='blue', edgecolor='black')
        plt.title('Distribution of Passenger Age', fontsize=16, fontweight = 'bold')
        plt.xlabel('Age', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.xlim([0,80])
        plt.ylim([0,80])
        plt.show()

        # Biểu đồ tỷ lệ sống sót theo giới tính (Bar Chart)
        
    def Barchartsurvival():
        plt.figure(figsize=(8, 6))
        survival_by_gender = titanic_data.groupby('Sex')['Survived'].mean()
        sns.barplot(x=survival_by_gender.index, y=survival_by_gender.values, palette='viridis')
        plt.title('Survival Rate by Gender', fontsize=16, fontweight = 'bold')
        plt.xlabel('Gender', fontsize=14)
        plt.ylabel('Survival Rate (%)', fontsize=14)
        plt.ylim([0,1])
        plt.show()

        # Biểu đồ tỷ lệ sống sót theo tầng lớp vé (Bar Chart)
    def Barchartticket():
        plt.figure(figsize=(8, 6))
        survival_by_pclass = titanic_data.groupby('Pclass')['Survived'].mean()
        sns.barplot(x = survival_by_pclass.index, y = survival_by_pclass.values, palette = 'muted')
        plt.title('Survival Rate by Ticket Class', fontsize = 16, fontweight = 'bold')
        plt.xlabel('Ticket Class', fontsize=14)
        plt.ylabel('Survival Rate (%)', fontsize=14)
        plt.ylim([0,1])
        plt.show()
    while True:
        print("Nhap vao bieu do muon hien thi:")
        print("0: Ket thuc! ")
        print("1: Bieu do phan phoi tuoi ")
        print("2: Bieu do ty le song sot theo gioi tinh")
        print("3: Bieu do ty le song sot theo tang lop ve")
        choose = int(input("Nhap vao bieu do muon hien thi:" ))
        while choose < 0 or choose > 3:
            choose = int(input("Nhap lai lua chon hop le: "))
        if choose == 0:
            print("Tam biet!")
            break
        elif choose == 1:
            Histogram()
        elif choose == 2:
            Barchartsurvival()
        elif choose == 3:
            Barchartticket()
            











        
