import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data.csv")

# Features (X) and Target (y)
X = data[['Area', 'Bedrooms', 'Age']]
y = data['Price']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Take user input
area = int(input("Enter area (sq ft): "))
bedrooms = int(input("Enter number of bedrooms: "))
age = int(input("Enter age of house: "))

# Predict price
predicted_price = model.predict([[area, bedrooms, age]])

print("Predicted House Price:", int(predicted_price[0]))
