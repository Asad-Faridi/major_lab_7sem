import pandas as pd
import numpy as np
# 1. Create simulated employee performance data
np.random.seed(42)
performance_scores = np.random.normal(
    loc=75,
    scale=10,
    size=100
)
# Add outliers
performance_scores[10] = 150
performance_scores[25] = -20
performance_scores[50] = 5
employee_df = pd.DataFrame({
    'EmployeeID': range(1, 101),
    'PerformanceScore': performance_scores.round(0)
})
# Display original data
print("Original Employee Performance Data (first 10 rows):")
print(employee_df.head(10))
print("\nOriginal Employee Performance Data (last 10 rows):")
print(employee_df.tail(10))

# 2. Calculate Q1 and Q3
Q1 = employee_df['PerformanceScore'].quantile(0.25)
Q3 = employee_df['PerformanceScore'].quantile(0.75)

# 3. Calculate IQR
IQR = Q3 - Q1

# 4. Calculate lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)


# 5. Identify outliers
outliers = employee_df[
    (employee_df['PerformanceScore'] < lower_bound) |
    (employee_df['PerformanceScore'] > upper_bound)
]

print("\nOutliers:")
print(outliers[['EmployeeID', 'PerformanceScore']])


# 6. Capping/Winsorization
employee_df.loc[
    employee_df['PerformanceScore'] > upper_bound,
    'PerformanceScore'
] = upper_bound

employee_df.loc[
    employee_df['PerformanceScore'] < lower_bound,
    'PerformanceScore'
] = lower_bound


# 7. Display PerformanceScore after capping
print("\nPerformance Scores after Capping:")
print(employee_df['PerformanceScore'])