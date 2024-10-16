# Data Anaysis with Pandas

import pandas as pd

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Step 2: Inspect the data
print("First few rows of the DataFrame:")
print(df.head())  # Display the first few rows

print("\nDataFrame info:")
print(df.info())  # Get basic information about the DataFrame

print("\nSummary statistics:")
print(df.describe())  # Get summary statistics

# Step 3: Calculate the average of the 'salary' column
average_salary = df['salary'].mean()
print(f"\nThe average salary is: {average_salary}")

