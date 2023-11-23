# data preprocessing

import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def handle_missing_values(data):
    # Handle missing values by filling or dropping them
    data.fillna(method='ffill', inplace=True)  # Forward fill missing values
    return data

def create_features(data):
    """
    Create time series features based on time series index.
    """
    data = data.copy()
    data['dayofweek'] = data.index.dayofweek
    data['quarter'] = data.index.quarter
    data['month'] = data.index.month
    data['year'] = data.index.year
    data['dayofyear'] = data.index.dayofyear
    data['dayofmonth'] = data.index.day
    data['weekofyear'] = data.index.isocalendar().week
    return data
