ALTER TABLE hrr_beds
ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;
WITH ranked AS (
  SELECT id,
         ROW_NUMBER() OVER (
           PARTITION BY 
             HRR,
             Total_Hospital_Beds,
             Total_ICU_Beds,
             Available_Hospital_Beds,
             Potentially_Available_Hosp_Beds,
             Available_ICU_Beds,
             Potentially_Available_ICU_Beds,
             Adult_Population,
             Population_65_Plus,
             Projected_Infected_Individuals,
             Projected_Hospitalized_Individuals,
             Projected_ICU_Individuals,
             Hosp_Beds_Needed_6mo,
             Pct_Avail_Beds_Needed_6mo,
             Pct_Pot_Avail_Beds_Needed_6mo,
             Pct_Total_Beds_Needed_6mo,
             Hosp_Beds_Needed_12mo,
             Pct_Avail_Beds_Needed_12mo,
             Pct_Pot_Avail_Beds_Needed_12mo,
             Pct_Total_Beds_Needed_12mo,
             Hosp_Beds_Needed_18mo,
             Pct_Avail_Beds_Needed_18mo,
             Pct_Pot_Avail_Beds_Needed_18mo,
             Pct_Total_Beds_Needed_18mo,
             ICU_Beds_Needed_6mo,
             Pct_Avail_ICU_Beds_Needed_6mo,
             Pct_Pot_Avail_ICU_Beds_Needed_6mo,
             Pct_Total_ICU_Beds_Needed_6mo,
             ICU_Beds_Needed_12mo,
             Pct_Avail_ICU_Beds_Needed_12mo,
             Pct_Pot_Avail_ICU_Beds_Needed_12mo,
             Pct_Total_ICU_Beds_Needed_12mo,
             ICU_Beds_Needed_18mo,
             Pct_Avail_ICU_Beds_Needed_18mo,
             Pct_Pot_Avail_ICU_Beds_Needed_18mo,
             Pct_Total_ICU_Beds_Needed_18mo
           ORDER BY id
         ) AS rn
  FROM hrr_beds
)
DELETE FROM hrr_beds
WHERE id IN (
  SELECT id FROM ranked WHERE rn > 1
);
