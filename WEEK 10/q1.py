import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

# Create data for 3 groups: Small, Medium, Large
small_animals = np.random.normal(loc=[5, 20], scale=[1, 5], size=(20, 2))
medium_animals = np.random.normal(loc=[50, 80], scale=[10, 15], size=(20, 2))
large_animals = np.random.normal(loc=[300, 150], scale=[50, 25], size=(20, 2))

# Combine all animal data
X_animals = pd.DataFrame(
    np.vstack([small_animals, medium_animals, large_animals]),
    columns=['Weight_kg', 'Height_cm']
)

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_animals)

X_scaled_df = pd.DataFrame(X_scaled, columns=X_animals.columns)

print("Scaled Animal Data (first 5 rows):\n", X_scaled_df.head())

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled_df)

# Get cluster labels
X_animals['Cluster'] = kmeans.labels_

print("\nAnimal Data with Clusters:\n", X_animals)

# Get cluster centroids
centroids = scaler.inverse_transform(kmeans.cluster_centers_)

print("\nCluster Centroids:\n", centroids)

# Visualize clusters
plt.figure(figsize=(8, 5))

plt.scatter(
    X_animals['Weight_kg'],
    X_animals['Height_cm'],
    c=X_animals['Cluster'],
    cmap='viridis',
    label='Animals'
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    color='red',
    marker='X',
    s=200,
    label='Centroids'
)

plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.title('Animal Grouping using K-Means Clustering')
plt.legend()
plt.show()