from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from src.config import *
from src.utils.model_loader import load_model, load_scaler
from src.data.load_data import data_train_test  # Function to load test data

#set up model
MODEL_PATH = SVM_MODEL_PATH
SCALER_PATH = SVM_SCALER_PATH

# Load test data (Ensure dataset has already been preprocessed)
X_test, y_test = data_train_test(BTCUSDT_data_path, test=True)  # Example function

# Load trained model & scaler
model = load_model(MODEL_PATH)
scaler = load_model(SCALER_PATH)

# Scale test data
X_test_scaled = scaler.transform(X_test)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Compute evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="macro")  # Use "binary" if it's binary classification
recall = recall_score(y_test, y_pred, average="macro")
f1 = f1_score(y_test, y_pred, average="macro")

# Print results
print(f"Model Performance Metrics:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-score: {f1:.4f}")
