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


def convert_from_to(data):
    if data.startswith('Счет'):
        return data[0:5] + "**" + data[-4:]
    else:
        name = ""
        numer = ""
        for i in data:
            if '0' <= i <= '9':
                numer += i
            else:
                name += i
        return f'{name}{numer[0:4]} {numer[4:6]}** **** {numer[-4:]}'


def result_data(data):
    date_ = norm_format_date(data["date"])
    description_ = data["description"]
    from_ = convert_from_to(data["from"]) if data.get("from") else ""
    to_ = convert_from_to(data["to"])
    amount_ = data["operationAmount"]["amount"]
    name_ = data["operationAmount"]["currency"]["name"]
    return f'{date_} {description_}\n' \
           f'{from_} -> {to_}\n' \
           f'{amount_} {name_}\n'


# print(five_new_operation_sorted_for_date(filter_executed(open_file(JSON))))
# print(norm_format_date("2019-08-26T10:50:58.294041"))
# print(covert_from_to("Счет 35383033474447895560"))
# print(covert_from_to("MasterCard 7158300734726758"))
# for operation in five_new_operation_sorted_for_date(filter_executed(open_file(JSON))):
#     print(result_data(operation))
