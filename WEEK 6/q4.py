import pandas as pd

# 1. Load ratings data
ratings_df = pd.read_csv(
    'u.data',
    sep='\t',
    header=None,
    names=['user_id', 'item_id', 'rating', 'timestamp']
)

# 2. Load movie information
movies_df = pd.read_csv(
    'u.item',
    sep='|',
    encoding='latin-1',
    header=None,
    usecols=[0, 1],
    names=['item_id', 'movie_title']
)

# 3. Calculate average rating and number of ratings
movie_aggregates = ratings_df.groupby('item_id').agg(
    avg_rating=('rating', 'mean'),
    num_ratings=('rating', 'count')
).reset_index()

# 4. Merge with movie titles
movie_stats_df = pd.merge(
    movies_df,
    movie_aggregates,
    on='item_id',
    how='inner'
)

# 5. Keep required columns
movie_stats_df = movie_stats_df[
    ['movie_title', 'avg_rating', 'num_ratings']
]

# 6. Sort by number of ratings
movie_stats_df = movie_stats_df.sort_values(
    by='num_ratings',
    ascending=False
)

# 7. Print top 10
print("Top 10 Most Rated Movies:")
print(movie_stats_df.head(10))