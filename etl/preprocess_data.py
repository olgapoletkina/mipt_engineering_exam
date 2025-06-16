import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

def save_scaler(scaler, path="results/scaler.pkl"):
    with open(path, "wb") as f:
        pickle.dump(scaler, f)

if __name__ == "__main__":
    from load_data import load_data

    X, y = load_data()
    X_train_scaled, X_test_scaled, y_train, y_test, scaler = preprocess_data(X, y)
    print("Preprocessing done.")
    save_scaler(scaler)