from timelambda.utils import suffix, get_time_strings
from datetime import datetime

import pytest
@pytest.mark.parametrize(
    "value,exepected",
    [
        ("1", "st"),
        ("2", "nd"),
        ("3", "rd"),
        ("4", "th"),
        ("11", "th"),
        ("12", "th"),
        ("13", "th"),
        ("21", "st"),
        ("22", "nd"),
        ("30", "th"),
        ("31", "st"),
    ],
)

def test_suffix(value, exepected):
    """Test the suffix function."""
    assert suffix(value) == exepected


def test_get_time_strings():
    """Test the get_time_strings function."""
    now = datetime(2023, 10, 1, 12, 30, 45)
    expected = {
        "time": "12:30",
        "top": "Sun 1st",
        "bottom": "Oct 2023",
        "refresh": 15
    }
    assert get_time_strings(now) == expected