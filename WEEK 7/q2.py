
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Create dataset
temp = np.array([10, 15, 20, 25, 30, 12, 18, 23, 28, 32]).reshape(-1, 1)
kwh = np.array([50, 60, 75, 90, 105, 55, 70, 85, 95, 110])

# Split data into training and testing sets
X_train_elec, X_test_elec, y_train_elec, y_test_elec = train_test_split(
    temp, kwh, test_size=0.3, random_state=42
)

# Display training data
print("Electricity Consumption Data (X_train_elec):\n",
      X_train_elec[:5])
print("\nElectricity Consumption (y_train_elec):\n",
      y_train_elec[:5])

# Train the model
model = LinearRegression()
model.fit(X_train_elec, y_train_elec)

# Make predictions
y_pred_elec = model.predict(X_test_elec)
print("\nPredicted Electricity Consumption:\n", y_pred_elec)

# Calculate MSE
mse = mean_squared_error(y_test_elec, y_pred_elec)
print("\nMean Squared Error:", mse)

# Visualize training data and regression line
plt.scatter(X_train_elec, y_train_elec, color='blue', label='Actual Data')

# Sort temperatures so the regression line displays correctly
sorted_indices = np.argsort(X_train_elec[:, 0])
X_sorted = X_train_elec[sorted_indices]
y_sorted_pred = model.predict(X_sorted)

plt.plot(X_sorted, y_sorted_pred, color='red', label='Regression Line')

plt.xlabel('Temperature (°C)')
plt.ylabel('Electricity Consumption (kWh)')
plt.title('Temperature vs Electricity Consumption')
plt.legend()
plt.show()
