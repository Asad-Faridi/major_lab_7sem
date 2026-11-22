import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 1. Load Iris dataset
iris = load_iris(as_frame=True)
iris_df = iris.frame

print("Original Iris Data:")
print(iris_df.head())

# 2. Select the four numerical features
features = [
    'sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)'
]

# 3. Normalization using Min-Max Scaling
minmax_scaler = MinMaxScaler()

normalized_data = minmax_scaler.fit_transform(
    iris_df[features]
)

normalized_df = pd.DataFrame(
    normalized_data,
    columns=features
)

print("\nNormalized Data:")
print(normalized_df.head())

# 4. Standardization using Z-score Scaling
standard_scaler = StandardScaler()

standardized_data = standard_scaler.fit_transform(
    iris_df[features]
)

standardized_df = pd.DataFrame(
    standardized_data,
    columns=features
)

print("\nStandardized Data:")
print(standardized_df.head())