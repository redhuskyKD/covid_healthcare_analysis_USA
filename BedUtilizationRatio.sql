SELECT 
  HRR,
  Total_Hospital_Beds,
  Available_Hospital_Beds,
  ROUND((Total_Hospital_Beds - Available_Hospital_Beds) / Total_Hospital_Beds, 2) AS Utilization_Rate
FROM hrr_beds
ORDER BY Utilization_Rate DESC
LIMIT 10;
