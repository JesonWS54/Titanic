import pandas as pd
import numpy as np
def fill_mising_age(titanic_data):
    """Fills in missing age values based on the average age of each passenger class (Pclass).

    Args:
      titanic_data: DataFrame containing the Titanic data.

    Returns:
      Series containing the filled 'Age' column.
    """
    titanic_data['Age']=titanic_data.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.mean()))
    return titanic_data['Age']

def fill_missing_Embarked(titanic_data):
    """Fills in missing Embarked values with the most frequent value.

    Args:
      titanic_data: DataFrame containing the Titanic data.

    Returns:
      Series containing the filled 'Embarked' column.
    """
    most_frequent_value = titanic_data['Embarked'].mode()[0]
    titanic_data['Embarked'] = titanic_data['Embarked'].fillna(most_frequent_value)
    return titanic_data['Embarked']

def fill_missing_Cabin(titanic_data):
    """Fills in missing Cabin values with "Unknown".

    Args:
      titanic_data: DataFrame containing the Titanic data.

    Returns:
      Series containing the filled 'Cabin' column.
    """
    titanic_data['Cabin']=titanic_data['Cabin'].fillna('Unknown')
    return titanic_data['Cabin']

def fix_wrong_value_Fare(titanic_data):
    """Fixes Fare values equal to 0 by using the average Fare by Pclass and Family_size.

    Args:
      titanic_data: DataFrame containing the Titanic data.

    Returns:
      Series containing the fixed 'Fare' column.
    """
    titanic_data['Family_size']=titanic_data['SibSp']+titanic_data['Parch']
    average_fare_by_group = titanic_data[titanic_data['Fare'] > 0].groupby(['Pclass', 'Family_size'])['Fare'].mean()

    titanic_data.loc[(titanic_data['Fare'] == 0) & (titanic_data['Ticket'] != 'LINE'), 'Fare'] = (
    titanic_data.loc[(titanic_data['Fare'] == 0) & (titanic_data['Ticket'] != 'LINE')].apply(
        lambda row: average_fare_by_group.get((row['Pclass'], row['Family_size']), row['Fare']), axis=1
        )
    )
    return titanic_data['Fare']
def normalize_parentheses_to_quotes(titanic_data):
    """
    Replace parentheses with quotes in the 'Name' column of a DataFrame.

    Args:
        titanic_data (pd.DataFrame): A DataFrame containing a 'Name' column.

    Modifies:
        Replacing '(' and ')' with '"', and cleaning redundant patterns like '("' or '")'.
    """
    titanic_data['Name'] = titanic_data['Name'].apply(lambda name: name.replace('(', '"').
                                                      replace(')', '"').replace('("','"').replace('")','"'))

def clean_data(titanic_data):
    """Performs data cleaning steps for the Titanic DataFrame.

    Args:
      titanic_data: DataFrame containing the Titanic data.

    Returns:
      Cleaned DataFrame.
    """
    fill_mising_age(titanic_data)
    fill_missing_Embarked(titanic_data)
    fill_missing_Cabin(titanic_data)
    fix_wrong_value_Fare(titanic_data)
    normalize_parentheses_to_quotes(titanic_data)
    return titanic_data
def missing_values(titanic_data):
    """Prints the number of missing values for each column in the Titanic DataFrame.

    Args:
      titanic_data: DataFrame containing the Titanic data.
    """
    print(titanic_data.isnull().sum())
