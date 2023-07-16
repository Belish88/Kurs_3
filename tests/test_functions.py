import pytest

from setting.path import JSON
from utils.functions import open_file, filter_executed, norm_format_date


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
