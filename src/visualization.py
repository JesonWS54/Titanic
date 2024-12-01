import matplotlib.pyplot as plt
import pandas as pd
from utils import load
from utils import save


file_path = 'data/Titanic.csv'
titanic_data = load(file_path)

# Biểu đồ phân phối tuổi (Histogram)

def Histogram(titanic_data):
    plt.figure(figsize=(10, 6))
    plt.hist(titanic_data['Age'].dropna(), bins=30, color='blue', edgecolor='black', alpha=0.7)
    plt.title('Distribution of Passenger Age', fontsize=16, fontweight='bold')
    plt.xlabel('Age', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.ylim(0, titanic_data['Age'].max())
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Biểu đồ tỷ lệ sống sót theo giới tính (Bar Chart)

def Barchartsurvival(titanic_data):

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

def Barchartticket(titanic_data):

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

def BarChartGenderSurvival(titanic_data):

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

 
def FareSurvivalmain(titanic_data):
    def plot_ticket_price_distribution(titanic_data):
        plt.figure(figsize=(10, 6))
        plt.hist(titanic_data['Fare'], bins=30, color='orange', edgecolor='black')
        plt.title('Number of Passengers by Ticket Price', fontsize=16, fontweight='bold')
        plt.xlabel('Ticket Price', fontsize=14)
        plt.ylabel('Number of Passengers', fontsize=14)
        plt.xlim(0, titanic_data['Fare'].max())
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
        
    def FareSurvival(titainc_data):
        survived = titanic_data[titanic_data['Survived'] == 1]['Fare']
        not_survived = titanic_data[titanic_data['Survived'] == 0]['Fare']

        plt.figure(figsize=(10, 6))
        plt.hist([survived, not_survived], bins=30, label=['Survived', 'Not Survived'], color=['green', 'red'], alpha=0.7)
        plt.title('Fare Distribution by Survival Status', fontsize=16, fontweight='bold')
        plt.xlabel('Fare', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.legend()
        plt.show()

    plot_ticket_price_distribution(titanic_data)
    FareSurvival(titanic_data)
    
#Biểu đồ thể hiện số lượng người sống sót theo tuổi
    
def SurvivalByAge(titanic_data):
    age_survival = titanic_data.groupby('Age')['Survived'].mean() * 100
    plt.figure(figsize=(10, 6))
    plt.plot(age_survival.index, age_survival.values, marker='o', color='purple', linestyle='-', alpha=0.7)
    plt.title('Survival Rate by Age', fontsize=16, fontweight='bold')
    plt.xlabel('Age', fontsize=14)
    plt.ylabel('Survival Rate (%)', fontsize=14)
    plt.grid(alpha=0.5)
    plt.show()

    
#Biểu đồ thể hiện số lượng người sống sót theo tuổi và giới tính

def AgeGenderSurvival(titanic_data):

    age_bins = [0, 18, 35, 50, 80]
    labels = ['0-17', '18-34', '35-49', '50+']
    titanic_data['AgeGroup'] = pd.cut(titanic_data['Age'], bins=age_bins, labels=labels)

    survival_rate = titanic_data.groupby(['AgeGroup', 'Sex'])['Survived'].mean().unstack() * 100

    survival_rate.plot(kind='bar', stacked=True, figsize=(12, 6), color=['skyblue', 'lightpink'], edgecolor='black')
    plt.title('Survival Rate by Age Group and Gender', fontsize=16, fontweight='bold')

    plt.xlabel('Age Group', fontsize=10)
    plt.ylabel('Survival Rate (%)', fontsize=14)
    plt.legend(title='Gender')
    plt.ylim([0, 150])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

