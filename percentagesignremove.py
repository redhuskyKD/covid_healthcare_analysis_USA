import pandas as pd

# Load your cleaned column-name CSV
df = pd.read_csv("cleaned_merged_data.csv")

# List of columns that are percentages (as per our column naming convention)
percentage_cols = [col for col in df.columns if 'Pct_' in col]

# Convert % strings like "45.2%" to float decimals like 0.452
for col in percentage_cols:
    df[col] = df[col].astype(str).str.replace('%', '', regex=False).str.strip()
    df[col] = pd.to_numeric(df[col], errors='coerce') # convert to float in [0, 1]

# Optional: Fill NaNs with 0 or leave as-is depending on your preference
df.fillna(0, inplace=True)

# Save to a new CSV for SQL import
df.to_csv("final_hrr_data.csv", index=False)

print("✅ Percentage values converted to decimals and saved to 'final_hrr_data.csv'")
