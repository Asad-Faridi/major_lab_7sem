import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

# Simulated Churn Data
np.random.seed(0)

churn_data = pd.DataFrame({
    'MonthlyCharges': np.random.uniform(20, 100, 200),
    'DataUsageGB': np.random.uniform(10, 80, 200),
    'ContractYears': np.random.randint(1, 4, 200),
    'Churn': np.random.choice([0, 1], 200, p=[0.7, 0.3])
})

# Separate features and target
X = churn_data.drop('Churn', axis=1)
y = churn_data['Churn']

# Initialize Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Apply 5-Fold Cross-Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

# Print accuracy for each fold
print("Accuracy for each fold:")

for i, score in enumerate(scores):
    print(f"Fold {i+1}: {score:.4f}")

# Calculate average accuracy
average_accuracy = np.mean(scores)

print("\nAverage Accuracy:", average_accuracy)