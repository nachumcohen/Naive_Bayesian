import pandas as pd

class NaiveBayesClassifier:
    def __init__(self, model: dict, target_columns: str):
        self.model = model
        self.target_col = target_columns

    def predict_row(self, row: dict):
        scores = {}

        for label in self.model.keys():
            score = 1.0
            for col, value in row.items():
                score *= self.model[label][col].get(value, 1e-6)
            score *= self.model[label][self.target_col].get(label, 1e-6)
            scores[label] = score

        return max(scores, key=scores.get)

    def check_model_accuracy(self , df_testing :pd.DataFrame):
        correct = 0
        df_test = df_testing.iloc[:, :-1]

        for idx, row in df_test.iterrows():
            row_dict = row.to_dict()
            predicted = self.predict_row(row_dict)
            actual = df_testing.loc[idx, self.target_col]
            if predicted == actual:
                correct += 1

        return correct / len(df_testing) * 100

