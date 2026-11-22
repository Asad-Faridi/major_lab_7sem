
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Activity 1.1: Data Preparation
data = {
    'Size_cm': [7, 7.5, 6.8, 18, 19, 17.5, 8.5, 9, 8.2, 7.2],
    'Color_Intensity': [0.8, 0.75, 0.82, 0.6, 0.58, 0.62, 0.9, 0.88, 0.92, 0.78],
    'FruitType': [
        'Apple', 'Apple', 'Apple',
        'Banana', 'Banana', 'Banana',
        'Orange', 'Orange', 'Orange', 'Apple'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Select features and target
X = df[['Size_cm', 'Color_Intensity']]
y = df['FruitType']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Display training data
print("Training Features:\n", X_train.head())
print("\nTraining Fruit Types:\n", y_train.head())

# Activity 1.2: KNN Training

# Create KNN model with 3 neighbors
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X_train, y_train)

# Predict fruit types
y_pred = model.predict(X_test)

print("\nActual Fruit Types:\n", y_test.to_list())
print("\nPredicted Fruit Types:\n", y_pred)

# Calculate accuracy
accuracy = model.score(X_test, y_test)

print("\nModel Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")
