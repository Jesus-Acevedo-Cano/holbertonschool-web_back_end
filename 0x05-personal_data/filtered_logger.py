#!/usr/bin/env python3
""" 0x05. Personal data """
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ returns the log message obfuscated """
    for i in fields:
        message = re.sub(r"{}=(.*?){}".format(i, separator),
                         f'{i}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class  """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """  constructor argument """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ method to filter values in incoming log records using """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
