import pandas as pd

# Load the merged voter data (with is_arabic already added)
merged_df = pd.read_csv("arab_voters_by_county.csv")

# Load the county mapping file
county_mapping_df = pd.read_csv("DHCS_County_Code_Reference_Table.csv")  # Has DHCS_County_Code, County_Name, etc.

# Keep only needed columns
county_mapping_df = county_mapping_df[['DHCS_County_Code', 'County_Name']]
county_mapping_df = county_mapping_df.rename(columns={"DHCS_County_Code": "CountyCode"})

# Merge to bring in County_Name
final_df = merged_df.merge(county_mapping_df, on='CountyCode', how='left')

# Check for any unmatched county codes
missing_counties = final_df['County_Name'].isna().sum()
print(f"🧐 Missing 'County_Name' for {missing_counties} records")

# Save final output
final_df.to_csv("arab_voters_by_countyWithNames.csv", index=False)
print("✅ Final file saved as 'final_voters_data.csv' with 'County_Name' added")
