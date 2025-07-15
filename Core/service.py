import json

from Core.DataHandler import DataHandler
from Test.Tester import NaiveBayesClassifier
from Model.Train import NaiveBayesModel


class Service:


    def __init__(self , path):

        self.df = DataHandler.load_data(path)

        df_split = DataHandler.split_data(self.df)

        self.df_training = df_split[0]
        self.df_tester = df_split[1]

        self.target_col = self.df_training.columns[-1]

        self.model = NaiveBayesModel(self.df_training)


    def training(self):

        self.model.training()


    def testing(self):

        model = self.model.return_model()
        tester = NaiveBayesClassifier(model ,self.target_col)
        return tester.check_model_accuracy(self.df_tester)

    def test_row(self):

        input_row = ''
        dict_row = DataHandler.return_unique_csv(self.df_training)

        while True:
            input_ = input(f'enter dict with these possible values:\n{dict_row}\n')

            try:
                input_row = json.loads(input_)
            except json.JSONDecodeError:
                print("invalid json format. please use double quotes and valid json syntax.")
                continue

            if not isinstance(input_row, dict):
                print("enter a dictionary , json.")
                continue


            dict_correct = True
            for col in input_row.keys():
                if col not in dict_row:
                    print(f"column '{col}' not recognized.")
                    dict_correct = False
                    break
                if input_row[col] not in dict_row[col]:
                    print(f"value '{input_row[col]}' is not valid for column '{col}'.")
                    dict_correct = False
                    break

            if dict_correct:
                break
            else:
                print("enter correct values as shown above.")

        model = self.model.return_model()
        tester = NaiveBayesClassifier(model , self.target_col)
        return tester.predict_row(input_row)
