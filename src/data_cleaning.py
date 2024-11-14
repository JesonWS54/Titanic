import pandas as pd
import numpy as np

def clean(titanic_data):
    # 1. Fill missing 'Age' values with the median age
    titanic_data['Age'].fillna(int(titanic_data['Age'].mean()) + 0.5, inplace=True)

    # 2. Fill missing 'Embarked' values with the mode (most common embarkation port)
    most_frequent_value = titanic_data['Embarked'].mode()[0]
    titanic_data['Embarked'].fillna(most_frequent_value, inplace=True)

    # 3. Fill missing 'Cabin' values with a placeholder ('Unknown')
    titanic_data['Cabin'].fillna('Unknown', inplace=True)

    # 4. Calculate the average fare by Pclass for fares greater than 0
    average_fare_by_class = titanic_data[titanic_data['Fare'] > 0].groupby('Pclass')['Fare'].mean()

    # 5. Replace 'Fare' values of 0 with the mean Fare of the corresponding Pclass
    titanic_data.loc[titanic_data['Fare'] == 0, 'Fare'] = titanic_data.loc[titanic_data['Fare'] == 0, 'Pclass'].map(average_fare_by_class)

    # 6. Replace 'LINE' in the 'Ticket' column with 'Unknown'
    titanic_data['Ticket'] = titanic_data['Ticket'].replace('LINE', 'Unknown')
    
    return titanic_data
