import json

from setting.path import JSON


def open_file(path):
    with open(path) as load_file:
        return json.loads(load_file.read())


def filter_executed(data):
    executed_operation = []
    for operation in data:
        if operation.get("state") == "EXECUTED":
            executed_operation.append(operation)
    return executed_operation


# print(filter_executed(open_file(JSON)))
