from datetime import datetime

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

    result = {
        "time": time,
        "top": f"{day} {date}{suffix(date)}",
        "bottom": mon_year,
        "refresh": remain
    }

    return result
