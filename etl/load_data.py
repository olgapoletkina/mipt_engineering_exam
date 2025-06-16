import pandas as pd
from sklearn.datasets import load_breast_cancer

def load_data(as_frame=True):
    X, y = load_breast_cancer(return_X_y=True, as_frame=as_frame)
    return X, y

if __name__ == "__main__":
    X, y = load_data()
    print(f"Features shape: {X.shape}")
    print(f"Target distribution:\n{y.value_counts()}")