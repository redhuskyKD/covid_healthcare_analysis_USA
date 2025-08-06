import pandas as pd

# Load your merged CSV file
df = pd.read_csv("merged_data.csv")

# Define the new column names (in exact order)
new_column_names = [
    "HRR",
    "Total_Hospital_Beds",
    "Total_ICU_Beds",
    "Available_Hospital_Beds",
    "Potentially_Available_Hosp_Beds",
    "Available_ICU_Beds",
    "Potentially_Available_ICU_Beds",
    "Adult_Population",
    "Population_65_Plus",
    "Projected_Infected_Individuals",
    "Projected_Hospitalized_Individuals",
    "Projected_ICU_Individuals",
    "Hosp_Beds_Needed_6mo",
    "Pct_Avail_Beds_Needed_6mo",
    "Pct_Pot_Avail_Beds_Needed_6mo",
    "Pct_Total_Beds_Needed_6mo",
    "Hosp_Beds_Needed_12mo",
    "Pct_Avail_Beds_Needed_12mo",
    "Pct_Pot_Avail_Beds_Needed_12mo",
    "Pct_Total_Beds_Needed_12mo",
    "Hosp_Beds_Needed_18mo",
    "Pct_Avail_Beds_Needed_18mo",
    "Pct_Pot_Avail_Beds_Needed_18mo",
    "Pct_Total_Beds_Needed_18mo",
    "ICU_Beds_Needed_6mo",
    "Pct_Avail_ICU_Beds_Needed_6mo",
    "Pct_Pot_Avail_ICU_Beds_Needed_6mo",
    "Pct_Total_ICU_Beds_Needed_6mo",
    "ICU_Beds_Needed_12mo",
    "Pct_Avail_ICU_Beds_Needed_12mo",
    "Pct_Pot_Avail_ICU_Beds_Needed_12mo",
    "Pct_Total_ICU_Beds_Needed_12mo",
    "ICU_Beds_Needed_18mo",
    "Pct_Avail_ICU_Beds_Needed_18mo",
    "Pct_Pot_Avail_ICU_Beds_Needed_18mo",
    "Pct_Total_ICU_Beds_Needed_18mo"
]

# Replace column names
df.columns = new_column_names

# Save the cleaned CSV
df.to_csv("cleaned_merged_data.csv", index=False)

print("✅ CSV cleaned and saved as 'cleaned_merged_data.csv'")
