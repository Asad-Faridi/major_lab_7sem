import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Simulated Churn Data
np.random.seed(0)

churn_data = pd.DataFrame({
    'MonthlyCharges': np.random.uniform(20, 100, 200),
    'DataUsageGB': np.random.uniform(10, 80, 200),
    'ContractYears': np.random.randint(1, 4, 200),
    'Churn': np.random.choice([0, 1], 200, p=[0.7, 0.3])
})

X = churn_data.drop('Churn', axis=1)
y = churn_data['Churn']

print("Original Churn Data (first 5 rows):\n", churn_data.head())

# Activity 1.2: Train-Test Split (70%-30%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("\nTrain-Test Split:")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Activity 1.3: Train-Validation-Test Split (60%-20%-20%)

# First split: 80% training + validation, 20% testing
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Second split: 60% training, 20% validation
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42
)

print("\nTrain-Validation-Test Split:")
print("X_train shape:", X_train.shape)
print("X_val shape:", X_val.shape)
print("X_test shape:", X_test.shape)

print("\ny_train shape:", y_train.shape)
print("y_val shape:", y_val.shape)
print("y_test shape:", y_test.shape)