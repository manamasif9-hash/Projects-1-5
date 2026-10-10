# import pandas as pd

# # Load the property dataset
# data = pd.read_csv("property_data.csv")

# # Check for missing values
# print("Missing values:")
# print(data.isnull().sum())

# # Check for zero or negative prices
# print("\nProperties with invalid prices:")
# print(data[data["Price"] <= 0])


# # Check for duplicate rows
# duplicates = data.duplicated().sum()

# print("Number of duplicate rows:", duplicates)

# # Remove duplicate rows
# data = data.drop_duplicates()

# # Check the new number of rows
# print("Number of rows after removing duplicates:", len(data))

# import pandas as pd

# # Load the property dataset
# data = pd.read_csv("property_data.csv")

# # Remove duplicate rows
# data = data.drop_duplicates()

# # Display all unique locations
# print("Unique locations:")
# print(data["Location"].unique())

# # Count the number of unique locations
# print("\nNumber of unique locations:")
# print(data["Location"].nunique())


# # Convert Location into separate 0/1 columns
# data_encoded = pd.get_dummies(data, columns=["Location"], dtype=int)

# Display the first 5 rows
# print(data_encoded.head())

# # Display the column names
# print("\nColumns after encoding:")
# print(data_encoded.columns)

# Separate features (X) and target (y)
# X = data_encoded.drop("Price", axis=1)
# y = data_encoded["Price"]

# # Display the features
# print("Features (X):")
# print(X.head())

# # Display the target
# print("\nTarget (y):")
# print(y.head())

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Load the property dataset
data = pd.read_csv("property_data.csv")

# Remove duplicate rows
data = data.drop_duplicates()

# Convert Location into numerical columns
data_encoded = pd.get_dummies(data, columns=["Location"], dtype=int)

# Separate features (X) and target (y)
X = data_encoded.drop("Price", axis=1)
y = data_encoded["Price"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Display the sizes
print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("Linear Regression model trained successfully!")
# Make predictions
y_pred = model.predict(X_test)

# Display actual and predicted prices
print("Actual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(y_pred)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)

print("\nMean Squared Error (MSE):")
print(mse)

from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)

print("\nR² Score:")
print(r2)

import numpy as np

rmse = np.sqrt(mse)

print("\nRoot Mean Squared Error (RMSE):")
print(rmse)

# Create 3 hypothetical properties
new_properties = pd.DataFrame({
    "Size_Marla": [5, 10, 7],
    "Bedrooms": [3, 5, 4],
    "Location": ["Eden Valley", "Eden Orchard", "Model City"]
})

# Encode the locations
new_properties_encoded = pd.get_dummies(
    new_properties,
    columns=["Location"],
    dtype=int
)

# Make sure new data has the same columns as training data
new_properties_encoded = new_properties_encoded.reindex(
    columns=X.columns,
    fill_value=0
)

# Predict prices
new_predictions = model.predict(new_properties_encoded)

# Display predictions
print("\nHypothetical Property Predictions:")

for i, prediction in enumerate(new_predictions, start=1):
    print(f"Property {i}: {prediction:,.2f} PKR")