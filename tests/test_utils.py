from datetime import datetime

import pytest
from PIL import Image

from clocklambda.utils import get_bitmap_from_image, get_time_strings, suffix


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

def test_ascii_hex_conversion():
    """Check that the asciihex conversion works"""
    im = Image.new("1", (3, 16))
    im.putpixel((0, 0), 1)
    im.putpixel((2, 15), 1)
    bitmap = get_bitmap_from_image(im)

    assert len(bitmap) == 3 * 4
    assert bitmap == "010000000080"
