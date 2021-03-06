import pytest
from app.main import is_odd


data_provider = (
    (2, True),
    (33, False),
    (44, True),
    (11, False),
)


@pytest.mark.parametrize(['number', 'expected'], data_provider)
def test_is_odd(number, expected):
    assert is_odd(number) == expected