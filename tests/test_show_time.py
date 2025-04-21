from datetime import datetime

import pytest

from clocklambda.show_time import get_time_image, get_time_result


@pytest.fixture
def timestring():
    return {"time": "08:24", "top": "Mon 21st", "bottom": "Apr 2025", "refresh": 58}

def test_image_size_is_correct_size(timestring):
    image = get_time_image(timestring)
    assert image.width == 96
    assert image.height == 16


def test_image_is_not_blank(timestring):
    image = get_time_image(timestring)

    assert image.entropy() != 0.0


def test_get_time_results_has_valid_refresh():
    now = datetime(2023, 10, 1, 12, 30, 45)

    actual = get_time_result(now)

    assert actual["refresh"] == 15


def test_get_time_results_has_valid_bitmap():
    now = datetime(2023, 10, 1, 12, 30, 45)

    actual = get_time_result(now)

    assert "bitmap" in actual
    assert len(actual["bitmap"]) == 96 * 4
