import joblib
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from src.data.load_data import enhance_data
from src.config import *

#CONSTS
SVM_MODEL_PATH = "models/svm/svm_model.pkl"
SVM_SCALER_PATH = "models/svm/svm_scaler.pkl"

def train_svm(train_data: pd.DataFrame) -> [str, str]:
    """trains SVM and return the model_path, scaler_path"""
    #load data
    print("Loading data...")
    train_data = enhance_data(train_data)
    X = train_data[DATA_FEATURES]
    y = train_data["label"]

    # Split into training (80%) and testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print("Training data shapes: ", X_train.shape, X_test.shape, y_train.shape, y_test.shape)

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

    return SVM_MODEL_PATH, SVM_SCALER_PATH
