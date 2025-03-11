import joblib as jl
from sklearn.model_selection import train_test_split
from load_data import load_data

#load model
svm = jl.load('models/svm_model.pkl')
scaler = jl.load('models/scaler_model.pkl')

#load data
df = load_data('data/BTCUSDT_hourly.csv')
# Select features
features = ["Close", "bb_pct", "macd", "macd_signal", "rsi"]
X = df[features]
y = df["label"]

X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# evaluate the model on the test set
accuracy = svm.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")