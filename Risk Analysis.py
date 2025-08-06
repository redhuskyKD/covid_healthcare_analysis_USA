import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load CSV
df = pd.read_csv("enhanced_risk_scored.csv")

# Step 2: Check required columns
required_cols = [
    'ICU_Stress', 'Hospital_Stress', 'Pop65_Proportion', 'Surge_Gap', 'HRR', 'Risk_Label'
]
missing_cols = [col for col in required_cols if col not in df.columns]
if missing_cols:
    raise ValueError(f"Missing columns in CSV: {missing_cols}")

# Step 3: Prepare feature matrix
features = ['ICU_Stress', 'Hospital_Stress', 'Pop65_Proportion', 'Surge_Gap']
x = df[features]

# Step 4: Standardize
x_scaled = StandardScaler().fit_transform(x)

# Step 5: Apply PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(x_scaled)
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

# Step 6: Add back labels
pca_df['HRR'] = df['HRR']
pca_df['Risk_Label'] = df['Risk_Label']

# Step 7: Plot
plt.figure(figsize=(10, 7))
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Risk_Label', palette='Set1', s=100, alpha=0.8)

plt.title("PCA of HRRs Based on Healthcare Stress Features")
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)")
plt.grid(True)
plt.tight_layout()
plt.show()
