import json


def open_file(path):
    with open(path) as load_file:
        return json.loads(load_file.read())


# def data_output():
#     operations = open_file(JSON)
#     for data in operations:
#         return (f'{data["date"]} '
#                 f'{data["description"]}\n'
#                 f'{data["from"]} -> '
#                 f'{data["to"]}\n'
#                 f'{data["operationAmount"]["amount"]} '
#                 f'{data["operationAmount"]["currency"]["name"]}\n')
