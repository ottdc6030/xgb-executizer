from pandas import read_csv, concat, DataFrame

def load_all_files(collection, condense=True):
    df = [read_csv(file) for file in collection]
    df = concat(df, ignore_index=True)

    has_answers = "optimal_policy" in df.columns

    mega_rows = []
    mega_columns = [*filter(lambda name: name not in ["optimal_policy","run_index","first-touch","interleave","preferred_0", "preferred_1"], df.columns)]

    for index in df["run_index"].unique():
        fragment = df[df["run_index"] == index]

        assert len(fragment) == 4, f"IMPROPER SIZE {len(fragment)} OF INDEX {index}"

        if has_answers:
            unique_count = fragment["optimal_policy"].nunique()
            assert unique_count == 1, f"MORE THAN ONE PREFERRED POLICY {unique_count} IN INDEX {index}"
        
        for field in ["first-touch", "interleave", "preferred_0", "preferred_1"]:
            assert fragment[field].value_counts()[1] == 1, f"MORE THAN ONE COPY OF POLICY: {field} IN INDEX {index}"

        if not condense: continue

        #Condensing assumes that that runs with run_index value x are directly connected to each other across every file and that it's not just a counting variable
        #If this isn't correct, let me know (or just pass false into the condense parameter)

        mega_row = {"run_index": index}

        if has_answers: mega_row["optimal_policy"] = fragment["optimal_policy"].unique()[0]

        for _, row in fragment.iterrows():
            if row["first-touch"]:
                suffix = "_on_first-touch"
            elif row["interleave"]:
                suffix = "_on_interleave"
            elif row["preferred_0"]:
                suffix = "_on_preferred_0"
            else:
                suffix = "_on_preferred_1"

            mega_row = mega_row | {f"{col}{suffix}": row[col] for col in mega_columns}


        mega_rows.append(mega_row)


    if condense: df = DataFrame(mega_rows)

    if has_answers:
        X = df.drop(["run_index","optimal_policy"], axis=1)
        y = df["optimal_policy"]
    else:
        X = df.drop(["run_index"],axis=1)
        y = None
    
    return X, y, df["run_index"]