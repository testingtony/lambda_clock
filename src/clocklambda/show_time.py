"""Create an image with the time."""

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from clocklambda.utils import get_bitmap_from_image, get_time_strings


def get_time_image(timestrings: dict[str, str]) -> Image.Image:
    """Return a PIL image baseed on the timestrings passed."""
    flip = Image.new("1", (96, 16))
    draw = ImageDraw.Draw(flip)
    font_8 = ImageFont.load("images/unscii.pil")
    font_16 = ImageFont.load("images/unscii_16.pil")

    draw.text((1, 0), timestrings["time"], 1, font_16)  # this is 31 dots long
    width = font_8.getlength(timestrings["top"])
    draw.text((31 + (65 - width) / 2, 0), timestrings["top"], 1, font_8)
    width = font_8.getlength(timestrings["bottom"])
    draw.text((31 + (65 - width) / 2, 8), timestrings["bottom"], 1, font_8)

    return flip


def get_time_result(now: datetime) -> dict[str, str]:
    """Return a result with the bitmap and refreshtime."""
    timestrings = get_time_strings(now)
    image = get_time_image(timestrings)
    bitmap = get_bitmap_from_image(image)
    return {"bitmap": bitmap, "refresh": timestrings["refresh"]}

    return None
