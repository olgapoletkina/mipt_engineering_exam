import os

def ensure_results_dir(path="results/"):
    if not os.path.exists(path):
        os.makedirs(path)
    print(f"Results directory ensured: {path}")

if __name__ == "__main__":
    ensure_results_dir()