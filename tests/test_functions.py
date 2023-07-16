import pytest

from setting.path import JSON
from utils.functions import open_file, filter_executed, norm_format_date, five_new_operation_sorted_for_date, \
    convert_from_to


def test_open_file():
    assert isinstance(open_file(JSON), list)
    with pytest.raises(FileNotFoundError):
        open_file("gfghj")


def test_filter_executed(fixture_filter_executed, fixture_one_executed):
    assert len(filter_executed(fixture_filter_executed)) == 1
    assert isinstance(filter_executed(fixture_filter_executed), list)
    assert filter_executed(fixture_filter_executed) == fixture_one_executed


def test_norm_format_date():
    assert norm_format_date("2019-12-08T22:46:21.935582") == "08.12.2019"


def test_five_new_operation_sorted_for_date(fixture_five_new_operation):
    assert len(five_new_operation_sorted_for_date(filter_executed(open_file(JSON)))) == 5
    assert five_new_operation_sorted_for_date(filter_executed(open_file(JSON))) == fixture_five_new_operation


def test_convert_from_to():
    assert convert_from_to("Счет 35383033474447895560") == "Счет **5560"
    assert convert_from_to("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
