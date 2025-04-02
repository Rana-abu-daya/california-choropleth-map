import pandas as pd

# Load the CSVs
arab_voters_df = pd.read_csv("VRDB-california-arabic-classified.csv")        # contains 'voterId', 'is_arabic'
full_voters_df = pd.read_csv("VoterRegistrationData.csv")        # contains 'voterId' and full details
print(f"Number of Rows: {len(arab_voters_df)}")
print(f"Number of Rows: {len(full_voters_df)}")
# Merge on 'voterId'
# Keep only the needed columns
arab_voters_df = arab_voters_df[['StateVoterID', 'is_arabic']]

# Rename to align columns for merging
arab_voters_df = arab_voters_df.rename(columns={"StateVoterID": "RegistrantID"})

# Merge to bring is_arabic into the full data
merged_df = full_voters_df.merge(arab_voters_df, on="RegistrantID", how="left")

# Count missing values before filling
missing_count = merged_df['is_arabic'].isna().sum()
print(f"🧐 Missing 'is_arabic' for {missing_count} voters — these will be filled as 'Non_Arabic'")

# Fill missing values
merged_df['is_arabic'] = merged_df['is_arabic'].fillna("Non_Arabic")

# Save the result
merged_df.to_csv("VoterRegistrationDataArabicClassified.csv", index=False)

print("✅ Merged file saved as 'merged_voters_data.csv'")
