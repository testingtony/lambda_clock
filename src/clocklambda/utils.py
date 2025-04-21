"""General utils."""

from datetime import datetime

from PIL import Image


def suffix(dd: str) -> str:
    """Return the suffix of a number."""
    if dd.endswith("1") and not dd.endswith("11"):
        return "st"
    elif dd.endswith("2") and not dd.endswith("12"):
        return "nd"
    elif dd.endswith("3") and not dd.endswith("13"):
        return "rd"
    else:
        return "th"


def get_time_strings(now: datetime) -> dict:
    """Get the current time strings."""
    time = now.strftime("%H:%M")
    day = now.strftime("%a")
    date = str(now.day)
    mon_year = now.strftime("%b %Y")
    remain = 60 - int(now.strftime("%S"))

    result = {"time": time, "top": f"{day} {date}{suffix(date)}", "bottom": mon_year, "refresh": remain}

    return result


def get_bitmap_from_image(image: Image.Image) -> str:
    """Get the asciihex representation for the image."""
    width = image.width
    height = image.height
    assert height == 16
    buff = ""
    for x in range(width):
        v = 0x0000
        for y in range(height):
            v = v | (0x10000 * image.getpixel((x, y)))
            v = v >> 1
        buff += f"{v & 0xFF:02X}{(v >> 8) & 0xFF:02X}"
    return buff
