from fastapi import FastAPI
from main import tester

app = FastAPI()

# @app.post("/train")
# def train(path : dict[str , str]):
#
#     t = Service(path.get("path"))
#     t.training()


@app.post("/predict")
def predict(input_row : dict[str , str]):
    prediction = tester.predict_single_row(input_row)
    return {"prediction" : prediction}



