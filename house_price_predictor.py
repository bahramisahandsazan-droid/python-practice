"""
House Price Predictor
A simple machine learning model that predicts house prices
based on area, number of rooms, and building age.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# --- Step 1: Load the data ---
data = {
    'area': [50, 60, 80, 100, 120, 150, 200, 90, 70, 110],
    'rooms': [1, 2, 2, 3, 3, 4, 5, 2, 2, 3],
    'age': [10, 5, 8, 3, 15, 2, 1, 20, 12, 6],
    'price': [500, 650, 800, 1100, 1000, 1800, 2500, 700, 600, 1200]
}
df = pd.DataFrame(data)
print('Dataset:')
print(df)
print()

# --- Step 2: Split features (X) and target (y) ---
X = df[['area', 'rooms', 'age']]
y = df['price']

# --- Step 3: Split into training and testing sets ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 4: Train the model ---
model = LinearRegression()
model.fit(X_train, y_train)

# --- Step 5: Evaluate the model ---
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f'Model trained. Mean Absolute Error on test data: {mae:.2f} million toman')
print()

# --- Step 6: Predict price for a new house ---
new_house = pd.DataFrame({'area': [95], 'rooms': [3], 'age': [7]})
predicted_price = model.predict(new_house)
print(f'Predicted price for a 95 sqm, 3-room, 7-year-old house: {predicted_price[0]:.2f} million toman')