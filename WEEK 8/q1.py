import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Activity 1.1: Data Preparation
# Create a dataset
data = {
    'Age': np.random.randint(20, 60, 100),
    'PurchaseFrequency': np.random.uniform(0.5, 5, 100).round(1),
    'RespondedToCampaign': np.random.choice(
        [0, 1], 100, p=[0.6, 0.4]
    )
}

# Make response dependent on age and purchase frequency
for i in range(100):
    if data['Age'][i] < 35 and data['PurchaseFrequency'][i] > 3:
        data['RespondedToCampaign'][i] = 1
    elif data['Age'][i] > 50 and data['PurchaseFrequency'][i] < 1.5:
        data['RespondedToCampaign'][i] = 0

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Separate features and target
X = df[['Age', 'PurchaseFrequency']]
y = df['RespondedToCampaign']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training Data (X_train head):\n", X_train.head())
print("\nTraining Target (y_train head):\n", y_train.head())

# Activity 1.2: Decision Tree Training
# Create the Decision Tree classifier
model = DecisionTreeClassifier(max_depth=3, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict responses for test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nActual Values:\n", y_test.values)
print("\nPredicted Values:\n", y_pred)
print("\nAccuracy Score:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")


# Activity 1.3: Conceptual Understanding
print("\nActivity 1.3: Tree Splitting")
print("A Decision Tree selects the feature and threshold")
print("that divide the data into purer groups.")
print("It uses criteria such as Gini impurity or entropy.")
print("max_depth=3 limits the tree to 3 levels of decisions.")
