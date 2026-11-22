import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_circles
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# -----------------------------------
# Activity 2.1: Linearly Separable Data
# -----------------------------------

# Generate linearly separable data
X_linear, y_linear = make_classification(
    n_samples=100,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    random_state=4,
    class_sep=1.5
)

# Visualize linear data
plt.figure(figsize=(8, 5))
plt.scatter(
    X_linear[:, 0], X_linear[:, 1],
    c=y_linear, cmap='viridis', s=50
)
plt.title("Linearly Separable Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Train Logistic Regression
linear_model = LogisticRegression()
linear_model.fit(X_linear, y_linear)

# Make predictions
y_pred_linear = linear_model.predict(X_linear)

# Calculate accuracy
print("Linear Data Accuracy:",
      accuracy_score(y_linear, y_pred_linear))


# -----------------------------------
# Activity 2.2: Non-linearly Separable Data
# -----------------------------------

# Generate non-linearly separable data
X_nonlinear, y_nonlinear = make_circles(
    n_samples=100,
    noise=0.1,
    factor=0.5,
    random_state=1
)

# Visualize nonlinear data
plt.figure(figsize=(8, 5))
plt.scatter(
    X_nonlinear[:, 0], X_nonlinear[:, 1],
    c=y_nonlinear, cmap='plasma', s=50
)
plt.title("Non-linearly Separable Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Train Logistic Regression
nonlinear_model = LogisticRegression()
nonlinear_model.fit(X_nonlinear, y_nonlinear)

# Make predictions
y_pred_nonlinear = nonlinear_model.predict(X_nonlinear)

# Calculate accuracy
print("Non-linear Data Accuracy:",
      accuracy_score(y_nonlinear, y_pred_nonlinear))