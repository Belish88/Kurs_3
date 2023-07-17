import datetime
import json


def open_file(path):
    """
    Open file json
    :param path: path file json
    :return: file for python
    """
    with open(path) as load_file:
        return json.loads(load_file.read())


def filter_executed(data):
    """
    filters executed operations
    :param data: data operations
    :return: data executed operations
    """
    executed_operation = []
    for operation in data:
        if operation.get("state") == "EXECUTED":
            executed_operation.append(operation)
    return executed_operation


def five_new_operation_sorted_for_date(executed_operation):
    """
    finds five new operations and sorted for date
    :param executed_operation: list executed operations
    :return: five new operstions
    """
    sorted_date = list(sorted(executed_operation,
                              key=lambda operation: operation['date'],
                              reverse=True))[:5]
    return sorted_date


def norm_format_date(date):
    """
    converted date for normal format
    :param date: date is data
    :return: normal format date
    """
    date_ = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return datetime.datetime.strftime(date_, '%d.%m.%Y')


def convert_from_to(data):
    """
    converted from and to
    :param data: data from and data to
    :return: from and to in new format
    """
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
    """
    displays result data
    :param data: data operations
    :return: data in new format
    """
    date_ = norm_format_date(data["date"])
    description_ = data["description"]
    from_ = convert_from_to(data["from"]) if data.get("from") else ""
    to_ = convert_from_to(data["to"])
    amount_ = data["operationAmount"]["amount"]
    name_ = data["operationAmount"]["currency"]["name"]
    return f'{date_} {description_}\n' \
           f'{from_} -> {to_}\n' \
           f'{amount_} {name_}\n'
