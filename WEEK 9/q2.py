import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data for shapes
# Features: NumCorners, AspectRatio
# Target: 0 = Square, 1 = Circle

X_shapes = np.array([
    [4, 1.0], [4, 1.05], [4, 0.95],  # Squares
    [0, 1.0], [0, 1.1], [0, 0.9],     # Circles
    [4, 0.5], [0, 2.0]               # Noisy points
])

y_shapes = np.array([0, 0, 0, 1, 1, 1, 0, 1])

# Split dataset into training and testing
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_shapes, y_shapes, test_size=0.3, random_state=42
)

print("Shape Classification Data (X_train_s):\n", X_train_s)
print("\nShape Target (y_train_s):\n", y_train_s)

# Initialize MLPClassifier
mlp = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=500,
    random_state=42,
    solver='adam'
)

# Train the model
mlp.fit(X_train_s, y_train_s)

# Make predictions
y_pred_s = mlp.predict(X_test_s)

# Calculate accuracy
accuracy = accuracy_score(y_test_s, y_pred_s)

print("\nActual Output:", y_test_s)
print("Predicted Output:", y_pred_s)
print("Accuracy:", accuracy)