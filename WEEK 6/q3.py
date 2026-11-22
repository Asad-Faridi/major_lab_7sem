import pandas as pd

# Column names because adult.data has no header
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week',
    'native-country', 'income'
]

# Load the dataset
adult_df = pd.read_csv(
    'adult.data',
    header=None,
    names=column_names,
    skipinitialspace=True
)

print("\nAdult Income Data (first 5 rows):\n", adult_df.head())

# Define age bins
bins = [17, 30, 45, 60, adult_df['age'].max()]
labels = [
    'Young Adult',
    'Middle-Aged',
    'Senior Adult',
    'Elderly'
]

# Discretize age
adult_df['age_group'] = pd.cut(
    adult_df['age'],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Print unique values and their counts
print("\nAge Group Counts:")
print(adult_df['age_group'].value_counts())