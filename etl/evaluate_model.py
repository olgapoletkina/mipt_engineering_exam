import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
    }
    return metrics

def save_metrics(metrics, path="results/metrics.json"):
    import json
    with open(path, "w") as f:
        json.dump(metrics, f, indent=4)

if __name__ == "__main__":
    from load_data import load_data
    from preprocess_data import preprocess_data
    from train_model import train_model

    X, y = load_data()
    X_train_scaled, X_test_scaled, y_train, y_test, scaler = preprocess_data(X, y)
    model = train_model(X_train_scaled, y_train)

    metrics = evaluate_model(model, X_test_scaled, y_test)
    print("Evaluation done:", metrics)
    save_metrics(metrics)