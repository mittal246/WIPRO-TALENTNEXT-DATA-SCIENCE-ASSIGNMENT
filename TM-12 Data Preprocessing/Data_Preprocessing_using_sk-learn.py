#1. Perfrom data preprocessing on melb_data.csv dataset with statistical prespective and using sklearn .

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 1. Load the dataset
df = pd.read_csv("melb_data.csv")

print("----- First 5 Rows -----")
print(df.head())

print("\n----- Dataset Shape -----")
print(df.shape)

print("\n----- Dataset Info -----")
print(df.info())

# 2. Handle inappropriate data
# Example: remove rows with invalid prices
df = df[df['Price'] > 0]

# Separate target and features (assuming Price is the target)
y = df['Price']
X = df.drop(['Price'], axis=1)

# 3. Identify numerical & categorical columns
num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = X.select_dtypes(include=['object']).columns

# 4. Preprocessing for numerical features (statistical handling)
num_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median'))  # median is robust against outliers
])

# 5. Preprocessing for categorical features
cat_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # mode for categorical
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# 6. Combine preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_pipeline, num_cols),
        ('cat', cat_pipeline, cat_cols)
    ]
)

# 7. Apply preprocessing
X_clean = preprocessor.fit_transform(X)

print("\n----- Preprocessing Done -----")
print(f"Final transformed feature matrix shape: {X_clean.shape}")

# 8. Save cleaned features (optional)
# Convert back to DataFrame with feature names
feature_names = list(num_cols) + list(preprocessor.named_transformers_['cat']
                                      .named_steps['onehot']
                                      .get_feature_names_out(cat_cols))
X_df_clean = pd.DataFrame(X_clean.toarray() if hasattr(X_clean, "toarray") else X_clean,
                          columns=feature_names)
X_df_clean['Price'] = y.values
X_df_clean.to_csv("melb_data_cleaned_sklearn.csv", index=False)

print("\nCleaned dataset saved as 'melb_data_cleaned_sklearn.csv'")
