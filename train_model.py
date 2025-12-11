from sys import argv
from xgboost import XGBClassifier
from load_files import load_all_files
import treelite
import tl2cgen

def train(files, binary_name="./model.so"):
    X, y, _ = load_all_files(files)

    model = XGBClassifier(random_state=45)
    model._estimator_type = "classifier"
    model.fit(X, y)

    model_name = "model-data.json"

    model.save_model(model_name)

    model = treelite.frontend.load_xgboost_model(model_name)

    tl2cgen.export_lib(model, toolchain="gcc", libpath=binary_name)

if __name__ == "__main__":
    train(argv[1:])
    
    
