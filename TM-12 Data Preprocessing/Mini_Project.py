#1. Use-Case: House Price Prediction
#Dataset used:- melb_data.csv
#Perform the follwing tasks:-
#1. Load the data in dataframe(Pandas)
#2. Handle inappropriate data
#3. Handle missing data
#4. Handle the categorical data

import pandas as pd
# 1. Load the data
df = pd.read_csv("melb_data.csv")
print("First 5 rows of dataset:")
print(df.head())

# 2. Handle inappropriate data
# Example: Remove rows with negative or zero price (if any)
df = df[df['Price'] > 0]

# 4. Handle categorical data
y = df['Price']
X = df.drop(['Price'], axis=1)