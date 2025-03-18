import pandas as pd

from src.models.svm_train import train_svm


def train_model(model: str, train_data: pd.DataFrame) -> str:
    """ chooses what model to train and returns the saved model path"""

    if model == "svm":
        return train_svm(train_data)

