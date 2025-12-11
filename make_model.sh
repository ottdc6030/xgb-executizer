#!/bin/bash

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
    pip install pandas scikit-learn xgboost tl2cgen
fi

python train_model.py $*
