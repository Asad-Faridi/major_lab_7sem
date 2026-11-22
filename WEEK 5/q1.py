import pandas as pd

# 1. Load the Titanic dataset
df = pd.read_csv("train.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# 2. Identify missing data
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# 3. Strategy 1: Remove the Cabin column
df = df.drop("Cabin", axis=1)

# 4. Strategy 2: Fill missing Age values with median
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# 5. Strategy 3: Fill missing Embarked values with mode
mode_embarked = df["Embarked"].mode()[0] # [0] extracts the actual value
df["Embarked"] = df["Embarked"].fillna(mode_embarked)

# 6. Verify remaining missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())