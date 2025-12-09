# XGBClassifier Training and Prediction

This project trains an XGBClassifier model and packages it as a standalone executable.

## Training

Run the bash script with CSV files as arguments.

```bash
bash ./create_exec.sh file1.csv file2.csv file3.csv ...
```

All CSV files are concatenated in order and used as training data.

## Prediction

The resulting executable takes CSV files as arguments. These will also be concatenated in the order you put them in.

```bash
./run_model file1.csv file2.csv ...
```

stdout prints a dictionary. Each key-value pair is a prediction for a given run_index
