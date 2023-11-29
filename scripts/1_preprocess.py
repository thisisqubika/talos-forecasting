# data preprocessing

import pandas as pd
import os

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def handle_missing_values(data):
    # Handle missing values by filling or dropping them
    data.fillna(method='ffill', inplace=True)  # Forward fill missing values
    return data

def create_date_features(data):
    # Create time series features based on time series index
    data = data.copy()
    data['dayofweek'] = data.index.dayofweek
    data['quarter'] = data.index.quarter
    data['month'] = data.index.month
    data['year'] = data.index.year
    data['dayofyear'] = data.index.dayofyear
    data['dayofmonth'] = data.index.day
    data['weekofyear'] = data.index.isocalendar().week
    return data

def add_lag_features(data, feature_column, lag_days):
    # Create lag features for the specified number of days
    for lag in lag_days:
        data[f'lag_{lag}_days_{feature_column}'] = data[feature_column].shift(lag)
    return data

def add_rolling_mean(data, feature_column, window_sizes):
    # Calculate rolling means for the specified window sizes
    for window_size in window_sizes:
        data[f'rolling_mean_{window_size}_days_{feature_column}'] = data[feature_column].rolling(window_size).mean()
    return data


def feature_engineering(data, feature_column):
    lag_days = [1, 7, 14]  # Specify the lag days to include
    data = add_lag_features(data, feature_column, lag_days)

    window_sizes = [14, 28]  # Specify the window sizes for rolling means
    data = add_rolling_mean(data, feature_column, window_sizes)

    return data

    
def main():
    file_path = 'data/processed_confirmed_cases_us.csv'
    feature_column = 'cases'

    # Step 1: Load data
    time_series_data = load_data(file_path)

    # Step 2: Handle missing values
    time_series_data = handle_missing_values(time_series_data)

    # Step 3: Feature engineering (add more steps as needed)
    time_series_data_final = feature_engineering(time_series_data, feature_column)

    # Get the current working directory
    current_directory = os.getcwd()

    # Construct the absolute path for saving the file
    saved_file_path = os.path.join(current_directory, 'data/preprocessed_data.csv')

    # Save the preprocessed data to a new file
    time_series_data_final.to_csv(saved_file_path, index=False)


if __name__ == "__main__":
    main()    
