import pytest

from setting.path import JSON
from utils.functions import open_file


def test_open_file():
    assert isinstance(open_file(JSON), list)
    with pytest.raises(FileNotFoundError):
        open_file("gfghj")



