import datetime
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


def five_new_operation_sorted_for_date(executed_operation):
    sorted_date = list(sorted(executed_operation,
                              key=lambda operation: operation["date"],
                              reverse=True))[:5]
    return sorted_date


def norm_format_date(date):
    date_ = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return datetime.datetime.strftime(date_, '%d.%m.%Y')



# print(five_new_operation_sorted_for_date(filter_executed(open_file(JSON))))
# print(norm_format_date("2019-08-26T10:50:58.294041"))
