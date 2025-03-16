from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def class_metrics(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average="macro")  # Use "binary" if it's binary classification
    recall = recall_score(y_true, y_pred, average="macro")
    f1 = f1_score(y_true, y_pred, average="macro")

    return round(accuracy,4), round(precision,4), round(recall,4), round(f1,4)