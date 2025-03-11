import pandas as pd
import joblib as jl
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from load_data import load_data

df = load_data('data/BTCUSDT_hourly.csv')
# Select features
features = ["Close", "bb_pct", "macd", "macd_signal", "rsi"]
X = df[features]
y = df["label"]

# standardize data
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


# Train SVM model
print("Started training SVM...")
svm = SVC(kernel="rbf", probability=True, class_weight="balanced")  # Class weighting for imbalance
svm.fit(X_train, y_train)
print("Finished training SVM...")

jl.dump(svm, "models/svm_model.pkl")
jl.dump(scaler, "models/scaler_model.pkl")
print("Model saved successfully!")






