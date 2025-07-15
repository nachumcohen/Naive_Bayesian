import pandas as pd

class DataHandler:

    @staticmethod
    def load_data(path):

        try:
            df = pd.read_csv(path)
            return df

        except FileNotFoundError as fe:
            print(f"load_data{fe}")
            return None

    @staticmethod
    def split_data(df, ratio = 0.7 , random_state = 42):

        df_shuffled = df.sample(frac=1, random_state= random_state)
        split_point = int(len(df_shuffled) * ratio)

        train = df_shuffled.iloc[:split_point]
        test = df_shuffled.iloc[split_point:]
        tuple_split = (train , test)
        return tuple_split

    @staticmethod
    def return_unique_csv(df):

        df = df

        unique_values = {
            col: df[col].unique().tolist()
            for col in df.columns[1:-1]
            if not df[col].is_unique
        }

        return unique_values


