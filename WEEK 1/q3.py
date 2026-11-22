log1_events = ["A101", "B202", "C303", "A101", "D404"]
log2_events=["C303","E505","F606","B202"]
log1=set(log1_events)
log2=set(log2_events)
print(log1)
print(log1.intersection(log2))
print(log1.union(log2))