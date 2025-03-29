"""Do some stuff."""
import json
from datetime import datetime

from timelambda.utils import get_time_strings

import boto3

#client = boto3.client("lambda")

def display(event, context):
    """I don't know what it does yet."""

    result = get_time_strings(datetime.now())

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
