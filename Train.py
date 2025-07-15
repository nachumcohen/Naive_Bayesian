import pandas as pd
from collections import defaultdict


class NaiveBayesModel:

    def __init__(self, file_csv : pd.DataFrame):

        self.file_csv = file_csv
        self.model = None

    def training(self):

        df = self.file_csv
        dict_naive_bayesian = defaultdict(lambda: defaultdict(lambda: defaultdict()))

        unique_values = {col: df[col].unique().tolist() for col in df.columns}
        last_column = df.columns[-1]

        for target in list(unique_values.values())[-1]:
            len_target = len(df[df[last_column] == target])
            for columns, rows in unique_values.items():
                for row in rows:
                    if columns == last_column:
                        if row == target:
                            dict_naive_bayesian[row][columns][row] = len_target / len(df)
                        continue
                    dict_naive_bayesian[target][columns][row] = (
                            (df[df[last_column] == target][columns].value_counts().get(row, 0) + 1) / (len_target + 1))

        self.model = dict_naive_bayesian
        print("Training was successful")

    def return_model(self):
        return self.model