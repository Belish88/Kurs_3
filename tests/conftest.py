import pytest


@pytest.fixture
def fixture_filter_executed():
    return [{
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
          "amount": "41096.24",
          "currency": {
            "name": "USD",
            "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
      },
      {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
          "amount": "67314.70",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
      }]


@pytest.fixture
def fixture_one_executed():
    return [{
      "id": 863064926,
      "state": "EXECUTED",
      "date": "2019-12-08T22:46:21.935582",
      "operationAmount": {
        "amount": "41096.24",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Открытие вклада",
      "to": "Счет 90424923579946435907"
    }]
