from sys import argv
from xgboost import XGBClassifier
from load_files import load_all_files


if __name__ == "__main__":
    X, _, indeces = load_all_files(argv[1:])
    
    model = XGBClassifier(random_state=45)
    model.load_model("model-data.json")

    pred = model.predict(X)

    print({f"{int(index)}": int(value) for index, value in zip(indeces, pred)})

