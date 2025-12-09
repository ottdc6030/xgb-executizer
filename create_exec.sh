#!/bin/bash

EXEC_NAME="run_model"

VENV_DIR="train_venv"

PY_VERSION=$(python3 --version | awk '{print $2}' | cut -d. -f1,2)

MAKE_VENV=false
if [ ! -d "$VENV_DIR" ]; then
    MAKE_VENV=true
fi

if $MAKE_VENV; then
    sudo apt install python$PY_VERSION-venv
    python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

if $MAKE_VENV; then
    pip install --upgrade pip
    pip install pandas scikit-learn xgboost pyinstaller
    pip install --upgrade pyinstaller 
fi

python create_model.py $* && \
pyinstaller --onefile \
    --collect-all xgboost \
    --collect-submodules sklearn \
    --add-data=./model-data.json:. \
    --distpath=. \
    --name="$EXEC_NAME" \
    test_model.py
