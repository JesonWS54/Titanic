import pandas as pd
import numpy as np
def fill_missing_Age(data):
    """Fills in missing age values based on the average age of each passenger class (Pclass).

    Args:
      data: DataFrame containing the Titanic data.

    Returns:
      Series containing the filled 'Age' column.
    """
    data['Age']=data.groupby('Pclass')['Age'].transform(lambda x: x.fillna(int(x.mean())+0.5))
    return data['Age']

def fill_missing_Embarked(data):
    """Fills in missing Embarked values with the most frequent value.

    Args:
      data: DataFrame containing the Titanic data.

    Returns:
      Series containing the filled 'Embarked' column.
    """
    most_frequent_value = data['Embarked'].mode()[0]
    data['Embarked'] = data['Embarked'].fillna(most_frequent_value)
    return data['Embarked']

def fill_missing_Cabin(data):
    """Fills in missing Cabin values with "Unknown".

    Args:
      data: DataFrame containing the Titanic data.

    Returns:
      Series containing the filled 'Cabin' column.
    """
    data['Cabin']=data['Cabin'].fillna('Unknown')
    return data['Cabin']

def fix_wrong_value_Fare(data):
    """Fixes Fare values equal to 0 by using the average Fare by Pclass and Family_size.

    Args:
      data: DataFrame containing the Titanic data.

    Returns:
      Series containing the fixed 'Fare' column.
    """
    data['Family_size']=data['SibSp']+data['Parch']
    average_fare_by_group = data[data['Fare'] > 0].groupby(['Pclass', 'Family_size'])['Fare'].mean().round(3)

    data.loc[(data['Fare'] == 0) & (data['Ticket'] != 'LINE'), 'Fare'] = (
    data.loc[(data['Fare'] == 0) & (data['Ticket'] != 'LINE')].apply(
        lambda row: average_fare_by_group.get((row['Pclass'], row['Family_size']), row['Fare']), axis=1
        )
    )
    return data['Fare']
def normalize_parentheses_to_quotes(data):
    """
    Replace parentheses with quotes in the 'Name' column of a DataFrame.

    Args:
        data (pd.DataFrame): A DataFrame containing a 'Name' column.

    Modifies:
        Replacing '(' and ')' with '"', and cleaning redundant patterns like '("' or '")'.
    """
    data['Name'] = data['Name'].apply(lambda name: name.replace('(', '"').
                                                      replace(')', '"').replace('("','"').replace('")','"'))

def clean_data(data):
    """Performs data cleaning steps for the Titanic DataFrame.

    Args:
      data: DataFrame containing the Titanic data.

    Returns:
      Cleaned DataFrame.
    """
    fill_missing_Age(data)
    fill_missing_Embarked(data)
    fill_missing_Cabin(data)
    fix_wrong_value_Fare(data)
    normalize_parentheses_to_quotes(data)
    return data
def missing_values(data):
    """Prints the number of missing values for each column in the Titanic DataFrame.

    Args:
      data: DataFrame containing the Titanic data.
    """
    print(data.isnull().sum())
