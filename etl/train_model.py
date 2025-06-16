import pickle
from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train, random_state=42, max_iter=1000):
    model = LogisticRegression(random_state=random_state, max_iter=max_iter)
    model.fit(X_train, y_train)
    return model

def save_model(model, path="results/model.pkl"):
    with open(path, "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    from load_data import load_data
    from preprocess_data import preprocess_data

    X, y = load_data()
    X_train_scaled, X_test_scaled, y_train, y_test, scaler = preprocess_data(X, y)

    model = train_model(X_train_scaled, y_train)
    print("Model trained.")
    save_model(model)