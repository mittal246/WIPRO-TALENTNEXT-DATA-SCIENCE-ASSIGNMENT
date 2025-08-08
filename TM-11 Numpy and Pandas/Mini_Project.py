#1. Use Case:- Perform the outlier detection for the given dataset. eg:- datasetExample
# Perform the following task:- 
# 1. Load the data in dataframe
# 2. Detection of outliers

import pandas as pd


df = pd.read_csv("datasetExample.csv")

print("First 5 rows of dataset:")
print(df.head())

# 2. Outlier Detection using IQR method
def detect_outliers_iqr(dataframe):
    outlier_indices = {}
    for col in dataframe.select_dtypes(include='number').columns:
        Q1 = dataframe[col].quantile(0.25)
        Q3 = dataframe[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = dataframe[(dataframe[col] < lower_bound) | (dataframe[col] > upper_bound)]
        outlier_indices[col] = outliers.index.tolist()
        print(f"\nOutliers in '{col}':")
        print(outliers[[col]])
    return outlier_indices

outlier_dict = detect_outliers_iqr(df)
