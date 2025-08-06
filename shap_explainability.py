import pandas as pd
import numpy as np
import shap
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Step 1: Load Data
df = pd.read_csv("enhanced_risk_scored.csv")

# Step 2: Encode Risk_Label
le = LabelEncoder()
df['Risk_Code'] = le.fit_transform(df['Risk_Label'])

# Step 3: Select Features and Target
features = ['ICU_Stress', 'Hospital_Stress', 'Pop65_Proportion', 'Surge_Gap']
X = df[features]
y = df['Risk_Code']

# Step 4: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Step 5: Train XGBoost Classifier
model = xgb.XGBClassifier(n_estimators=100, random_state=42, eval_metric='mlogloss')
model.fit(X_train, y_train)

# Step 6: SHAP Explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_train)

# Step 7: Global Feature Importance (Bar)
shap.summary_plot(shap_values, X_train, plot_type="bar", class_names=le.classes_)

# Step 8: Individual Force Plot
sample_idx = 2  # Make sure this is valid
sample_features = X_train.iloc[sample_idx:sample_idx+1]  # Must be a 2D DataFrame

true_class = y_train.iloc[sample_idx]
print(f"True Class: {le.classes_[true_class]}")

shap.force_plot(
    explainer.expected_value[true_class],
    shap_values[true_class][sample_idx],
    sample_features,
    matplotlib=True,
    show=True
)
