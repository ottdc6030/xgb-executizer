from sys import argv
from xgboost import XGBClassifier
from load_files import load_all_files
import tl2cgen
import numpy as np

model = None
current_model_path = None

def evaluate(files, model_path="./model.so"):
    global model
    global current_model_path

    if model is None or model_path != current_model_path:
        model = tl2cgen.Predictor(model_path)
        current_model_path = model_path

    X, _, indeces = load_all_files(files)
    matrix = tl2cgen.DMatrix(X.values)

    pred_proba = model.predict(matrix)
    pred_proba = pred_proba.squeeze()
    pred = np.argmax(pred_proba, axis=1)

    return {i: p.item() for i, p in zip(indeces, pred)}
    

if __name__ == "__main__":
    print(evaluate(argv[1:]))