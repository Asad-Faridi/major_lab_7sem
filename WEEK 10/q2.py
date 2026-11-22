import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

# Create synthetic data with some groupings
X_students = pd.DataFrame({
    'Study_Hours_Week': np.random.randint(5, 40, 50),
    'Sleep_Hours_Night': np.random.uniform(4, 9, 50).round(1)
})

# Add some patterns
X_students.loc[X_students['Study_Hours_Week'] > 30,
               'Sleep_Hours_Night'] = np.random.uniform(
                   4, 6, sum(X_students['Study_Hours_Week'] > 30)
               ).round(1)

X_students.loc[X_students['Study_Hours_Week'] < 10,
               'Sleep_Hours_Night'] = np.random.uniform(
                   7, 9, sum(X_students['Study_Hours_Week'] < 10)
               ).round(1)

# Display student data
print("\nStudent Habit Data (first 5 rows):\n")
print(X_students.head())

# Perform hierarchical clustering
Z = linkage(X_students, method='ward')

# Generate dendrogram
plt.figure(figsize=(12, 6))
dendrogram(Z)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Students")
plt.ylabel("Distance")
plt.show()

# Apply Agglomerative Clustering
model = AgglomerativeClustering(n_clusters=3, linkage='ward')
X_students['Cluster'] = model.fit_predict(X_students)

# Display clustered data
print("\nStudent Data with Clusters:\n")
print(X_students)

# Visualize clusters
plt.figure(figsize=(8, 5))

plt.scatter(
    X_students['Study_Hours_Week'],
    X_students['Sleep_Hours_Night'],
    c=X_students['Cluster'],
    cmap='viridis'
)

plt.xlabel("Study Hours per Week")
plt.ylabel("Sleep Hours per Night")
plt.title("Student Grouping using Hierarchical Clustering")
plt.show()