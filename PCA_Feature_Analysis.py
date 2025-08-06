import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Step 1: Load CSV
df = pd.read_csv("enhanced_risk_scored.csv")

# Step 2: Select features and preprocess
features = ['ICU_Stress', 'Hospital_Stress', 'Pop65_Proportion', 'Surge_Gap']
x = df[features]
x_scaled = StandardScaler().fit_transform(x)

# Step 3: PCA with 3 components
pca = PCA(n_components=3)
principal_components = pca.fit_transform(x_scaled)
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2', 'PC3'])
pca_df['HRR'] = df['HRR']
pca_df['Risk_Label'] = df['Risk_Label']
pca_df['Enhanced_Risk_Score'] = df['Enhanced_Risk_Score']

# Step 4: Feature Loading Interpretation
loadings = pd.DataFrame(pca.components_.T, index=features, columns=['PC1', 'PC2', 'PC3'])
print("📊 Feature Loadings:\n")
print(loadings.round(3))

# Step 5: Label Top 5 High-Risk HRRs
top_hrrs = df.nlargest(5, 'Enhanced_Risk_Score')[['HRR', 'Enhanced_Risk_Score']]
print("\n🔥 Top 5 High-Risk HRRs:")
print(top_hrrs)

# Step 6: K-Means Clustering on 2D PCA
kmeans = KMeans(n_clusters=3, random_state=42)
pca_df['Cluster'] = kmeans.fit_predict(pca_df[['PC1', 'PC2']])

# Step 7: 2D PCA Plot with Clusters and Labels
plt.figure(figsize=(10, 7))
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Cluster', palette='tab10', s=100, alpha=0.7)

# Annotate top HRRs
for _, row in top_hrrs.iterrows():
    label = row['HRR']
    pc_row = pca_df[pca_df['HRR'] == label]
    plt.text(pc_row['PC1'].values[0] + 0.2, pc_row['PC2'].values[0], label, fontsize=9)

plt.title("🔍 PCA with K-Means Clustering and Top High-Risk HRRs")
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
plt.legend(title='Cluster')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 8: 3D PCA Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(pca_df['PC1'], pca_df['PC2'], pca_df['PC3'],
           c=pca_df['Cluster'], cmap='Set2', s=60, alpha=0.8)

ax.set_title("🌐 3D PCA of HRRs with K-Means Clustering")
ax.set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
ax.set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
ax.set_zlabel(f"PC3 ({pca.explained_variance_ratio_[2]*100:.1f}%)")

plt.tight_layout()
plt.show()
