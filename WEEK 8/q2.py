import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Activity 2.1: Data Preparation
np.random.seed(42)

# Generate the number of suspicious keywords
keywords = np.random.randint(0, 10, 100)

# Higher keywords = higher spam probability
spam_prob = 1 / (1 + np.exp(-(keywords - 5)))

# Generate spam labels: 1 = Spam, 0 = Not Spam
is_spam = (np.random.rand(100) < spam_prob).astype(int)

# Create a DataFrame
df = pd.DataFrame({
    'NumSuspiciousKeywords': keywords,
    'IsSpam': is_spam
})

# Separate features and target
X = df[['NumSuspiciousKeywords']]
y = df['IsSpam']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Display the first five training records
print("Spam Detection Data (X_train head):\n", X_train.head())
print("\nSpam Target (y_train head):\n", y_train.head())

# Activity 2.2: Logistic Regression Training
# Create the Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict spam labels for test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nActual Values:\n", y_test.values)
print("\nPredicted Values:\n", y_pred)
print("\nAccuracy Score:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")


# Activity 2.3: Conceptual Decision Boundary
# Predict spam probabilities for keyword counts from 0 to 9
keyword_range = pd.DataFrame({
    'NumSuspiciousKeywords': np.arange(0, 10)
})

spam_probabilities = model.predict_proba(keyword_range)[:, 1]
# Plot predicted spam probabilities
plt.plot(
    keyword_range['NumSuspiciousKeywords'],
    spam_probabilities,
    marker='o'
)
# Show the 0.5 probability threshold
plt.axhline(y=0.5, linestyle='--', label='0.5 threshold')
plt.xlabel("Number of Suspicious Keywords")
plt.ylabel("Predicted Probability of Spam")
plt.title("Logistic Regression: Spam Detection")
plt.legend()
plt.grid(True)
plt.show()

# Display the learned decision boundary
boundary = -model.intercept_[0] / model.coef_[0][0]
print("\nDecision Boundary:", boundary, "suspicious keywords")
print("Below the boundary: predicted Not Spam (0)")
print("Above the boundary: predicted Spam (1)")
