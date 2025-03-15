import joblib
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from src.data.load_data import data_train_test
from src.config import *

#load data
print("Loading data...")
X_train, X_test, y_train, y_test = data_train_test(BTCUSDT_data_path)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

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
print(f"Model saved: {SVM_MODEL_PATH}")
