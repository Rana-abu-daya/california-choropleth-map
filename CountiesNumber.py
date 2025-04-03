import pandas as pd

# Load full merged voter file
df = pd.read_csv("arab_voters_only.csv")

# Filter only Arab voters
# Group by City and count
city_counts = df.groupby("City").size().reset_index(name="arab_voter_count")

# Save to file
city_counts.to_csv("Muslim_voters_by_city.csv", index=False)
print("✅ Saved arab_voters_by_city.csv")
