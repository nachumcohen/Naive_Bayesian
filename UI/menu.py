import os
from Core.service import Service

def menu():

    while True:
      path = input("enter file path CSV: ").strip('"').strip()
      if not os.path.exists(path):
          print("path does not exist")
      elif not os.path.isfile(path):
          print("is not file")
      else:
          break

    service = Service(path)
    service.training()

    choice = input("choice: "
              "1: check model accuracy, "
              "2: prediction ")

    match choice:
        case "1":
            print(service.testing())
        case "2":
            print(service.test_row())

        case _:
            print("enter only numbers in menu")

if __name__ == '__main__':
    menu()


