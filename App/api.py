from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from Core.service import Service
from Test.Tester import NaiveBayesClassifier

app = FastAPI()
service_instance = None


class PathInput(BaseModel):
    path: str


class InputRow(BaseModel):
    row: dict


@app.post("/load_path")
def load_csv_path(input_data: PathInput):
    global service_instance
    if not os.path.exists(input_data.path):
        raise HTTPException(status_code=404, detail="File path not found")

    service_instance = Service(input_data.path)
    return {"status": "file loaded", "path": input_data.path}


@app.post("/train")
def train_model():
    if not service_instance:
        raise HTTPException(status_code=400, detail="No dataset loaded")
    service_instance.training()
    return {"status": "model trained"}


@app.get("/test")
def test_model():
    if not service_instance:
        raise HTTPException(status_code=400, detail="No dataset loaded")
    accuracy = service_instance.testing()
    return {"accuracy": accuracy}


@app.post("/predict")
def predict_row(input_data: InputRow):
    if not service_instance:
        raise HTTPException(status_code=400, detail="No dataset loaded")

    model = service_instance.model.return_model()
    target_col = service_instance.target_col

    tester = NaiveBayesClassifier(model, target_col)
    result = tester.predict_row(input_data.row)
    return {"prediction": result}




