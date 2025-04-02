import pandas as pd

# Load the merged data
df = pd.read_csv("VoterRegistrationDataArabicClassified.csv")

# Filter only rows where is_arabic == "Arabic"
arab_only_df = df[df['is_arabic'] == "Arabic"]
print(arab_only_df)
# Group by CountyCode and count the number of Arabic voters
arab_counts = arab_only_df.groupby("CountyCode").size().reset_index(name="arab_voter_count")

# Save the summary to a new CSV
arab_counts.to_csv("arab_voters_by_county.csv", index=False)
#264718
print("✅ Saved count of Arabic voters by CountyCode to 'arab_voters_by_county.csv'")
