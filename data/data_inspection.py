import pandas as pd

# Load the data
data = pd.read_csv('census.csv')

# Inspect the first few rows
print(data.head())

# Check for leading/trailing spaces in column names
print(data.columns)

# Check for missing or irregular values
print(data.info())
