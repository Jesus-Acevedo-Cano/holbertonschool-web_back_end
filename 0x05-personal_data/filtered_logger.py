#!/usr/bin/env python3
import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """ returns the log message obfuscated """
    for i in fields:
        message = re.sub(r"{}=(.*?){}".format(i, separator),
                         f'{i}={redaction}{separator}', message)
    return message
