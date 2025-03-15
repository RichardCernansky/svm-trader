import joblib
import pickle
# import torch
# import tensorflow as tf
# from tensorflow.keras.models import load_model as keras_load_model


def load_model(model_path, model_type="sklearn"):
    """
    Load a model based on its type.

    Args:
        model_path (str): Path to the saved model file.
        model_type (str): Type of model to load. Options: "sklearn", "pytorch", "tensorflow".

    Returns:
        Loaded model object.
    """
    if model_type == "sklearn":
        # Load Scikit-learn models (SVM, RandomForest, etc.)
        return joblib.load(model_path)  # or pickle.load(open(model_path, 'rb'))

    # elif model_type == "pytorch":
    #     # Load PyTorch model
    #     model = torch.load(model_path)
    #     model.eval()  # Set model to evaluation mode
    #     return model
    #
    # elif model_type == "tensorflow":
    #     # Load TensorFlow/Keras model
    #     return keras_load_model(model_path)

    else:
        raise ValueError(f"Unsupported model type: {model_type}")


def load_scaler(scaler_path, scaler_type="sklearn"):
    """
    Load a scaler based on its type.

    Args:
        scaler_path (str): Path to the saved scaler file.
        scaler_type (str): Type of scaler to load. Options: "sklearn", "tensorflow".

    Returns:
        Loaded scaler object.
    """
    if scaler_type == "sklearn":
        # Load Scikit-learn scalers (StandardScaler, MinMaxScaler, etc.)
        return joblib.load(scaler_path)  # or pickle.load(open(scaler_path, 'rb'))

    # elif scaler_type == "tensorflow":
    #     # Load a TensorFlow/Keras custom scaler (if stored as a part of a model)
    #     return tf.keras.models.load_model(scaler_path)

    else:
        raise ValueError(f"Unsupported scaler type: {scaler_type}")