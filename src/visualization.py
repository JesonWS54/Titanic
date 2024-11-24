import matplotlib.pyplot as plt
import pandas as pd


file_path = 'Titanic.csv'
titanic_data = pd.read_csv(file_path)

# Biểu đồ phân phối tuổi (Histogram)
def Histogram():
    plt.figure(figsize=(10, 6))
    plt.hist(titanic_data['Age'].dropna(), bins=30, color='blue', edgecolor='black', alpha=0.7)
    plt.title('Distribution of Passenger Age', fontsize=16, fontweight='bold')
    plt.xlabel('Age', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.ylim(0, titanic_data['Age'].max())
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Biểu đồ tỷ lệ sống sót theo giới tính (Bar Chart)
def Barchartsurvival():
    plt.figure(figsize=(8, 6))
    survival_by_gender = titanic_data.groupby('Sex')['Survived'].mean() * 100
    plt.bar(survival_by_gender.index, survival_by_gender.values, color=['blue', 'pink'], edgecolor='black', alpha=0.7)
    plt.title('Survival Rate by Gender', fontsize=16, fontweight='bold')
    plt.xlabel('Gender', fontsize=14)
    plt.ylabel('Survival Rate (%)', fontsize=14)
    plt.ylim([0, 100])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Biểu đồ tỷ lệ sống sót theo tầng lớp vé (Bar Chart)
def Barchartticket():
    plt.figure(figsize=(8, 6))
    survival_by_pclass = titanic_data.groupby('Pclass')['Survived'].mean() * 100
    plt.bar(survival_by_pclass.index, survival_by_pclass.values, color=['green', 'orange', 'red'], edgecolor='black', alpha=0.7)
    plt.title('Survival Rate by Ticket Class', fontsize=16, fontweight='bold')
    plt.xlabel('Ticket Class', fontsize=14)
    plt.ylabel('Survival Rate (%)', fontsize=14)
    plt.xticks([1, 2, 3], ['1st', '2nd', '3rd'])
    plt.ylim([0, 100])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Biểu đồ tỷ lệ sống sót theo tầng lớp vé và giới tính (Bar Chart)
def BarChartGenderSurvival():
    plt.figure(figsize=(12, 6))
    survival_rate = titanic_data.groupby(['Pclass', 'Sex'])['Survived'].mean().unstack() * 100

    # Survival rate for males
    plt.subplot(1, 2, 1)
    plt.bar(survival_rate.index, survival_rate['male'], color='blue', edgecolor='black', alpha=0.7)
    plt.title('Survival Rate (Male)', fontsize=16, fontweight='bold')
    plt.xlabel('Ticket Class', fontsize=14)
    plt.ylabel('Survival Rate (%)', fontsize=14)
    plt.xticks([1, 2, 3], ['1st', '2nd', '3rd'])
    plt.ylim([0, 100])
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Survival rate for females
    plt.subplot(1, 2, 2)
    plt.bar(survival_rate.index, survival_rate['female'], color='pink', edgecolor='black', alpha=0.7)
    plt.title('Survival Rate (Female)', fontsize=16, fontweight='bold')
    plt.xlabel('Ticket Class', fontsize=14)
    plt.ylabel('Survival Rate (%)', fontsize=14)
    plt.xticks([1, 2, 3], ['1st', '2nd', '3rd'])
    plt.ylim([0, 100])
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

#Biểu đồ thể hiện số lượng người sống sót theo giá vé
def plot_ticket_price_distribution():
    plt.figure(figsize=(10, 6))
    plt.hist(titanic_data['Fare'], bins=30, color='orange', edgecolor='black')
    plt.title('Number of Passengers by Ticket Price', fontsize=16, fontweight='bold')
    plt.xlabel('Ticket Price', fontsize=14)
    plt.ylabel('Number of Passengers', fontsize=14)
    plt.xlim(0, titanic_data['Fare'].max())
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
def FareSurvival():
    survived = titanic_data[titanic_data['Survived'] == 1]['Fare']
    not_survived = titanic_data[titanic_data['Survived'] == 0]['Fare']

    plt.figure(figsize=(10, 6))
    plt.hist([survived, not_survived], bins=30, label=['Survived', 'Not Survived'], color=['green', 'red'], alpha=0.7)
    plt.title('Fare Distribution by Survival Status', fontsize=16, fontweight='bold')
    plt.xlabel('Fare', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.legend()
    plt.show()
    
#Biểu đồ thể hiện số lượng người sống sót theo tuổi
    
def SurvivalByAge():
    age_survival = titanic_data.groupby('Age')['Survived'].mean() * 100
    plt.figure(figsize=(10, 6))
    plt.plot(age_survival.index, age_survival.values, marker='o', color='purple', linestyle='-', alpha=0.7)
    plt.title('Survival Rate by Age', fontsize=16, fontweight='bold')
    plt.xlabel('Age', fontsize=14)
    plt.ylabel('Survival Rate (%)', fontsize=14)
    plt.grid(alpha=0.5)
    plt.show()

    
#Biểu đồ thể hiện số lượng người sống sót theo tuổi và giới tính
def AgeGenderSurvival():
    age_bins = [0, 18, 35, 50, 80]
    labels = ['0-17', '18-34', '35-49', '50+']
    titanic_data['AgeGroup'] = pd.cut(titanic_data['Age'], bins=age_bins, labels=labels)

    survival_rate = titanic_data.groupby(['AgeGroup', 'Sex'])['Survived'].mean().unstack() * 100

    survival_rate.plot(kind='bar', stacked=True, figsize=(12, 6), color=['skyblue', 'lightpink'], edgecolor='black')
    plt.title('Survival Rate by Age Group and Gender', fontsize=16, fontweight='bold')
    plt.xlabel('Age Group', fontsize=14)
    plt.ylabel('Survival Rate (%)', fontsize=14)
    plt.legend(title='Gender')
    plt.ylim([0, 100])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Call the function to display the charts
while True:
    print("Nhap vao bieu do muon hien thi:")
    print("0: Ket thuc!")
    print("1: Bieu do phan phoi tuoi")
    print("2: Bieu do ty le song sot theo gioi tinh")
    print("3: Bieu do ty le song sot theo tang lop ve")
    print("4: Bieu do ty le song sot theo tang lop ve va gioi tinh")
    print("5: Bieu do the hien so luong nguoi song sot theo gia ve")
    print("6: Bieu do the hien so luong nguoi song sot theo tuoi")
    print("7: Bieu do the hien ty le song sot theo tuoi va gioi tinh")
    choose = int(input("Nhap vao bieu do muon hien thi: "))
    while choose < 0 or choose > 7:
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
    elif choose == 4:
        BarChartGenderSurvival()
    elif choose == 5:
        plot_ticket_price_distribution()
        FareSurvival()
    elif choose == 6:
        SurvivalByAge()
    elif choose == 7:
        AgeGenderSurvival()
