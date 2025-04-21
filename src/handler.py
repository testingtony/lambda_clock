"""AWS entry point."""

import json
from datetime import datetime

from clocklambda.show_time import get_time_result

# client = boto3.client("lambda")


def display(event, context):
    """Respond to calls."""
    result = get_time_result(datetime.now())  # noqa:DTZ005

    return {"statusCode": 200, "body": json.dumps(result)}
