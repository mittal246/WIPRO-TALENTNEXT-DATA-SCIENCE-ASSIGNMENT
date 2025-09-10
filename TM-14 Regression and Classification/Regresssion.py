#1. Predict the price of the car based on its features. Use appropriate evaluation metrics.
# Dataset- cars.csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv("cars.csv")

# Features & Target (assuming 'Price' is the target column)
X = data.drop("Price", axis=1)
y = data["Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

#2. Create a model that can predict the profit based on its features. Dataset- 50_startups.csv

data = pd.read_csv("50_startups.csv")

# One-hot encode categorical variables (e.g. 'State')
data = pd.get_dummies(data, drop_first=True)

# Features & Target
X = data.drop("Profit", axis=1)
y = data["Profit"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))
#3. Create a model that can predict the profit based on its features. Dataset- Salary_Data

data = pd.read_csv("Salary_Data.csv")

# Features & Target
X = data.drop("Salary", axis=1)
y = data["Salary"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))