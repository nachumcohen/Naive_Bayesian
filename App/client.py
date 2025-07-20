import json

import requests
import os

import App.server_url

SERVER_URL = App.server_url.return_url()

def get_valid_path():
    path = input("enter path file CSV: ").strip()
    if not os.path.exists(path) or not os.path.isfile(path):
        print("path is not invalid or does not exist")
        exit(1)
    return path

def send_path_to_server(path):

    data = {"path": path}
    response = requests.post(f"{SERVER_URL}/load_path", json=data)
    if response.status_code == 200:
        print("path is sent and saved on the server")
    else:
        print("Error sending path", response.status_code)
        print(response.text)
        exit(1)

def send_train_request():
    response = requests.post(f"{SERVER_URL}/train")
    if response.status_code == 200:
        print("model train successfully")
    else:
        print("Error on train", response.status_code)
        print(response.text)

def send_predict_request():
    input_row = input("enter row to prediction").strip()

    try:
        input_dict = json.loads(input_row)
    except json.JSONDecodeError as e:
        print("Invalid JSON format:", e)
        exit(1)

    payload = {"row": input_dict}
    response = requests.post(f"{SERVER_URL}/predict", json=payload)
    if response.status_code == 200:
        print("prediction result", response.json())
    else:
        print("prediction error", response.status_code)
        print(response.text)

def send_test_request():
    response = requests.get(f"{SERVER_URL}/test")
    if response.status_code == 200:
        print("test result", response.json())
    else:
        print("tests error", response.status_code)
        print(response.text)

def main():
    path = get_valid_path()
    send_path_to_server(path)
    send_train_request()
    send_predict_request()
    send_test_request()

if __name__ == "__main__":
    main()