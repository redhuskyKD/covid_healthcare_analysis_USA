import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQL
user = "root"
password = "root"
host = "127.0.0.1:3306"
database = "mydb"
table = "hrr_beds"

engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
df = pd.read_sql(f"SELECT * FROM {table}", con=engine)

# Step 1: Feature Engineering (as done earlier)
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna(subset=[
    'Available_ICU_Beds', 'Available_Hospital_Beds',
    'Potentially_Available_ICU_Beds', 'Projected_ICU_Individuals', 'Projected_Hospitalized_Individuals',
    'Total_ICU_Beds', 'Population_65_Plus', 'Adult_Population'
])

df['ICU_Stress'] = df['Projected_ICU_Individuals'] / df['Available_ICU_Beds']
df['Hospital_Stress'] = df['Projected_Hospitalized_Individuals'] / df['Available_Hospital_Beds']
df['Pop65_Proportion'] = df['Population_65_Plus'] / df['Adult_Population']
df['Surge_Gap'] = df['Projected_ICU_Individuals'] - df['Potentially_Available_ICU_Beds']

# Step 2: Select features for PCA
features = ['ICU_Stress', 'Hospital_Stress', 'Pop65_Proportion', 'Surge_Gap']
x = df[features]

# Step 3: Standardize
x_scaled = StandardScaler().fit_transform(x)

# Step 4: PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(x_scaled)
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

# Add back HRR info for labeling
pca_df['HRR'] = df['HRR']
pca_df['Risk_Label'] = df.get('Risk_Label', 'Unknown')  # fallback if not present

# Step 5: Plot
plt.figure(figsize=(10, 7))
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Risk_Label', palette='coolwarm', s=100, alpha=0.7)
plt.title("PCA of HRRs Based on Healthcare Risk Indicators")
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)")
plt.grid(True)
plt.tight_layout()
plt.show()
