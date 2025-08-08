#1. Perfrom data preprocessing on melb_data.csv dataset with statistical prespective and using pandas.
import pandas as pd


df = pd.read_csv("melb_data.csv")

print("----- First 5 Rows -----")
print(df.head())

print("\n----- Dataset Shape -----")
print(df.shape)

print("\n----- Dataset Info -----")
print(df.info())

print("\n----- Statistical Summary (Numerical) -----")
print(df.describe())

print("\n----- Statistical Summary (Categorical) -----")
print(df.describe(include=['object']))


# Example: Remove rows where Price <= 0
df = df[df['Price'] > 0]

# 3. Check missing values
print("\n----- Missing Values Count -----")
print(df.isnull().sum())
