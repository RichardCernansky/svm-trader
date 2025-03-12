import joblib
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from src.data.load_data import load_crypto_data
from src.config import *

#load data
print("Loading data...")
X_train, X_test, y_train, y_test = load_crypto_data()

#scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#train model
print("Training SVM model...")
svm = SVC(kernel="rbf", probability=True, class_weight="balanced")
svm.fit(X_train_scaled, y_train)

#save model and scaler
joblib.dump(svm, SVM_MODEL_PATH)
joblib.dump(scaler, SVM_SCALER_PATH)
print("Model saved: models/svm/svm_model.pkl")
