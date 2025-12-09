from sys import argv
from xgboost import XGBClassifier
from load_files import load_all_files

if __name__ == "__main__":
    X, y, _ = load_all_files(argv[1:])
    
    model = XGBClassifier(random_state=45)
    model.fit(X, y)
    model.save_model("model-data.json")

    print(X)
    print(y)