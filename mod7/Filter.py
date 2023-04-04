import logging
import string


class Filter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return str.isascii(record.message)
        # return not any(char not in string.printable for char in record.message)
