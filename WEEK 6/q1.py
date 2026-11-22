from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)

housing_df = housing.frame

print("California Housing Data (first 5 rows):\n",
      housing_df.head())

print("\nOriginal columns:\n",
      housing_df.columns)

# Select required features
selected_features_df = housing_df[
    ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population']
]

# Print selected data
print("\nSelected Features (first 5 rows):\n",
      selected_features_df.head())

# Print selected columns
print("\nSelected columns:\n",
      selected_features_df.columns)