import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generate synthetic dataset
np.random.seed(0)

X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.5, 80)

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Plot original data
plt.figure(figsize=(8, 5))
plt.scatter(X_train, y_train, label='Training Data')
plt.scatter(X_test, y_test, label='Testing Data', alpha=0.6)
plt.title("Original Data")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# Activity 1.2: Underfitting using Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)

# Activity 1.3: Overfitting using Polynomial Regression (Degree 20)
poly_model = make_pipeline(
    PolynomialFeatures(degree=20),
    LinearRegression()
)

poly_model.fit(X_train, y_train)

y_pred_poly = poly_model.predict(X_test)

# Calculate Mean Squared Error
linear_error = mean_squared_error(y_test, y_pred_linear)
poly_error = mean_squared_error(y_test, y_pred_poly)

print("Linear Regression MSE:", linear_error)
print("Polynomial Regression MSE:", poly_error)

# Generate points for plotting curves
X_plot = np.linspace(0, 5, 300).reshape(-1, 1)

# Plot Linear Regression
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Original Data')
plt.plot(X_plot, linear_model.predict(X_plot),
         color='red', label='Linear Regression')
plt.title("Underfitting - Linear Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# Plot Polynomial Regression
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Original Data')
plt.plot(X_plot, poly_model.predict(X_plot),
         color='red', label='Polynomial Regression')
plt.title("Overfitting - Polynomial Regression (Degree 20)")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()